# python imports
from flask import render_template

# project imports
from app import app
from ..models.dimensions.events import EventDimension


@app.route("/events")
def events():
    events = EventDimension.query.all()
    return render_template('events.html', events=events)
