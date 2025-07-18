# routes/producto.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import Producto, db

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/registrar_producto', methods=['GET', 'POST'])
def registrar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form.get('descripcion', '')
        precio = request.form['precio']
        stock = request.form['stock']
        categoria = request.form.get('categoria', '')
        imagen_gui = request.form.get('imagen_gui', '')

        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            imagen_gui=imagen_gui
        )

        db.session.add(nuevo_producto)
        db.session.commit()

        return redirect(url_for('producto.lista_productos'))

    return render_template('registrar_producto.html')

@producto_bp.route('/productos')
def lista_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@producto_bp.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form.get('descripcion', '')
        producto.precio = request.form['precio']
        producto.stock = request.form['stock']
        producto.categoria = request.form.get('categoria', '')
        producto.imagen_gui = request.form.get('imagen_gui', '')

        db.session.commit()
        return redirect(url_for('producto.lista_productos'))

    return render_template('editar_producto.html', producto=producto)

@producto_bp.route('/eliminar_producto/<int:id>', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('producto.lista_productos'))

def init_app(app):
    app.register_blueprint(producto_bp)