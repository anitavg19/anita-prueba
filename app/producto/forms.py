from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ProductoForm(FlaskForm):
    nombre_producto = StringField('Nombre del Producto', validators=[
        DataRequired(), Length(max=128)
    ])
    demanda_planeada = IntegerField('Demanda Planeada', validators=[
        NumberRange(min=0)
    ])
    fecha_entrega = DateField('Fecha de Entrega', format='%Y-%m-%d', validators=[
        DataRequired()
    ])
    cantidad_producir = IntegerField('Cantidad a Producir', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    submit = SubmitField('Guardar')
