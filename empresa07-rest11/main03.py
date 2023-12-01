from flask import Flask, jsonify, request
app = Flask(__name__)

# Criar uma lista de dicionários para armazenar os dados dos itens do cardápio
cardapio = [{'codigo': 1, 'produto': 'Cachorro quente', 'preco': 12.00},
            {'codigo': 2, 'produto': 'Sanduíche', 'preco': 23.89},
            {'codigo': 3, 'produto': 'Pastel', 'preco': 3.98},
            {'codigo': 4, 'produto': 'Refrigerante', 'preco': 5.72},
            {'codigo': 5, 'produto': 'Suco', 'preco': 4.35}]

# http://127.0.0.1:5000/cardapio
@app.route('/cardapio', methods=['GET'])
def consultar_todos_os_itens_do_cardapio():
    # Retornar todos os itens do cardápio em formato JSON
    return jsonify({'cardapio': cardapio})

# http://127.0.0.1:5000/cardapio/1
@app.route('/cardapio/<int:codigo>', methods=['GET'])
def consultar_item_do_cardapio_por_codigo(codigo):
    # Buscar o item do cardápio com o código informado na lista
    item = next((i for i in cardapio if i['codigo'] == codigo), None)
    # Retornar o item do cardápio em formato JSON
    return jsonify({'item': item})

# http://127.0.0.1:5000/cardapio/6/Bolo/15.50
@app.route('/cardapio/<int:codigo>/<string:produto>/<float:preco>', methods=['POST'])
def inserir_item_no_cardapio(codigo, produto, preco):
    # Criar um novo item do cardápio com os valores informados na rota
    item = {'codigo': codigo, 'produto': produto, 'preco': preco}
    # Inserir o novo item do cardápio na lista
    cardapio.append(item)
    # Retornar o item inserido em formato JSON
    return jsonify({'item': item})

# http://127.0.0.1:5000/cardapio/6/Bolo de chocolate/18.00
@app.route('/cardapio/<int:codigo>/<string:produto>/<float:preco>', methods=['PUT'])
def atualizar_item_do_cardapio_totalmente(codigo, produto, preco):
    # Buscar o item do cardápio com o código informado na lista
    item = next((i for i in cardapio if i['codigo'] == codigo), None)
    # Se o item existir, atualizar todos os seus valores com os informados na rota
    if item:
        item['produto'] = produto
        item['preco'] = preco
    # Retornar o item atualizado em formato JSON
    return jsonify({'item': item})

# http://127.0.0.1:5000/cardapio/6/preco/20.00
@app.route('/cardapio/<int:codigo>/<string:campo>/<float:valor>', methods=['PATCH'])
def atualizar_item_do_cardapio_parcialmente(codigo, campo, valor):
    # Buscar o item do cardápio com o código informado na lista
    item = next((i for i in cardapio if i['codigo'] == codigo), None)
    # Se o item existir, atualizar o valor do campo informado na rota
    if item and campo in item:
        item[campo] = valor
    # Retornar o item atualizado em formato JSON
    return jsonify({'item': item})

# http://127.0.0.1:5000/cardapio/6
@app.route('/cardapio/<int:codigo>', methods=['DELETE'])
def remover_item_do_cardapio(codigo):
    # Buscar o item do cardápio com o código informado na lista
    item = next((i for i in cardapio if i['codigo'] == codigo), None)
    # Se o item existir, removê-lo da lista
    if item:
        cardapio.remove(item)
    # Retornar todos os itens do cardápio em formato JSON
    return jsonify({'cardapio': cardapio})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)
