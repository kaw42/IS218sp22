from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class CicdController(ControllerBase):
    @staticmethod
    def get():
        name = "kelly"
        return render_template('cicd.html', name=name)
