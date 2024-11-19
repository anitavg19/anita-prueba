from flask import render_template, redirect, url_for, flash, request
from app import db
from app.centro_trabajo import bp
from app.centro_trabajo.forms import CentroTrabajoForm
from app.centro_trabajo.models import CentroTrabajo

@bp.route('/')
def index():
    centros = CentroTrabajo.query.all()
    return render_template('centro_trabajo/index.html', centros=centros)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = CentroTrabajoForm()
    if form.validate_on_submit():
        centro = CentroTrabajo(
            nombre_centro_trabajo=form.nombre_centro_trabajo.data,
            capacidad_teorica=form.capacidad_teorica.data,
            capacidad_real=form.capacidad_real.data
        )
        db.session.add(centro)
        db.session.commit()
        flash('Centro de Trabajo creado con éxito.')
        return redirect(url_for('centro_trabajo.index'))
    return render_template('centro_trabajo/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    centro = CentroTrabajo.query.get_or_404(id)
    form = CentroTrabajoForm(obj=centro)
    if form.validate_on_submit():
        form.populate_obj(centro)
        db.session.commit()
        flash('Centro de Trabajo actualizado con éxito.')
        return redirect(url_for('centro_trabajo.index'))
    return render_template('centro_trabajo/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    centro = CentroTrabajo.query.get_or_404(id)
    db.session.delete(centro)
    db.session.commit()
    flash('Centro de Trabajo eliminado con éxito.')
    return redirect(url_for('centro_trabajo.index'))
