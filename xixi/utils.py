# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash
import json
import os


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)

def read_resume(resume_path):
    print(os.getcwd())
    return json.load(open(resume_path))
