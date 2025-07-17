# routes/cliente.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import Clientes, db

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/registrar_cliente', methods=['GET', 'POST'])
def registrar_cliente():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre']
        nit_cc = request.form['documento_num']
        nombre_empresa = request.form.get('nombre_empresa', '')
        direccion_empresa = request.form['direccion_empresa']
        telefono = request.form['telefono']
        correo_electronico = request.form['email']

        nuevo_cliente = Clientes(
    nombre=nombre_cliente,  
    documento_num=nit_cc,
    nombre_empresa=nombre_empresa,
    direccion_empresa=direccion_empresa,
    telefono=telefono,
    email=correo_electronico,
)
        db.session.add(nuevo_cliente)
        db.session.commit()

        return redirect(url_for('cliente.lista_clientes'))

    return render_template('registrar_cliente.html')

@cliente_bp.route('/clientes')
@cliente_bp.route('/clientes/')
def lista_clientes():
    clientes = Clientes.query.all()
    return render_template('cliente.html', clientes=clientes)

@cliente_bp.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Clientes.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.documento_num = request.form['documento_num']
        cliente.nombre_empresa = request.form.get('nombre_empresa', '')
        cliente.direccion_empresa = request.form['direccion_empresa']
        cliente.telefono = request.form['telefono']
        cliente.email = request.form['email']

        db.session.commit()
        return redirect(url_for('cliente.lista_clientes'))

    return render_template('editar_cliente.html', cliente=cliente)

@cliente_bp.route('/eliminar_cliente/<int:id>', methods=['POST'])
def eliminar_cliente(id):
    cliente = Clientes.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cliente.lista_clientes'))

def init_app(app):
    app.register_blueprint(cliente_bp)