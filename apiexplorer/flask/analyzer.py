# -*- coding: utf-8 -*-

from docutils.core import publish_parts

def rule_to_endpoint(flask_app, rule, skip_methods=['OPTIONS', 'HEAD']):
    func = flask_app.view_functions[rule.endpoint]
    endpoint = {
        'url' : rule.rule,
        'methods' : [m for m in rule.methods if m not in skip_methods],
        'arguments' : {arg:rule._converters[arg].__doc__ for arg in rule.arguments},
        'code' : '{}.{}'.format(func.__module__, func.__name__),
    }

    if func.__doc__:
        endpoint['docs'] = publish_parts(func.__doc__, writer_name='html')['html_body']

    return endpoint

def analyze_api(flask_app):
    return [rule_to_endpoint(flask_app, rule) for rule in flask_app.url_map.iter_rules()]
