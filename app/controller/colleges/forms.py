from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class collegeForm(FlaskForm):
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
                regex=r"^[A-Za-z]+$",
                message="Only letters are allowed in the name field.",
            ),
        ],
    )
    submit = SubmitField("Submit")
