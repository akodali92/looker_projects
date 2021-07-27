# python imports
from flask import render_template

# project imports
from app import app
# from ..models.projects import ProjectModel


@app.route("/projects")
def projects():
    return render_template('projects.html')
