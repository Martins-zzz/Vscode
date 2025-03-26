# Este projeto foi feito para ter um entendimento básico sobre o framework Flask
# O aplicativo é bruto e crude devido ao quão basico o html é, o ponto do projeto foi aprender as funcionalidades do Flask
# Comando principal 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from view import *


if __name__ == '__main__': 
    with app.app_context():
        db.create_all()
    app.run()