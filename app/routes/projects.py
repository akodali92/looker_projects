# python imports
from flask import redirect, render_template, request, url_for

# project imports
from app import app
from ..models.projects import ProjectModel


@app.route("/projects")
def projects():
    projects = ProjectModel.query.all()
    return render_template('projects.html', projects=projects)

@app.route("/projects/new", methods=['POST'])
def projects_new():
    form_dict = dict(request.form)
    project_record = ProjectModel(**form_dict)
    try:
        project_record.save_to_db()
        print(f"Inserted: {project_record.sk_project}")
    except Exception as e:
        print(f"Not inserted: {e}")
    return redirect(url_for('projects'))