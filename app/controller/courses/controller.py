from os import name
from flask.helpers import url_for
from app.controller.courses.forms import courseForm
from flask import render_template, redirect, request, jsonify, flash
from . import course
import app.models.course as courseModel
import app.models.college as collegeModel


@course.route("/course")
def index():
    courses = courseModel.Courses.all()
    collegecode = collegeModel.Colleges.refer()
    return render_template("courses.html", courses=courses, colleges=collegecode)


@course.route("/course/delete", methods=["POST"])
def delete_course():
    course_code = request.form["code"]
    if courseModel.Courses.delete(course_code):
        return jsonify(success=True, message="Successfully deleted Course!")
    else:
        return jsonify(
            success=False,
            message="Failed to Delete Course, Data was Referenced in Students!",
        )


@course.route("/course/add", methods=["POST", "GET"])
def add_course():
    form = courseForm(request.form)
    if request.method == "POST" and form.validate():
        course = courseModel.Courses(
            code=form.code.data, name=form.name.data, collegecode=form.collegecode.data
        )
        existing_course = courseModel.Courses.exists(form.code.data)
        if existing_course:
            flash("Error: Course with the same CODE already exists.", "danger")
            return redirect(url_for(".index"))
        
        course.add()
        flash("Course added successfully!", "success")
        return redirect(url_for(".index"))
    else:
        flash("Error: Please check the form for validation errors.", "danger")
        return redirect(url_for(".index"))


@course.route("/course/update", methods=["POST"])
def update_course():
    if request.method == "POST":
        code = request.form["code"]
        name = request.form["name"]
        collegecode = request.form["collegecode"]
        try:
            courseModel.Courses.update(code, name, collegecode)
            return redirect(url_for(".index"))
        except Exception as e:
            return f"Error updating college: {str(e)}"


@course.route("/course/search", methods=["GET", "POST"])
def search_course():
    info = request.form.get("information")
    if info is None or info.strip() == "":
        return redirect(url_for(".index"))
    else:
        courses = courseModel.Courses.search(info)
    return render_template("courses.html", courses=courses)
