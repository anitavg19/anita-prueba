from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class OrdenProduccionForm(FlaskForm):
    producto_asociado = IntegerField('ID del Producto', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    fecha_inicio_produccion = DateField('Fecha de Inicio de Producción', format='%Y-%m-%d', validators=[
        DataRequired()
    ])
    fecha_fin_produccion = DateField('Fecha de Fin de Producción', format='%Y-%m-%d', validators=[
        DataRequired()
    ])
    cantidad_ordenada = IntegerField('Cantidad Ordenada', validators=[
        DataRequired(), NumberRange(min=1)
    ])
    submit = SubmitField('Guardar')
