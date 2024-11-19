from flask import render_template, redirect, url_for, flash, request
from app import db
from app.orden_produccion import bp
from app.orden_produccion.forms import OrdenProduccionForm
from app.orden_produccion.models import OrdenProduccion

@bp.route('/')
def index():
    ordenes = OrdenProduccion.query.all()
    return render_template('orden_produccion/index.html', ordenes=ordenes)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = OrdenProduccionForm()
    if form.validate_on_submit():
        orden = OrdenProduccion(
            producto_asociado=form.producto_asociado.data,
            fecha_inicio_produccion=form.fecha_inicio_produccion.data,
            fecha_fin_produccion=form.fecha_fin_produccion.data,
            cantidad_ordenada=form.cantidad_ordenada.data
        )
        db.session.add(orden)
        db.session.commit()
        flash('Orden de Producción creada con éxito.')
        return redirect(url_for('orden_produccion.index'))
    return render_template('orden_produccion/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    orden = OrdenProduccion.query.get_or_404(id)
    form = OrdenProduccionForm(obj=orden)
    if form.validate_on_submit():
        form.populate_obj(orden)
        db.session.commit()
        flash('Orden de Producción actualizada con éxito.')
        return redirect(url_for('orden_produccion.index'))
    return render_template('orden_produccion/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    orden = OrdenProduccion.query.get_or_404(id)
    db.session.delete(orden)
    db.session.commit()
    flash('Orden de Producción eliminada con éxito.')
    return redirect(url_for('orden_produccion.index'))
