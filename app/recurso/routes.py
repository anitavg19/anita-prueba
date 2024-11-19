from flask import render_template, redirect, url_for, flash, request
from app import db
from app.recurso import bp
from app.recurso.forms import RecursoForm
from app.recurso.models import Recurso

@bp.route('/')
def index():
    recursos = Recurso.query.all()
    return render_template('recurso/index.html', recursos=recursos)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = RecursoForm()
    if form.validate_on_submit():
        recurso = Recurso(
            tipo_recurso=form.tipo_recurso.data,
            disponibilidad=form.disponibilidad.data
        )
        db.session.add(recurso)
        db.session.commit()
        flash('Recurso creado con éxito.')
        return redirect(url_for('recurso.index'))
    return render_template('recurso/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    recurso = Recurso.query.get_or_404(id)
    form = RecursoForm(obj=recurso)
    if form.validate_on_submit():
        form.populate_obj(recurso)
        db.session.commit()
        flash('Recurso actualizado con éxito.')
        return redirect(url_for('recurso.index'))
    return render_template('recurso/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    recurso = Recurso.query.get_or_404(id)
    db.session.delete(recurso)
    db.session.commit()
    flash('Recurso eliminado con éxito.')
    return redirect(url_for('recurso.index'))
