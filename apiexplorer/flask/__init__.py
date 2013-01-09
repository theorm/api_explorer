# -*- coding: utf-8 -*-

from .blueprint import api_explorer

def add_explorer_to(app, url='/explorer'):
    app.register_blueprint(api_explorer, url_prefix=url)
