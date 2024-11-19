from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class BOMForm(FlaskForm):
    id_producto = IntegerField('ID del Producto', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    id_material = IntegerField('ID del Material', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    cantidad_por_producto = IntegerField('Cantidad por Producto', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    submit = SubmitField('Guardar')
