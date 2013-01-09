# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader(__name__, 'templates'))

def render_explorer(endpoints, name):
    return env.get_template('explorer.html').render(endpoints=endpoints, name=name)
