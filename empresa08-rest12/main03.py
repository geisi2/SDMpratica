# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify

# Criar o objeto Flask app:
app = Flask(__name__)

# Definir os valores das horas normais e extras:
valor_hora_normal = 40
valor_hora_extra = 50

# Definir a taxa de imposto:
taxa_imposto = 0.1

# http://127.0.0.1:5000/salario
@app.route('/salario', methods=['GET'])
def calcular_salario():
    # Obter as horas normais e extras dos headers da requisição:
    horas_normais = int(request.headers.get('horas-normais', '0'))
    horas_extras = int(request.headers.get('horas-extras', '0'))

    # Calcular o salário bruto:
    salario_bruto = horas_normais * valor_hora_normal + horas_extras * valor_hora_extra

    # Calcular o salário líquido:
    salario_liquido = salario_bruto * (1 - taxa_imposto)

    # Retornar os salários em formato JSON:
    return jsonify({'salario_bruto': salario_bruto, 'salario_liquido': salario_liquido})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)
# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify

# Criar o objeto Flask app:
app = Flask(__name__)

# Definir os valores das horas normais e extras:
valor_hora_normal = 40
valor_hora_extra = 50

# Definir a taxa de imposto:
taxa_imposto = 0.1

# http://127.0.0.1:5000/salario
@app.route('/salario', methods=['GET'])
def calcular_salario():
    # Obter as horas normais e extras dos headers da requisição:
    horas_normais = int(request.headers.get('horas_normais'))
    horas_extras = int(request.headers.get('horas_extras'))

    # Calcular o salário bruto e salario liquido :
    salario_bruto = horas_normais * 40 + horas_extras * 50
    salario_liquido = salario_bruto * 0.9


    # Retornar os salários em formato JSON:
    return jsonify({'salario_bruto': salario_bruto, 'salario_liquido': salario_liquido})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)

# http://127.0.0.1:5000/salario?20&6

