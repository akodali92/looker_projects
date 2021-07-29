# python imports
from flask import render_template

# project imports
from app import app
from ..models.events import EventModel


@app.route("/events")
def events():
    events = EventModel.query.all()
    return render_template('events.html', events=events)
