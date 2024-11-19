from flask import render_template, redirect, url_for, flash, request
from app import db
from app.inventario import bp
from app.inventario.forms import InventarioForm
from app.inventario.models import Inventario

@bp.route('/')
def index():
    inventarios = Inventario.query.all()
    return render_template('inventario/index.html', inventarios=inventarios)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = InventarioForm()
    if form.validate_on_submit():
        inventario = Inventario(
            id_material=form.id_material.data,
            cantidad_disponible=form.cantidad_disponible.data,
            cantidad_requerida=form.cantidad_requerida.data,
            fecha_reabastecimiento=form.fecha_reabastecimiento.data
        )
        db.session.add(inventario)
        db.session.commit()
        flash('Inventario creado con éxito.')
        return redirect(url_for('inventario.index'))
    return render_template('inventario/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    inventario = Inventario.query.get_or_404(id)
    form = InventarioForm(obj=inventario)
    if form.validate_on_submit():
        form.populate_obj(inventario)
        db.session.commit()
        flash('Inventario actualizado con éxito.')
        return redirect(url_for('inventario.index'))
    return render_template('inventario/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    inventario = Inventario.query.get_or_404(id)
    db.session.delete(inventario)
    db.session.commit()
    flash('Inventario eliminado con éxito.')
    return redirect(url_for('inventario.index'))
