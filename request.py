from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/new')
def index():
    return "Bem Vindo, aba de teste"

tasks = [
    {
        'idUser': 1,
        'login': 'jonathan@hotmail.com',
        'senha': 123456,
        'nameLoja': 'Store Miame'
    },
    {
        'idUser': 2,
        'login': 'igormail.faustino@gmail.com',
        'senha': 'teste0123456789',
        'nameLoja': 'Store Monster Build'
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)