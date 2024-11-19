from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class CentroTrabajoForm(FlaskForm):
    nombre_centro_trabajo = StringField('Nombre del Centro de Trabajo', validators=[
        DataRequired(), Length(max=128)
    ])
    capacidad_teorica = IntegerField('Capacidad Teórica', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    capacidad_real = IntegerField('Capacidad Real', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    submit = SubmitField('Guardar')
