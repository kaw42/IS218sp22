from flask import render_template
#don't change this import or it can't find the module controller
from . controller import ControllerBase

class GitController(ControllerBase):
    @staticmethod
    def get():
        name = "kelly"
        return render_template('git.html', name=name)
