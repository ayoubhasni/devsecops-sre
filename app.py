from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return "OK"

@app.route('/health')
def health():
    return jsonify(status='healthy')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id_counter
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': task_id_counter,
        'title': data['title'],
        'description': data.get('description', ''),
        'done': False
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_done(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) == len(tasks):
        return jsonify({'error': 'Task not found'}), 404
    tasks = updated_tasks
    return jsonify({'result': 'Task deleted'})

@app.route('/error')
def trigger_error():
    # Simule une erreur pour tester la détection d'incidents
    return 1 / 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
