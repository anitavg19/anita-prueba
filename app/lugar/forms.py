from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LugarForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    codigo_postal = StringField('Código Postal', validators=[DataRequired()])
    submit = SubmitField('Guardar')