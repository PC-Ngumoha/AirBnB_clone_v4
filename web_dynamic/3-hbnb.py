#!/usr/bin/python3
""" Renders a Web page with the list of all the States stores on the DB
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the current session with the DB """
    storage.close()


@app.route('/3-hbnb', strict_slashes=False)
def display_states_list():
    """ Renders the list of states in a web page """
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    places = storage.all(Place).values()
    return render_template('1-hbnb.html', amenities=amenities,
                           states=states, places=places,
                           cache_id=str(uuid.uuid4()))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
