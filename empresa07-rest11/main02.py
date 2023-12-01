from flask import Flask, jsonify
import math # importa a biblioteca math 

app = Flask(__name__)

# a rota tem que ter os parâmetros de caminho para capturar os valores das coordenadas na rota.Para isso tem que definir uma rota com 
#  /distancia/<float:x1>/<float:y1>/<float:x2>/<float:y2> para receber quatro números reais que representam as coordenadas dos pontos.
#  exemplo :  http://127.0.0.1:5000/distancia/1.0/2.0/3.0/4.0
@app.route('/distancia/<float:x1>/<float:y1>/<float:x2>/<float:y2>', methods=['GET'])
def calcular_distancia(x1, y1, x2, y2):
    # Calcular a distância entre os pontos usando a fórmula
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # Retornar a distância em formato JSON
    return jsonify({'distancia': d})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)
