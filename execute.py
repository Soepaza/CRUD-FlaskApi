from flask import Flask, request, jsonify
print("Novo projeto, copia do pinterest usando Flask.")

# definir aplicacao
myApp = Flask(__name__)

# ter um banco de dados para testar (vou criar um dic)
alunos = [
    {"nome": "soe", "id": 12, "cidade": "SP"},
    {"nome": "carboni", "id": 10, "cidade": "RJ"},
    {"nome": "schautz", "id": 20, "cidade": "ES"},
]

# definir rota


@myApp.route("/alunos", methods=['GET'])
def get_aluno():
    return jsonify(alunos)


@myApp.route("/alunos/<int:id_aluno>", methods=['GET'])
def get_estudante(id_aluno):
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
        



@myApp.route("/alunos/<int:id_aluno>", methods=['DELETE'])
def delete_aluno(id_aluno):
    for jovem in alunos:
        if jovem['id'] == id_aluno:
            alunos.remove(jovem)
        return "Aluno deletado com sucesso.", 200
    return "Aluno nao encontrado.", 404


if (__name__) == "__main__":
    myApp.run(debug=True)
