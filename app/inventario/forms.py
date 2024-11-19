from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class InventarioForm(FlaskForm):
    id_material = IntegerField('ID del Material', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    cantidad_disponible = IntegerField('Cantidad Disponible', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    cantidad_requerida = IntegerField('Cantidad Requerida', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    fecha_reabastecimiento = DateField('Fecha de Reabastecimiento', format='%Y-%m-%d', validators=[
        DataRequired()
    ])
    submit = SubmitField('Guardar')
