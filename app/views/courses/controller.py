from os import name
from flask.helpers import url_for
from app.views.courses.forms import CourseForm
from flask import render_template, redirect, request, jsonify
from . import course
import app.models.course as models


@course.route("/course")
def index():
    courses = models.Courses.all()
    return render_template(
        "courses.html", courses=courses, title="Home", something="something"
    )


@course.route("/course/delete", methods=["POST"])
def delete_course():
    id = request.form["id"]
    if models.Courses.delete(id):
        return jsonify(success=True, message="Successful")
    else:
        return jsonify(success=False, message="Failed")
