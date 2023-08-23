from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired


class calcForm(FlaskForm):
    number1 = DecimalField("first number", validators = [DataRequired(), ])
    number2 = DecimalField("second number", validators = [DataRequired(), ])
    submit = SubmitField('Calculate')