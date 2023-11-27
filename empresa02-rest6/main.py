from flask import Flask, jsonify # importando a classe Flask(classe que representa a aplicação web) e a classe jonify (função que converte dados em python em json)
app = Flask (__name__)  # criando uma instancia da classe Flask, e passando o nome do modulo atual como argumento, permitindo que o Flask saiba onde encontrar os recursos da aplicação 

@app.route('/') # definindo uma rota
def cumprimentar(): # Definindo uma função que retona o conteudo que será exibido na tela 
        return jsonify({"resp": "Ola, Mundo!"}) # resposta em json que será retornada quando o usuário acessar a rota

if  __name__ ==  "__main__" : # verifica se o módulo atual é o principal, evitando que o código seja executado quando o módulo for importado por outro módulo.
    app.run() # iniciando o servidor de desenvolvimento do Flask , que permite testar a aplicação web localmente , fazendo com que a aplicação fique disponível na porta 5000 do seu computador