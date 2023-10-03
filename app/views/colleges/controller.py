from os import name
from flask.helpers import url_for
from app.views.colleges.forms import collegeForm
from flask import render_template, redirect, request, jsonify
from . import college
import app.models.college as models


@college.route("/college")
def index():
    colleges = models.Colleges.all()
    return render_template(
        "colleges.html", colleges=colleges, title="Home", something="something"
    )


@college.route("/college/delete", methods=["POST"])
def delete_college():
    id = request.form["id"]
    if models.Colleges.delete(id):
        return jsonify(success=True, message="Successful")
    else:
        return jsonify(success=False, message="Failed")
