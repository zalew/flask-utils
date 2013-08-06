Flask-utils
============

Various Flask utilities. It's a work in progress lib where I dump stuff occasionally. Feel free to contribute yours and send me pull requests.

.. image:: https://pypip.in/v/flask-utils/badge.png
    :target: https://crate.io/packages/flask-utils/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/flask-utils/badge.png
    :target: https://crate.io/packages/flask-utils/
    :alt: Number of PyPI downloads

Project links
-------------

**Source**

* builds: http://pypi.python.org/pypi/flask-utils/
* repository: https://bitbucket.org/zalew/flask-utils/
* mirror: https://github.com/zalew/flask-utils/

Install
--------

.. code-block:: shell

    pip install flask-utils

Contents
---------


**decorators.py**

.. code-block:: python

    from flask_utils.decorators import render

    @render('index.html')
    def homepage():    
        return {'var1': 1, 'var2': 2}
    
    
**jinja2htmlcompress.py**

https://github.com/mitsuhiko/jinja2-htmlcompress/
