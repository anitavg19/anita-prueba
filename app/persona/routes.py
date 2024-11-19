from sqlite3 import IntegrityError
from flask import render_template, redirect, url_for, flash, request
from app import db
from app.persona import bp
from app.persona.forms import PersonaForm
from app.persona.models import Persona
from app.lugar.models import Lugar

@bp.route('/')
def index():
    personas = Persona.query.all()
    return render_template('persona/index.html', personas=personas)


@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = PersonaForm()
    
    if form.validate_on_submit():
        # Verificar si el número de identidad ya existe en la base de datos
        persona_existente = Persona.query.filter_by(numero_identidad=form.numero_identidad.data).first()
        
        if persona_existente:
            flash('El número de identidad ya existe. Por favor ingresa uno diferente.', 'error')
            return render_template('persona/form.html', form=form)
        
        # Si no existe, proceder a crear la nueva persona
        persona = Persona(
            numero_identidad=form.numero_identidad.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            correo=form.correo.data,
            cantidad_mascotas=form.cantidad_mascotas.data,
            semana_inicio=form.semana_inicio.data,
            lugar_id=form.lugar_id.data
        )
        
        db.session.add(persona)
        db.session.commit()
        flash('Persona creada con éxito.', 'success')
        return redirect(url_for('persona.index'))
    
    return render_template('persona/form.html', form=form)



@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    form = PersonaForm()

    if form.validate_on_submit():
        # Verificar si el número de identidad ya existe en otra persona
        persona_existente = Persona.query.filter_by(numero_identidad=form.numero_identidad.data).filter(Persona.id != id).first()
        
        if persona_existente:
            flash('El número de identidad ya existe. Por favor ingresa uno diferente.', 'error')
            return render_template('persona/form.html', form=form)
        
        # Si el número de identidad no está duplicado, proceder con la actualización
        persona.numero_identidad = form.numero_identidad.data
        persona.nombre = form.nombre.data
        persona.apellidos = form.apellidos.data
        persona.fecha_nacimiento = form.fecha_nacimiento.data
        persona.correo = form.correo.data
        persona.cantidad_mascotas = form.cantidad_mascotas.data
        persona.semana_inicio = form.semana_inicio.data
        persona.lugar_id = form.lugar_id.data
        
        db.session.commit()
        flash('Persona actualizada con éxito.', 'success')
        return redirect(url_for('persona.index'))

    # Pre-popular el formulario con los datos de la persona actual
    form.numero_identidad.data = persona.numero_identidad
    form.nombre.data = persona.nombre
    form.apellidos.data = persona.apellidos
    form.fecha_nacimiento.data = persona.fecha_nacimiento
    form.correo.data = persona.correo
    form.cantidad_mascotas.data = persona.cantidad_mascotas
    form.semana_inicio.data = persona.semana_inicio
    form.lugar_id.data = persona.lugar_id

    return render_template('persona/form.html', form=form)


@bp.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    form = PersonaForm()
    if request.method == 'POST':
        db.session.delete(persona)
        db.session.commit()
        flash('Persona eliminada con éxito.')
        return redirect(url_for('persona.index'))
    return render_template('persona/eliminar.html', persona=persona, form=form)
