from os import name
from flask.helpers import url_for
from app.views.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify
from . import student
import app.models.student as models


@student.route("/")
@student.route("/student")
def index():
    students = models.Students.all()
    return render_template(
        "students.html", students=students, title="Home", something="something"
    )


@student.route("/student/delete", methods=["POST"])
def delete_student():
    id = request.form["id"]
    if models.Students.delete(id):
        return jsonify(success=True, message="Successful")
    else:
        return jsonify(success=False, message="Failed")
