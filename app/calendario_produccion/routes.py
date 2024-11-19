from flask import render_template, redirect, url_for, flash, request
from app import db
from app.calendario_produccion import bp
from app.calendario_produccion.forms import CalendarioProduccionForm
from app.calendario_produccion.models import CalendarioDeProduccion

@bp.route('/')
def index():
    calendarios = CalendarioDeProduccion.query.all()
    return render_template('calendario_produccion/index.html', calendarios=calendarios)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = CalendarioProduccionForm()
    if form.validate_on_submit():
        calendario = CalendarioDeProduccion(
            semana=form.semana.data,
            capacidad_disponible=form.capacidad_disponible.data,
            produccion_programada=form.produccion_programada.data
        )
        db.session.add(calendario)
        db.session.commit()
        flash('Calendario de producción creado con éxito.')
        return redirect(url_for('calendario_produccion.index'))
    return render_template('calendario_produccion/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    calendario = CalendarioDeProduccion.query.get_or_404(id)
    form = CalendarioProduccionForm(obj=calendario)
    if form.validate_on_submit():
        form.populate_obj(calendario)
        db.session.commit()
        flash('Calendario actualizado con éxito.')
        return redirect(url_for('calendario_produccion.index'))
    return render_template('calendario_produccion/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    calendario = CalendarioDeProduccion.query.get_or_404(id)
    db.session.delete(calendario)
    db.session.commit()
    flash('Calendario de producción eliminado con éxito.')
    return redirect(url_for('calendario_produccion.index'))
