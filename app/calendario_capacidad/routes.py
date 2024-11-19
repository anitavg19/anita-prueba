from flask import render_template, redirect, url_for, flash, request
from app import db
from app.calendario_capacidad import bp
from app.calendario_capacidad.forms import CalendarioCapacidadForm
from app.calendario_capacidad.models import CalendarioCapacidad

@bp.route('/')
def index():
    calendarios = CalendarioCapacidad.query.all()
    return render_template('calendario_capacidad/index.html', calendarios=calendarios)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = CalendarioCapacidadForm()
    if form.validate_on_submit():
        calendario = CalendarioCapacidad(
            fecha=form.fecha.data,
            horas_laborables=form.horas_laborables.data,
            capacidad_restante=form.capacidad_restante.data
        )
        db.session.add(calendario)
        db.session.commit()
        flash('Calendario de Capacidad creado con éxito.')
        return redirect(url_for('calendario_capacidad.index'))
    return render_template('calendario_capacidad/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    calendario = CalendarioCapacidad.query.get_or_404(id)
    form = CalendarioCapacidadForm(obj=calendario)
    if form.validate_on_submit():
        form.populate_obj(calendario)
        db.session.commit()
        flash('Calendario de Capacidad actualizado con éxito.')
        return redirect(url_for('calendario_capacidad.index'))
    return render_template('calendario_capacidad/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    calendario = CalendarioCapacidad.query.get_or_404(id)
    db.session.delete(calendario)
    db.session.commit()
    flash('Calendario de Capacidad eliminado con éxito.')
    return redirect(url_for('calendario_capacidad.index'))
