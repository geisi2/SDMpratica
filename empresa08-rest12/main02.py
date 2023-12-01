# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify

# Criar o objeto Flask app:
app = Flask(__name__)

# Definir os preços das camisetas por tamanho:
precos = {'pequena': 10, 'media': 12, 'grande': 15}

# http://127.0.0.1:5000/venda
@app.route('/venda', methods=['GET'])
def calcular_valor_venda():
    # Obter as quantidades de camisetas por tamanho dos headers da requisição:
    qtd_pequena = int(request.headers.get('X-qtd-pequena', 0))
    qtd_media = int(request.headers.get('X-qtd-media', 0))
    qtd_grande = int(request.headers.get('X-qtd-grande', 0))

    # Calcular o valor total da venda:
    valor_total = qtd_pequena * precos['pequena'] + qtd_media * precos['media'] + qtd_grande * precos['grande']

    # Retornar o valor total em formato JSON:
    return jsonify({'valor_total': valor_total})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)
