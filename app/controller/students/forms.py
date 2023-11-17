from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField, FileField


class StudentForm(FlaskForm):
    id = StringField(
        "ID Number",
        [
            validators.DataRequired(),
            validators.Regexp(
                regex=r"^\d{4}-\d{4}$",
                message="ID should be in the format xxxx-xxxx (numbers only).",
            ),
        ],
    )
    photo = FileField("Upload File", validators=[validators.DataRequired()])

    firstname = StringField(
        "First Name",
        [
            validators.DataRequired(),
            validators.Regexp(
                regex=r"^[A-Za-z\s]+$",
                message="Only letters and spaces are allowed in the first name field.",
            ),
        ],
    )
    lastname = StringField(
        "Last Name",
        [
            validators.DataRequired(),
            validators.Regexp(
                regex=r"^[A-Za-z\s]+$",
                message="Only letters and spaces are allowed in the last name field.",
            ),
        ],
    )
    year = SelectField(
        "Year",
        choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
        validators=[validators.DataRequired()],
    )
    gender = SelectField(
        "Gender",
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
        validators=[validators.DataRequired()],
    )
    coursecode = StringField("Course", [validators.DataRequired()])
    submit = SubmitField("Submit")
