from flask import Flask, render_template, request, redirect, url_for
from models import Cliente, db

@app.route('/clientes')
def lista_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@app.route('/registrar_cliente', methods=['GET', 'POST'])
def registrar_cliente():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        nit_cc = request.form['nit_cc']
        nombre_empresa = request.form.get('nombre_empresa', '')  # opcional
        direccion_empresa = request.form['direccion_empresa']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']

        nuevo_cliente = Cliente(
            nombre_cliente=nombre_cliente,
            nit_cc=nit_cc,
            nombre_empresa=nombre_empresa,
            direccion_empresa=direccion_empresa,
            telefono=telefono,
            correo_electronico=correo_electronico
        )

        db.session.add(nuevo_cliente)
        db.session.commit()

        return redirect(url_for('lista_clientes'))

    return render_template('registrar_cliente.html')