from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)

uri = '/api/'
persona = {'name':'Rafael', 'matricula': '123456'}

tasks = [
    {
        'id': 1,
        'name': 'Cocinar algo bien sabroso',
        'status': False
    },
    {
        'id': 2,
        'name': 'Limpiar la casa',
        'status': False
    },
]

@app.route("/")
def hello_world():
    return render_template('index.html', data=persona)

#API

@app.route(uri+'/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route(uri+'/tasks/<int:id>', methods=['GET'])
def get_task(id):
    this_task = 0
    for task in tasks:
        if task['id'] == id:
            this_task = task
    if this_task == 0:
        abort(404)
    return jsonify({'task': this_task})
