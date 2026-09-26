# Importando bibliotecas necessarias
from flask import Flask
from app.core.config import Config

# Criando a aplicação
def create_app(environment: str = "development"):
    
    # Criando a aplicação
    app: Flask = Flask(__name__)
    
    # Getting environment variables
    app.config.from_object(Config)
    
    # Criando as rotas
    @app.route("/")
    def hello_world() -> str:
        return "<h1>Hello, World!</h1>"
    
    # Retornando a aplicação
    return app