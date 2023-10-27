from os import name
from flask.helpers import url_for
from math import ceil
from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from . import student
import app.models.student as studentModel
import app.models.course as courseModel


@student.route("/", defaults={"page": 1})
@student.route("/student/<int:page>")
def index(page):
    limit = 7
    offset = page * limit - limit
    total_row = len(studentModel.Students.all())
    total_page = ceil(total_row / limit)
    next = page + 1
    prev = page - 1
    students = studentModel.Students.page(limit, offset)
    courses = courseModel.Courses.refer()
    return render_template(
        "students.html",
        students=students,
        courses=courses,
        page=total_page,
        next=next,
        prev=prev,
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
        existing_student = studentModel.Students.exists(form.id.data)
        if existing_student:
            flash("Error: Student with the same ID already exists.", "danger")
            return redirect(url_for(".index"))

        student.add()
        flash("Student added successfully!", "success")
        return redirect(url_for(".index"))
    else:
        flash("Error: Failed to add Student, Please check your Input.", "danger")
        return redirect(url_for(".index"))


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


@student.route("/student/search", methods=["GET", "POST"])
def search_student():
    info = request.form.get("information")
    if info is None or info.strip() == "":
        return redirect(url_for(".index"))
    else:
        students = studentModel.Students.search(info)
        courses = courseModel.Courses.refer()
    return render_template("searchStudents.html", students=students, courses=courses)
