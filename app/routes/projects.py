# python imports
from flask import redirect, render_template, request, url_for

# project imports
from app import app
from ..models.dimensions.projects import ProjectDimension


@app.route("/projects")
def projects():
    projects = ProjectDimension.query.all()
    return render_template('projects.html', projects=projects)

@app.route("/projects/new", methods=['POST'])
def projects_new():
    form_dict = dict(request.form)
    project_record = ProjectDimension(**form_dict)
    try:
        project_record.save_to_db()
        print(f"Inserted: {project_record.sk_project}")
    except Exception as e:
        print(f"Not inserted: {e}")
    return redirect(url_for('projects'))

@app.route("/projects/<sk_project>", methods=['POST'])
def projects_project(sk_project):
    # get method type
    print(request.get_json)
    # query for project
    project = ProjectDimension.query.get(sk_project)
    print(project)
    return redirect(url_for('projects'))  