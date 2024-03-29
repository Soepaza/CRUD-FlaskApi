from flask import Flask, request, jsonify

# definir aplicacao
myApp = Flask(__name__)

# ter um banco de dados para testar (vou criar um dic)
alunos = [
    {"nome": "ribeiro", "id": 1, "cidade": "SP"},
    {"nome": "fernandes", "id": 2, "cidade": "RJ"},
    {"nome": "matos", "id": 3, "cidade": "ES"},
]


# definir rota
@myApp.route("/alunos", methods=['GET'])
def get_aluno():
    return jsonify(alunos)

# Rota para obter específico por ID


@myApp.route("/alunos/<int:id_aluno>", methods=['GET'])
def get_estudante(id_aluno):
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return jsonify({'mensagem': 'Aluno não encontrado.'}), 404

# Rota para criar um novo aluno
@myApp.route("/alunos", methods=['POST'])
def create_aluno():
    dados = request.json
    if 'nome' not in dados or 'cidade' not in dados:
        return jsonify({'mensagem': 'Nome e cidade são campos obrigatórios.'}), 400
    novo_aluno = {
        "nome": dados.get('nome'),
        "id": len(alunos) + 1,
        "cidade": dados.get('cidade')
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

# Rota para atualizar os dados de um aluno existente
@myApp.route("/alunos/<int:id_aluno>", methods=['PUT'])
def atualizar_aluno(id_aluno):
    dados = request.json
    for i in alunos:
        if i['id'] == id_aluno:
            i['nome'] = dados.get('nome', i['nome'])
            i['cidade'] = dados.get('cidade', i['cidade'])
            return jsonify(i), 200
    return jsonify({'mensagem': 'Aluno nao encontrado.'})

# Rota para deletar um aluno por ID
@myApp.route("/alunos/<int:id_aluno>", methods=['DELETE'])
def delete_aluno(id_aluno):
    for jovem in alunos:
        if jovem['id'] == id_aluno:
            alunos.remove(jovem)
        return "Aluno deletado com sucesso.", 200
    return "Aluno nao encontrado.", 404


# Executar
if (__name__) == "__main__":
    myApp.run(debug=True)


#iniciar meu projeto do pinterest