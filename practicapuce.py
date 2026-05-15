from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Prueba Numero 1 Prueba Infraestructura PaaS"

    if __name__ == '__main__':
        app.run()

