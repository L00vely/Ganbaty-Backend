from flask import Flask, jsonify
# Crear una aplicación Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Lógica para manejar la solicitud GET a la ruta raíz
    # data = {'message': 'Hello, World!'}
    # return jsonify(data)
    return "Hello, I'm ready to help"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
