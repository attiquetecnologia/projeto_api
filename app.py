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
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "data": num})

@app.route("/salarios", methods=("GET",))
def salarios():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "data": {"registros": num[2], "porcentagem": num[1], "total": num[0]}})