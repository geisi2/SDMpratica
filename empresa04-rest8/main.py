from flask import Flask, request  # Importar a classe Flask e o objeto request

app = Flask(__name__)  # Criação do objeto (instancia) Flask que atribui o valor da variavel app, usado para determinar o caminho dos arquivos  estaticos e dos templetes.ou seja, a variavel é objeto que representa a aplicaçao web que sera usado para definir as rotas e as funções de visualização.

# http://127.0.0.1:5000/testes/1?linguagem=Python
@app.route('/testes/1') #  primeira rota, usa-se um decorador que associa uma URL com uma função, que é responsavel por processar a requisição e retornar uma resposta  
def teste_query_string_1_agurmento_get(): #  inicializando a função quando é dada a rota /testes/1
    # query string é a parte da url que vem depois da ? que contem pares de chaves e valor separados por um &, usados para enviar informações adicionais ao servidor, como filtros, nessse  caso não temos o & porque eles são usados  quando se tem que enviar 2 parametros ou mais 
    linguagem = request.args.get('linguagem') # a variavel linguagem recebe a requisição get como argumento e aplica a funçao dada ao digitar a rota
    return '''<h1>Linguagem informada: {}</h1>'''.format(linguagem) # Vai retornar a mensagem mais a linguagem informada na requisição 

# http://127.0.0.1:5000/testes/2?linguagem=Python&framework=Flask
@app.route('/testes/2') #  segunda rota,  que tambem usa-se um decorador que associa uma URL com uma função, é responsavel por processar a requisição e retornar uma resposta  
def teste_query_string_2_agurmentos_get():  #  inicializando a função quando é dada a rota:  /testes/2  
    # query string parte da url que vem depois da ?,  usados para enviar informações adicionais ao servidor, como filtros, nessse caso já temos o & porque  tem que enviar 2 parametros no caso da linguagem e o framework 
    # tanto a variavel linguagem quanto a framework recebem a requisição get digitada como argumento e aplica a funçao dada ao digitar a rota
    linguagem = request.args.get('linguagem') 
    framework = request.args.get('framework')
    # Retorna a mensagem da função mais a linguagem e o framework informados na requisição 
    return '''<h1>Linguagem informada: {}</h1>
              <h1>Framework informado: {}</h1>'''.format(linguagem, framework)

# http://127.0.0.1:5000/testes/3?linguagem=Python&framework=Flask
@app.route('/testes/3') #  terceira rota, usa-se um decorador que associa  a uma URL com a função, responsavel por processar a requisição e retornar uma resposta  
def teste_query_string_2_agurmentos_vetor(): # inicia-se a função dada a rota: /testes/3; onde recebe como argumento o objeto request, que representa a requisição feita pelo usuario. Esse objeto contem varios atributos e metodos que permitem acessar as informações da requisição , como os parametros, os cabeçalhos, os cookies e o corpo. 
    linguagem = request.args['linguagem']  # usa-se o atributo args do request para acessar os parametros da query string. Esse atributo é um dicionario imutavél que contém as chaves e os varalores dos parametros. Ele usa o metodo get desse dicionario para obter o valor do parametro linguagem e atribui à variavel linguagem. Se o parametro não existir, o metodo get retorna NONE.  
    framework = request.args['framework'] # usa-se o metodo get do dicionario para obter o valor do parametro framework e atribiu à variavel framework. Se o parametro nao existir, o metodo get retorna NONE 
    # ele retorna uma string formatada com as variaveis linguagem e framework, usando a letra f antes das aspas para indicar que é uma string interpolada. Essa string será o conteudo da resposta http que será enviada ao usuario. Ele usa a tag html <h1> para indicar que é um titulo de nivel 1 e aumentar o tamanho da fonte 
    return '''<h1>Linguagem informada: {}</h1>
              <h1>Framework informado: {}</h1>'''.format(linguagem, framework)

if __name__ == '__main__': # verifica se o módulo atual é o principal, evitando que o código seja executado quando o módulo for importado por outro módulo.

    app.run(debug = True, port = 5000)
# Executar app no modo debug (default) na porta 5000 (default):
