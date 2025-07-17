from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(100), nullable=False)
    nit_cc = db.Column(db.String(50), unique=True, nullable=False)
    nombre_empresa = db.Column(db.String(100))
    direccion_empresa = db.Column(db.String(200))
    telefono = db.Column(db.String(20))
    correo_electronico = db.Column(db.String(100), unique=True)