from os import name
from flask.helpers import url_for
from app.views.courses.forms import courseForm
from flask import render_template, redirect, request, jsonify
from . import course
import app.models.course as courseModel
import app.models.college as collegeModel


@course.route("/course")
def index():
    courses = courseModel.Courses.all()
    return render_template("courses.html", courses=courses)


@course.route("/course/delete", methods=["POST"])
def delete_course():
    code = request.form["code"]
    if courseModel.Courses.delete(code):
        return jsonify(success=True, message="Successfully deleted Course")
    else:
        return jsonify(success=False, message="Failed to Delete Course")


@course.route("/course/add", methods=["POST", "GET"])
def add_course():
    form = courseForm(request.form)
    if request.method == "POST" and form.validate():
        course = courseModel.Courses(
            code=form.code.data, name=form.name.data, collegecode=form.collegecode.data
        )
        course.add()
        return redirect("/course")
    else:
        colleges = collegeModel.Colleges.refer()
        return render_template("courses.html", form=form, data=colleges)
