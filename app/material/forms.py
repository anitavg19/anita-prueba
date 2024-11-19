from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class MaterialForm(FlaskForm):
    nombre_material = StringField('Nombre del Material', validators=[
        DataRequired(), Length(max=128)
    ])
    cantidad_necesaria = IntegerField('Cantidad Necesaria', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    tiempo_entrega = IntegerField('Tiempo de Entrega (días)', validators=[
        DataRequired(), NumberRange(min=0)
    ])
    submit = SubmitField('Guardar')
