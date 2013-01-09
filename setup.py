#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Api Explorer
============

One page documentation for your RESTful API.

Supports Flask.
'''

from setuptools import setup

setup(
    name='api-explorer',
    version='0.1.0',
    url='http://github.com/theorm/api-explorer',
    license='BSD',
    author='Roman Kalyakin',
    author_email='roman@kalyakin.com',
    description='One page automatic documentation for your RESTful API.',
    long_description=__doc__,
    packages=[
        'apiexplorer',
        'apiexplorer.flask',
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'jinja2',
        'docutils'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)