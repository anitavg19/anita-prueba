from flask import render_template, redirect, url_for, flash, request
from app import db
from app.carga_trabajo import bp
from app.carga_trabajo.forms import CargaTrabajoForm
from app.carga_trabajo.models import CargaTrabajo

@bp.route('/')
def index():
    cargas = CargaTrabajo.query.all()
    return render_template('carga_trabajo/index.html', cargas=cargas)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = CargaTrabajoForm()
    if form.validate_on_submit():
        carga = CargaTrabajo(
            id_centro_trabajo=form.id_centro_trabajo.data,
            cantidad_horas_requeridas=form.cantidad_horas_requeridas.data,
            disponibilidad_recursos=form.disponibilidad_recursos.data
        )
        db.session.add(carga)
        db.session.commit()
        flash('Carga de Trabajo creada con éxito.')
        return redirect(url_for('carga_trabajo.index'))
    return render_template('carga_trabajo/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    carga = CargaTrabajo.query.get_or_404(id)
    form = CargaTrabajoForm(obj=carga)
    if form.validate_on_submit():
        form.populate_obj(carga)
        db.session.commit()
        flash('Carga de Trabajo actualizada con éxito.')
        return redirect(url_for('carga_trabajo.index'))
    return render_template('carga_trabajo/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    carga = CargaTrabajo.query.get_or_404(id)
    db.session.delete(carga)
    db.session.commit()
    flash('Carga de Trabajo eliminada con éxito.')
    return redirect(url_for('carga_trabajo.index'))
