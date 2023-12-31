from os import name
from flask.helpers import url_for
from math import ceil
from app.controller.students.forms import StudentForm
from flask import render_template, redirect, request, jsonify, flash
from werkzeug.utils import secure_filename
from . import student
import app.models.student as studentModel
import app.models.course as courseModel
import app.models.course as courseModel
from cloudinary.uploader import upload

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
MAX_FILE_SIZE = 1 * 1024 * 1024 

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        and request.content_length <= MAX_FILE_SIZE
    )

def upload_to_cloudinary(file):
    try:
        upload_result = upload(file)
        return upload_result
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        return None


# Routes Here
@student.route("/", defaults={"page": 1})
@student.route("/student/<int:page>")
def index(page):
    limit = 5
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
        file = request.files["photo"]
        if str(file) != "<FileStorage: '' ('application/octet-stream')>":
            if not allowed_file(file.filename):
                flash(
                    "Error: Invalid file Upload. Exceeding 2 MB File Size.",
                    "danger",
                )
                return redirect(url_for(".index"))
            upload_result = upload_to_cloudinary(file)
            if upload_result and "secure_url" in upload_result:
                photo = upload_result["secure_url"]
            else:
                flash("Error: Failed to upload photo to Cloudinary.", "danger")
                return redirect(url_for(".index"))
        else:
            photo = "https://res.cloudinary.com/db52qexfl/image/upload/v1700228834/an2b07zud7ifxjmejw8z.jpg"
            flash("Error: No photo provided.", "warning")

        student = studentModel.Students(
            id=form.id.data,
            photo=photo,
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

        if "photo" in request.files:
            file = request.files["photo"]
            if str(file) != "<FileStorage: '' ('application/octet-stream')>":
                if not allowed_file(file.filename):
                    flash(
                    "Error: Invalid file Upload. Exceeding 2 MB File Size.",
                    "danger",
                    )
                    return redirect(url_for(".index"))
                
                upload_result = upload_to_cloudinary(file)
                if upload_result and "secure_url" in upload_result:
                    photo = upload_result["secure_url"]
                else:
                    flash("Error: Failed to upload photo to Cloudinary.", "danger")
                    return redirect(url_for(".index"))
            else:
                photo = studentModel.Students.get_photo_by_id(id)
                print(photo)
        try:
            studentModel.Students.update(
                id, photo, firstname, lastname, coursecode, year, gender
            )
            flash("Student updated successfully!", "success")
            return redirect(url_for(".index"))
        except Exception as e:
            flash(f"Error updating student: {str(e)}", "danger")
            return redirect(url_for(".index"))


@student.route("/student/search", methods=["GET", "POST"])
def search_student():
    info = request.form.get("information")
    if info is None or info.strip() == "":
        return redirect(url_for(".index"))
    else:
        students = studentModel.Students.search(info)
        courses = courseModel.Courses.refer()
    return render_template("searchStudents.html", students=students, courses=courses)
