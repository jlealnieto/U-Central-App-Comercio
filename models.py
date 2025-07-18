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
    
class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)
    categoria = db.Column(db.String(50))
    imagen_gui = db.Column(db.Text)

    def __repr__(self):
        return f'<Producto {self.nombre}>'