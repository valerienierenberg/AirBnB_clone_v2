#!/usr/bin/python3
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes:
    - /states_list
"""
from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display HTML page with city and state data from storage engine"""
    all_states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def remove_SQLalc_session(exception):
    """ close storage when tear down occurs """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
