from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import app.models.student as models


class StudentForm(FlaskForm):
    id = StringField("ID Number", [validators.DataRequired()])
    firstname = StringField("First Name", [validators.DataRequired()])
    lastname = StringField("Last Name", [validators.DataRequired()])
    coursecode = StringField("Course", [validators.DataRequired()])
    year = SelectField(
        "Year",
        choices=[
            ("1st Year", "1st Year"),
            ("2nd Year", "2nd Year"),
            ("3rd Year", "3rd Year"),
            ("4th Year", "4th Year"),
        ],
    )
    gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female")])
    submit = SubmitField("Submit")
