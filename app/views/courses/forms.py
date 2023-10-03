from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import app.models.course as models


class CourseForm(FlaskForm):
    code = StringField("Code", [validators.DataRequired()])
    name = StringField("Name", [validators.DataRequired()])
    college = StringField("College", [validators.DataRequired()])
    submit = SubmitField("Submit")
