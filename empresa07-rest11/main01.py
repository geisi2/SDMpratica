from flask import Flask, request, jsonify, g
#importa o módulo sqlite3 do Python
import sqlite3 

app = Flask(__name__)

# Criar uma função para obter a conexão com o banco de dados SQLite
def get_db():
    # Se a conexão não existir no contexto da aplicação, criar uma nova
    if 'db' not in g:
        g.db = sqlite3.connect('produtos.db')
        # Configurar o cursor para retornar as linhas como dicionários
        g.db.row_factory = sqlite3.Row
    # Retornar a conexão
    return g.db

# Criar uma função para fechar a conexão com o banco de dados SQLite
def close_db(e=None):
    # Obter a conexão do contexto da aplicação
    db = g.pop('db', None)
    # Se a conexão existir, fechá-la
    if db is not None:
        db.close()

# Registrar a função de fechar a conexão com o banco de dados SQLite na aplicação Flask
app.teardown_appcontext(close_db)

# Criar uma função para inicializar o banco de dados SQLite
def init_db():
    # Obter a conexão com o banco de dados SQLite
    db = get_db()
    # Criar um cursor para executar comandos SQL
    cur = db.cursor()
    # Criar uma tabela de produtos no banco de dados, se ela não existir
    cur.execute('CREATE TABLE IF NOT EXISTS produtos (nome TEXT, preco REAL)')
    # Inserir os dados dos produtos na tabela, usando uma transação SQL
    cur.executescript('''
    BEGIN TRANSACTION;
    INSERT INTO produtos VALUES ('sapato', 128.55);
    INSERT INTO produtos VALUES ('camisa', 49.89);
    INSERT INTO produtos VALUES ('calça', 89.99);
    INSERT INTO produtos VALUES ('bermuda', 78.63);
    COMMIT;
    ''')
    # Salvar as alterações no banco de dados
    db.commit()

# Chamar a função de inicializar o banco de dados SQLite dentro de um contexto da aplicação
with app.app_context():
    init_db()

# modifica as rotas da aplicação Flask para usar o banco de dados SQLite em vez da lista de produtos em memória.

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    # Obter a conexão com o banco de dados SQLite
    db = get_db()
    # Criar um cursor para executar comandos SQL
    cur = db.cursor()
    # Consultar todos os produtos na tabela, usando um gerador para iterar sobre as linhas
    produtos = (dict(produto) for produto in cur.execute('SELECT * FROM produtos'))
    # Retornar os produtos em formato JSON
    return jsonify({'produtos': list(produtos)})

# http://127.0.0.1:5000/produtos/camisa
@app.route('/produtos/<string:nome>', methods=['GET'])
def retornar_dados_do_produto_informado(nome):
    # Obter a conexão com o banco de dados SQLite
    db = get_db()
    # Criar um cursor para executar comandos SQL
    cur = db.cursor()
    # Consultar o produto com o nome informado na tabela
    produto = cur.execute('SELECT * FROM produtos WHERE nome = ?', (nome,)).fetchone()
    # Verificar se o produto existe
    if produto is None:
        # Retornar um código de status 404 (não encontrado)
        return jsonify({'mensagem': 'Produto não encontrado'}), 404
    # Retornar o produto em formato JSON
    return jsonify({'produto': dict(produto)})

# http://127.0.0.1:5000/produtos/cinto/45.67
@app.route('/produtos/<string:nome>/<float:preco>', methods=['POST'])
def inserir_produto(nome, preco):
    # Obter a conexão com o banco de dados SQLite
    db = get_db()
    # Criar um cursor para executar comandos SQL
    cur = db.cursor()
    # Inserir o novo produto na tabela, usando uma instrução SQL preparada
    cur.execute('INSERT INTO produtos VALUES (?, ?)', (nome, preco))
    # Salvar as alterações no banco de dados
    db.commit()
    # Retornar o produto inserido em formato JSON
    return jsonify({'produto': nome, 'preco': preco})

# http://127.0.0.1:5000/produtos/camisa/10.00
# http://127.0.0.1:5000/produtos/camisa/-10.00
@app.route('/produtos/<string:nome>/<float(signed=True):preco>',
methods=['PATCH'])
def alterar_preco_do_produto(nome, preco):
    # Obter a conexão com o banco de dados SQLite
    db = get_db()
    # Criar um cursor para executar comandos SQL
    cur = db.cursor()
    # Alterar o preço do produto com o nome informado na tabela
    cur.execute('UPDATE produtos SET preco = preco + ? WHERE nome = ?', (preco, nome))
    # Salvar as alterações no banco de dados
    db.commit()
    # Consultar o produto alterado na tabela
    produto = cur.execute('SELECT * FROM produtos WHERE nome = ?', (nome,)).fetchone()
    # Verificar se o produto existe
    if produto is None:
        # Retornar um código de status 404 (não encontrado)
        return jsonify({'mensagem': 'Produto não encontrado'}), 404
    # Retornar o produto alterado em formato JSON
    return jsonify({'produto': dict(produto)})

# http://127.0.0.1:5000/produtos/camisa
@app.route('/produtos/<string:nome>', methods=['DELETE'])
def remover_produto(nome):
    # Obter a conexão com o banco de dados SQLite
    db = get_db()
    # Criar um cursor para executar comandos SQL
    cur = db.cursor()
    # Remover o produto com o nome informado da tabela
    cur.execute('DELETE FROM produtos WHERE nome = ?', (nome,))
    # Salvar as alterações no banco de dados
    db.commit()
    # Consultar todos os produtos na tabela, usando um gerador para iterar sobre as linhas
    produtos = (dict(produto) for produto in cur.execute('SELECT * FROM produtos'))
    # Retornar os produtos em formato JSON
    return jsonify({'produtos': list(produtos)})

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
