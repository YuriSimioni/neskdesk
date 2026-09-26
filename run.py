# Importando bibliotecas
from app import create_app
from flask import Flask


if __name__ == "__main__":
    
    # Criando a aplicação
    app: Flask = create_app()
    
    # Iniciando a aplicação
    app.run(port=3333)