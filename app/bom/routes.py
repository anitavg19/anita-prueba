from flask import render_template, redirect, url_for, flash, request
from app import db
from app.bom import bp
from app.bom.forms import BOMForm
from app.bom.models import BOM

@bp.route('/')
def index():
    boms = BOM.query.all()
    return render_template('bom/index.html', boms=boms)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = BOMForm()
    if form.validate_on_submit():
        bom = BOM(
            id_producto=form.id_producto.data,
            id_material=form.id_material.data,
            cantidad_por_producto=form.cantidad_por_producto.data
        )
        db.session.add(bom)
        db.session.commit()
        flash('Lista de Materiales creada con éxito.')
        return redirect(url_for('bom.index'))
    return render_template('bom/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    bom = BOM.query.get_or_404(id)
    form = BOMForm(obj=bom)
    if form.validate_on_submit():
        form.populate_obj(bom)
        db.session.commit()
        flash('Lista de Materiales actualizada con éxito.')
        return redirect(url_for('bom.index'))
    return render_template('bom/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    bom = BOM.query.get_or_404(id)
    db.session.delete(bom)
    db.session.commit()
    flash('Lista de Materiales eliminada con éxito.')
    return redirect(url_for('bom.index'))
