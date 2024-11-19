from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class CalendarioProduccionForm(FlaskForm):
    semana = StringField('Semana', validators=[DataRequired(), Length(max=20)])
    capacidad_disponible = IntegerField('Capacidad Disponible', validators=[DataRequired(), NumberRange(min=0)])
    produccion_programada = IntegerField('Producción Programada', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Guardar')
