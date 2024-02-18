from flask import Flask, jsonify
# Crear una aplicación Flask
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['GET'])
def index():
    # Lógica para manejar la solicitud GET a la ruta raíz
    data = {'message': 'Hello, World!'}
    return jsonify(data)
