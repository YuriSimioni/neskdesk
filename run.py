# Importando bibliotecas
from app import create_app
from flask import Flask
from app.core.config import Config

if __name__ == "__main__":
    
    # Criando a aplicação
    app: Flask = create_app()
    
    # Iniciando a aplicação
    app.run(port=Config.FLASK_PORT, host=Config.FLASK_HOST, debug=Config.FLASK_DEBUG)