from flask import Flask, jsonify  # importando a classe Flask(classe que representa a aplicação web) e a classe jonify (função que converte dados em python em json)

app = Flask (__name__) # criando uma instancia da classe Flask, e passando o nome do modulo atual como argumento, permitindo que o Flask saiba onde encontrar os recursos da aplicação 

@app.route ("/testes/1") # definindo uma rota padrão, já que não tem nenhuma metodo especificado, o flask assume o metodo GET implicito 
def teste_GET_implicito ():  # Define uma função que quando chamada pelo flask é acessada pela requisição http retonando o conteudo que será exibido na tela 
    return jsonify ({"resp": "Teste 1: metodo GET implicito."})
            # o flask usa o jsonify para converter o objeto em python para json

@app.route ("/testes/2", methods=['GET']) # define uma segunda rota, ou contrario da rota de cima essa define explicitamente que só aceita o metodo GET
def teste_GET_explicito (): # Define uma função que retona o conteudo que será exibido na tela 
    return jsonify ({"resp": "Teste 2: metodo GET explicito."}) # retorna uma resposta em json para a requisição HTTP com o metodo GET quando o usuário acessar a rota. Pode ate tentar acessa-la com outro metodo, como o post, mas receberá um errro 405 Method Not Allowed.  

@app.route ("/testes/3", methods=['POST'])  # define uma terceira rota, essa define explicitamente que só aceita o metodo POST, ou seja, o metodo usado para enviar dados para o servidor , como um formulario ou um arquivo  
def teste_POST ():  # Define uma função que retona o conteudo que será exibido na tela 
    return jsonify ({"resp": "Teste 3: metodo POST."})  # retorna uma resposta em json para a requisição HTTP com o metodo POST . Pode ate tentar acessa-la com outro metodo, como o get, mas receberá um errro 405 Method Not Allowed.  


@app.route ("/testes/4", methods=['GET', 'POST'])  # define uma quarta rota, essa define explicitamente que aceita o metodo GET e o POST
def teste_GET_POST ():  # Define uma função que retona o conteudo que será exibido na tela 
    return jsonify ({"resp": "Teste 4: metodo GET ou POST."}) # resposta que mostra que essa rota pode ser acessada por qualquer um dos metodos usados 

if __name__ == "__main__":  # verifica se o módulo atual é o principal, evitando que o código seja executado quando o módulo for importado por outro módulo.
    app.run () # iniciando o servidor de desenvolvimento do Flask , que permite testar a aplicação web localmente, fazendo com que a aplicação fique disponível na porta 5000 do seu computador. além de  regarregar o codigo automaticamente quando ha alguma alteração e mostrar mensagens de erro detalhadas 