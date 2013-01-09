# -*- coding: utf-8 -*-

from docutils.core import publish_parts

def rule_to_endpoint(flask_app, rule, skip_methods=['OPTIONS', 'HEAD'], skip_endpoints=[]):
    func = flask_app.view_functions[rule.endpoint]
    code = '{}.{}'.format(func.__module__, func.__name__)
    
    if code not in skip_endpoints:
        endpoint = {
            'url' : rule.rule,
            'methods' : [m for m in rule.methods if m not in skip_methods],
            'arguments' : {arg:rule._converters[arg].__doc__ for arg in rule.arguments},
            'code' : code,
        }

        if func.__doc__:
            endpoint['docs'] = publish_parts(func.__doc__, writer_name='html')['html_body']

        return endpoint

def analyze_api(flask_app, skip_endpoints=[]):
    for rule in flask_app.url_map.iter_rules():
        endpoint = rule_to_endpoint(flask_app, rule, skip_endpoints=skip_endpoints)
        if endpoint:
            yield endpoint
