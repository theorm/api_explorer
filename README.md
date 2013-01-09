API Explorer
============

Automatic single page documentation for RESTful APIs.

For now only Flask is supported::

		from apiexplorer.flask import api_explorer
		app.register_blueprint(api_explorer, url_prefix='/docs')

List of all endpoints is available on 'http://localhost:5000/docs'

