from os import name
from flask.helpers import url_for
from app.views.colleges.forms import collegeForm
from flask import render_template, redirect, request, jsonify
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
        return jsonify(success=True, message="Successfully deleted College")
    else:
        return jsonify(success=False, message="Failed to Delete College")


@college.route("/college/add", methods=["POST", "GET"])
def add_college():
    form = collegeForm(request.form)
    if request.method == "POST" and form.validate():
        college = collegeModel.Colleges(code=form.code.data, name=form.name.data)
        college.add()
        return redirect("/college")
    else:
        return render_template("colleges.html", form=form)


@college.route("/college/update/<id>", methods=["POST"])
def update_college(id):
    if request.method == "POST":
        code = request.form["code"]
        name = request.form["name"]

        colleges = collegeModel.Colleges.update(id, code, name)
        return redirect(url_for("college.index"))
