from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class RecursoForm(FlaskForm):
    tipo_recurso = StringField('Tipo de Recurso', validators=[
        DataRequired(), Length(max=128)
    ])
    disponibilidad = IntegerField('Disponibilidad', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    submit = SubmitField('Guardar')
