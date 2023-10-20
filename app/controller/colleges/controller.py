from os import name
from flask.helpers import url_for
from app.controller.colleges.forms import collegeForm
from flask import render_template, redirect, request, jsonify, flash
from . import college
import app.models.college as collegeModel


@college.route("/college")
def index():
    colleges = collegeModel.Colleges.all()
    return render_template("colleges.html", colleges=colleges)


@college.route("/college/delete", methods=["POST"])
def delete_college():
    college_code = request.form["code"]
    if collegeModel.Colleges.delete(college_code):
        return jsonify(success=True, message="Successfully deleted College!")
    else:
        return jsonify(
            success=False,
            message="Failed to Delete College, Data was Referenced in Courses!",
        )


@college.route("/college/add", methods=["POST", "GET"])
def add_college():
    form = collegeForm(request.form)
    if request.method == "POST" and form.validate():
        college = collegeModel.Colleges(code=form.code.data, name=form.name.data)
        college.add()
        flash("College added successfully!", "success")
        return redirect("/college")
    else:
        flash("Error: Please check the form for validation errors.", "danger")
        return redirect("/college")


@college.route("/college/update", methods=["POST"])
def update_college():
    if request.method == "POST":
        code = request.form["code"]
        name = request.form["name"]

        try:
            collegeModel.Colleges.update(code, name)
            return redirect(url_for(".index"))
        except Exception as e:
            return f"Error updating college: {str(e)}"


@college.route("/college/search", methods=["GET", "POST"])
def search_college():
    info = request.form.get("information")
    if info is None or info.strip() == "":
        colleges = collegeModel.Colleges.all()
    else:
        colleges = collegeModel.Colleges.search(info)
    return render_template("colleges.html", colleges=colleges)
