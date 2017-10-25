import settings

from flask import Flask, Blueprint
from flask import render_template
from api.resources import name_space as todo_list_namespace
from api.api_provider import api
from database import db

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(todo_list_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


if __name__ == "__main__":
    initialize_app(app)
    print("============>>>>>>>>>>>>>>>>>App is initalized==============================")
    app.run(debug=settings.FLASK_DEBUG)

