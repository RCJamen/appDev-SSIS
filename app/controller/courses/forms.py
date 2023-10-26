from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class courseForm(FlaskForm):
    code = StringField(
        "Code",
        [
            validators.DataRequired(),
            validators.Regexp(
                regex=r"^[A-Za-z]+$",
                message="Only letters are allowed in the code field.",
            ),
        ],
    )
    name = StringField(
        "Name",
        [
            validators.DataRequired(),
            validators.Regexp(
                regex=r"^[A-Za-z\s]+$",
                message="Only letters and spaces are allowed in the name field.",
            ),
        ],
    )
    collegecode = StringField("Collegecode", [validators.DataRequired()])
    submit = SubmitField("Submit")
