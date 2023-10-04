from os import name
from flask.helpers import url_for
from app.views.colleges.forms import collegeForm
from flask import render_template, redirect, request, jsonify
from . import college
import app.models.college as collegeModel


@college.route("/college")
def index():
    colleges = collegeModel.Colleges.all()
    return render_template(
        "colleges.html", colleges=colleges, title="Home", something="something"
    )


@college.route("/college/delete", methods=["POST"])
def delete_college():
    id = request.form["id"]
    if collegeModel.Colleges.delete(id):
        return jsonify(success=True, message="Successful")
    else:
        return jsonify(success=False, message="Failed")


@college.route("/college/add", methods=["POST", "GET"])
def add_college():
    form = collegeForm(request.form)
    if request.method == "POST" and form.validate():
        college = collegeModel.Colleges(code=form.code.data, name=form.name.data)
        college.add()
        return redirect("/college")
    else:
        return render_template("colleges.html", form=form)
