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


# def index():
#     data = models.Students.all()
#     students = []
#     for student in data:
#         students.append(student)
#     return jsonify(students)


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
#             course=form.course.data,
#             year=form.year.data,
#             gender=form.gender.data,
#         )
#         student.add(image_url)
#         return redirect("/")
#     else:
#         course = models.Courses.refer()
#         return render_template("user/student.html", form=form, data=course)


# @student.route("/student/edit/<id>", methods=["POST", "GET"])
# def edit_student(id):
#     student = models.Students.edit(id)
#     course = models.Courses.refer()
#     return render_template("user/edit.html", data=student[0], datas=course)


# @student.route("/student/update/<id>", methods=["POST"])
# def update_student(id):
#     if request.method == "POST":
#         id_number = request.form["id_number"]
#         first_name = request.form["first_name"]
#         last_name = request.form["last_name"]
#         course = request.form["course"]
#         year = request.form["year"]
#         gender = request.form["gender"]

#         student = models.Students.update(
#             id, id_number, first_name, last_name, course, year, gender
#         )
#         return redirect(url_for(".index"))


# @student.route("/student/search", methods=["GET", "POST"])
# def search_student():
#     key_name = request.form.get("key_name")
#     students = models.Students.search(key_name)
#     return render_template("user/index.html", data=students)
