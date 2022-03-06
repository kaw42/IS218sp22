"""A simple flask web app"""
from flask import Flask, render_template

from controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication
from controllers.git_controller import GitController
from controllers.docker_controller import DockerController
from controllers.python_controller import PythonController
from controllers.cicd_controller import CicdController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/git", methods=['GET'])
def git_get():
    return GitController.get()

@app.route("/docker", methods=['GET'])
def docker_get():
    return DockerController.get()

@app.route("/python", methods=['GET'])
def python_get():
    return PythonController.get()

@app.route("/cicd", methods=['GET'])
def cicd_get():
    return CicdController.get()