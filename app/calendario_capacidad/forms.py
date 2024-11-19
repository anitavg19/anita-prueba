from flask_wtf import FlaskForm
from wtforms import FloatField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CalendarioCapacidadForm(FlaskForm):
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[
        DataRequired()
    ])
    horas_laborables = FloatField('Horas Laborables', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    capacidad_restante = FloatField('Capacidad Restante', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    submit = SubmitField('Guardar')
