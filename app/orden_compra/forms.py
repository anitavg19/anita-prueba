from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class OrdenCompraForm(FlaskForm):
    id_proveedor = IntegerField('ID del Proveedor', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    material_solicitado = IntegerField('ID del Material', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    cantidad_ordenada = IntegerField('Cantidad Ordenada', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    fecha_entrega_esperada = DateField('Fecha de Entrega Esperada', format='%Y-%m-%d', validators=[
        DataRequired()
    ])
    submit = SubmitField('Guardar')
