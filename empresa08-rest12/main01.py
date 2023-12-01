# Importar o módulo sqlite3 e a classe Flask, objeto request e o objeto jsonify:
import sqlite3
from flask import Flask, request, jsonify, g

# Criar o objeto Flask app:
app = Flask(__name__)

# Definir o caminho do banco de dados SQLite:
DATABASE = 'produtos.db'

# Definir uma função para obter uma conexão com o banco de dados:
def get_db_connection():
    # Verificar se o objeto g já tem uma conexão:
    db = getattr(g, '_database', None)
    # Se não tiver, criar uma nova conexão:
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Definir uma função row_factory para converter os resultados em objetos Row:
        db.row_factory = sqlite3.Row
    # Retornar a conexão:
    return db

# Definir uma função para fechar a conexão com o banco de dados quando o contexto da aplicação terminar:
@app.teardown_appcontext
def close_connection(exception):
    # Verificar se o objeto g tem uma conexão:
    db = getattr(g, '_database', None)
    # Se tiver, fechar a conexão:
    if db is not None:
        db.close()

# Definir uma função para executar consultas SQL no banco de dados:
def query_db(query, args=()):
    # Obter a conexão com o banco de dados:
    conn = get_db_connection()
    # Obter o objeto cursor:
    cur = conn.cursor()
    # Executar o comando SQL:
    cur.execute(query, args)
    # Obter os resultados:
    results = cur.fetchall()
    # Fechar o objeto cursor:
    cur.close()
    # Retornar os resultados:
    return results

# Criar uma tabela no banco de dados para armazenar os dados dos produtos:
with app.app_context():
    query_db('CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT, preco REAL)')

# Inserir alguns dados na tabela produtos:
with app.app_context():
    query_db('INSERT INTO produtos (nome, preco) VALUES (?, ?)', ('sapato', 128.55))
    query_db('INSERT INTO produtos (nome, preco) VALUES (?, ?)', ('camisa', 49.89))
    query_db('INSERT INTO produtos (nome, preco) VALUES (?, ?)', ('calça', 89.99))
    query_db('INSERT INTO produtos (nome, preco) VALUES (?, ?)', ('bermuda', 78.63))

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    # Definir a consulta SQL para obter todos os produtos:
    query = 'SELECT * FROM produtos'
    # Verificar se o cabeçalho X-nome-produto está presente na requisição:
    if 'X-nome-produto' in request.headers:
        # Obter o valor do cabeçalho:
        nome = request.headers['X-nome-produto']
        # Modificar a consulta SQL para filtrar os produtos por nome:
        query = query + ' WHERE nome = ?'
        # Executar a consulta SQL e obter os resultados:
        resp = query_db(query, (nome,))
    else:
        # Executar a consulta SQL e obter os resultados:
        resp = query_db(query)
        # Converter os resultados em uma lista de dicionários:
    resp = [dict(row) for row in resp]
    # Retornar os resultados convertidos em JSON:
    return jsonify(resp)

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
