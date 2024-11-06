from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Todo
from config import Config


from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Todo.db'
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    new_todo = Todo(task=data['title'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    todo = Todo.query.get_or_404(id)
    todo.task = data['title']
    # todo.completed = data['completed']
    db.session.commit()
    return jsonify(todo.to_dict())

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
