from flask import render_template, redirect, url_for, flash, request
from app import db
from app.producto import bp
from app.producto.forms import ProductoForm
from app.producto.models import Producto

@bp.route('/')
def index():
    productos = Producto.query.all()
    return render_template('producto/index.html', productos=productos)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = ProductoForm()
    if form.validate_on_submit():
        producto = Producto(
            nombre_producto=form.nombre_producto.data,
            demanda_planeada=form.demanda_planeada.data,
            fecha_entrega=form.fecha_entrega.data,
            cantidad_producir=form.cantidad_producir.data
        )
        db.session.add(producto)
        db.session.commit()
        flash('Producto creado con éxito.')
        return redirect(url_for('producto.index'))
    return render_template('producto/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Producto.query.get_or_404(id)
    form = ProductoForm(obj=producto)
    if form.validate_on_submit():
        form.populate_obj(producto)
        db.session.commit()
        flash('Producto actualizado con éxito.')
        return redirect(url_for('producto.index'))
    return render_template('producto/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado con éxito.')
    return redirect(url_for('producto.index'))
