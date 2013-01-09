# -*- coding: utf-8 -*-

from flask import Blueprint, current_app as app
from .analyzer import analyze_api
from ..render import render_explorer

api_explorer = Blueprint('api_explorer', __name__)

@api_explorer.route('/', methods=['GET'])
def show():
    endpoints = analyze_api(app)
    return render_explorer(endpoints=endpoints, name=app.__name__)
