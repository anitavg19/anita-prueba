from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange
from app.lugar.models import Lugar

class PersonaForm(FlaskForm):
    numero_identidad = StringField('Número de Identidad', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio")])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email(message="Dirección de correo electrónico inválida")])
    cantidad_mascotas = IntegerField('Cantidad de Mascotas', validators=[DataRequired(), NumberRange(min=0)])
    semana_inicio = StringField('Semana de Inicio', validators=[DataRequired()])
    lugar_id = SelectField('Lugar', coerce=int)
    submit = SubmitField('Guardar')

    def __init__(self):
        super().__init__()
        self.lugar_id.choices = [(lugar.id, lugar.nombre) for lugar in Lugar.query.all()]
