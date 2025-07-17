# models.py
from extensions import db
from datetime import datetime

class Clientes(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    documento_num = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    nombre_empresa = db.Column(db.String(100))
    direccion_empresa = db.Column(db.Text)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)  # Puedes usar default

    def __repr__(self):
        return f'<Clientes {self.nombre}>'  