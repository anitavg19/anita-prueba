from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CargaTrabajoForm(FlaskForm):
    id_centro_trabajo = IntegerField('ID del Centro de Trabajo', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    cantidad_horas_requeridas = FloatField('Cantidad de Horas Requeridas', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    disponibilidad_recursos = IntegerField('Disponibilidad de Recursos', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    submit = SubmitField('Guardar')
