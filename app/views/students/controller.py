from os import name
from flask.helpers import url_for
from app.views.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify
from . import student
import app.models.student as studentModel
import app.models.course as courseModel


@student.route("/")
@student.route("/student")
def index():
    students = studentModel.Students.all()
    return render_template(
        "students.html", students=students, title="Home", something="something"
    )


@student.route("/student/delete", methods=["POST"])
def delete_college():
    student_id = request.form["id"]
    if studentModel.Students.delete(student_id):
        return jsonify(success=True, message="Successfully deleted Student")
    else:
        return jsonify(success=False, message="Failed to Delete Student")


@student.route("/student/add", methods=["POST", "GET"])
def add_student():
    form = StudentForm(request.form)
    if request.method == "POST" and form.validate():
        student = studentModel.Students(
            id=form.id.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            coursecode=form.coursecode.data,
            year=form.year.data,
            gender=form.gender.data,
        )
        student.add()
        return redirect("/student")
    else:
        courses = courseModel.Courses.refer()
        return render_template("students.html", form=form, data=courses)


@student.route("/student/update", methods=["POST"])
def update_student():
    if request.method == "POST":
        id = request.form["id"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        coursecode = request.form["coursecode"]
        year = request.form["year"]
        gender = request.form["gender"]

        try:
            studentModel.Students.update(
                id, firstname, lastname, coursecode, year, gender
            )
            return redirect(url_for(".index"))
        except Exception as e:
            return f"Error updating college: {str(e)}"
