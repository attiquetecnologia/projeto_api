from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Rodrigo"})

@app.route("/aleatorios", methods=("GET",)) # decorator de rota
def aleatorios(): # função python
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a}) # retorno

@app.route("/argumentos/<string:nome>", methods=("GET",))
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos", methods=("GET",))
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@app.route("/idades", methods=("GET",))
def idades():
    from random_data import pessoas
    import funcoes
    if request.args.get("sexo"):
        idades = funcoes.maior_2000_sexo(pessoas, sexo="Masculino") # retorna profissões
        homens = {"total": idades[0], "%":idades[1]}
        idades = funcoes.maior_2000_sexo(pessoas, sexo="Feminino") # retorna profissões
        mulheres = {"total": idades[0], "%":idades[1]}

        return jsonify({"status": 200, "data": {"homens": homens, "mulheres":mulheres}})
    else:
        num = funcoes.maior_de_50(pessoas)
        return jsonify({"status": 200, "data": num})

@app.route("/salarios", methods=("GET",))
def salarios():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "data": {"registros": num[2], "porcentagem": num[1], "total": num[0]}})

@app.route("/maiores_salarios", methods=("GET", ))
def maiores_salarios():
    from random_data import pessoas
    import funcoes
    pessoa1 = funcoes.maior_salario(pessoas)
    pessoa2 = funcoes.maior_salario(pessoas, float(pessoa1['salario']))
    pessoa3 = funcoes.maior_salario(pessoas, float(pessoa2['salario']))
    return jsonify({"status": 200, "data": {"pessoa1": pessoa1
                                , "pessoa2": pessoa2, "pessoa3": pessoa3}})

@app.route("/profissoes", methods=("GET", ))
def profissoes():
    from random_data import pessoas
    import funcoes
    profissoes = funcoes.media_profissoes(pessoas)
    return jsonify({"status": 200, "data": profissoes})