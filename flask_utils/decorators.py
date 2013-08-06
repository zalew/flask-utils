#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask.templating import render_template
from functools import wraps


def render(template_name_or_list):
    def renderer(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            output = function(*args, **kwargs)
            if not isinstance(output, dict):
                return output
            return render_template(template_name_or_list, **output)
        return wrapper
    return renderer
