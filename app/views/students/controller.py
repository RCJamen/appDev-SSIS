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


# @student.route("/student/add", methods=["POST", "GET"])
# def add_student():
#     form = StudentForm(request.form)
#     if request.method == "POST" and form.validate():
#         uploaded_file = upload(request.files["image_file"])
#         image_url, options = cloudinary_url(
#             uploaded_file["public_id"], format="jpg", width="100", height="100"
#         )
#         student = models.Students(
#             id_number=form.id_number.data,
#             first_name=form.first_name.data,
#             last_name=form.last_name.data,
#             student=form.student.data,
#             year=form.year.data,
#             gender=form.gender.data,
#         )
#         student.add(image_url)
#         return redirect("/")
#     else:
#         student = models.students.refer()
#         return render_template("user/student.html", form=form, data=student)


# @student.route("/student/edit/<id>", methods=["POST", "GET"])
# def edit_student(id):
#     student = models.Students.edit(id)
#     student = models.students.refer()
#     return render_template("user/edit.html", data=student[0], datas=student)


# @student.route("/student/update/<id>", methods=["POST"])
# def update_student(id):
#     if request.method == "POST":
#         id_number = request.form["id_number"]
#         first_name = request.form["first_name"]
#         last_name = request.form["last_name"]
#         student = request.form["student"]
#         year = request.form["year"]
#         gender = request.form["gender"]

#         student = models.Students.update(
#             id, id_number, first_name, last_name, student, year, gender
#         )
#         return redirect(url_for(".index"))
