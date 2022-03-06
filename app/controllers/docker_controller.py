from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase

class DockerController(ControllerBase):
    @staticmethod
    def get():
        name = "kelly"
        return render_template('docker.html', name=name)
