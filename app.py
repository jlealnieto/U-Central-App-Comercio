# app.py
from flask import Flask, render_template
from extensions import db
from models import Clientes, Producto
from routes.cliente import init_app as init_cliente
from routes.productos import init_app as init_producto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proyfinal_progcert_user:5jNcji4EdNgyWkNHj2AGRtMQvpXXH6DS@dpg-d1s3132dbo4c73buesn0-a.oregon-postgres.render.com/proyfinal_progcert"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la única instancia de SQLAlchemy
db.init_app(app)

# Registrar Blueprints
init_cliente(app)
init_producto(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)