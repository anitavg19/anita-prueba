from flask import render_template, redirect, url_for, flash, request
from app import db
from app.material import bp
from app.material.forms import MaterialForm
from app.material.models import Material

@bp.route('/')
def index():
    materiales = Material.query.all()
    return render_template('material/index.html', materiales=materiales)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = MaterialForm()
    if form.validate_on_submit():
        material = Material(
            nombre_material=form.nombre_material.data,
            cantidad_necesaria=form.cantidad_necesaria.data,
            tiempo_entrega=form.tiempo_entrega.data
        )
        db.session.add(material)
        db.session.commit()
        flash('Material creado con éxito.')
        return redirect(url_for('material.index'))
    return render_template('material/form.html', form=form)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    material = Material.query.get_or_404(id)
    form = MaterialForm(obj=material)
    if form.validate_on_submit():
        form.populate_obj(material)
        db.session.commit()
        flash('Material actualizado con éxito.')
        return redirect(url_for('material.index'))
    return render_template('material/form.html', form=form)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    material = Material.query.get_or_404(id)
    db.session.delete(material)
    db.session.commit()
    flash('Material eliminado con éxito.')
    return redirect(url_for('material.index'))
