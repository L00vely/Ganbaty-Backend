from flask import Flask, jsonify
from association_rules import association_rules
from decision_trees import decision_trees
from flask_cors import CORS

# Crear una aplicación Flask
app = Flask(__name__)
CORS(app)

app.register_blueprint(association_rules, url_prefix='/association_rules')
app.register_blueprint(decision_trees, url_prefix='/decision_trees')


@app.route('/', methods=['GET'])
def index():
    # Lógica para manejar la solicitud GET a la ruta raíz
    data = {'message': 'Hello, World!', 'ok': "true"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
