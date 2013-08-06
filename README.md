flask-utils
===========

[![](https://pypip.in/v/flask-utils/badge.png)](https://crate.io/package/flask-utils)

Various Flask utilities. It's a work in progress lib where I dump stuff occasionally. Feel free to contribute yours and send me pull requests.

## Install

    pip install flask-utils

## Contents


### decorators.py

    from flask_utils.decorators import render

    @render('index.html')
    def homepage():    
        return {'var1': 1, 'var2': 2}
    
    
### jinja2htmlcompress.py

https://github.com/mitsuhiko/jinja2-htmlcompress/
