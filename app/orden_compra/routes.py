from flask import render_template, redirect, url_for, flash, request
from app import db
from app.orden_compra import bp
from app.orden_compra.forms import OrdenCompraForm
from app.orden_compra.models import OrdenCompra

@bp.route('/')
def index():
    ordenes = OrdenCompra.query.all()
    return render_template('orden_compra/index.html', ordenes=ordenes)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = OrdenCompraForm()
    if form.validate_on_submit():
        orden = OrdenCompra(
            id_proveedor=form.id_proveedor.data,
            material_solicitado=form.material_solicitado.data,
            cantidad_ordenada=form.cantidad_ordenada.data,
            fecha_entrega_esperada=form.fecha_entrega_esperada.data
        )
        db.session.add(orden)
        db.session.commit()
        flash('Orden de Compra creada con éxito.')
        return redirect(url_for('orden_compra.index'))
    return render_template('orden_compra/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    orden = OrdenCompra.query.get_or_404(id)
    form = OrdenCompraForm(obj=orden)
    if form.validate_on_submit():
        form.populate_obj(orden)
        db.session.commit()
        flash('Orden de Compra actualizada con éxito.')
        return redirect(url_for('orden_compra.index'))
    return render_template('orden_compra/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    orden = OrdenCompra.query.get_or_404(id)
    db.session.delete(orden)
    db.session.commit()
    flash('Orden de Compra eliminada con éxito.')
    return redirect(url_for('orden_compra.index'))
