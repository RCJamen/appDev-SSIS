from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import app.models.course as models


class courseForm(FlaskForm):
    code = StringField("Code", [validators.DataRequired()])
    name = StringField("Name", [validators.DataRequired()])
    collegecode = StringField("Collegecode", [validators.DataRequired()])
    submit = SubmitField("Submit")
