from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#ACA ESTAMOS LIGANDO LA BASE DE DATOS QUE VAMOS A USAR
app.config["SQLACHEMY_DATABASE_URI"] = "sqlite:////C:/Users/1550752/Documents/Python/flask-slqalchemy/youtube.db" 
#app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    pais = db.Column(db.String())

    def __repr__(self): # Esto para convertir el nombre de la bases de datos legible
        return "<Equipo %r>" % self.nombre