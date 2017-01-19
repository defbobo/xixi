# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, abort, render_template

blueprint = Blueprint('cheatsheet', __name__, url_prefix='/cheatsheet', static_folder='../static')


@blueprint.route('/')
def home():
    """Cheatsheet home."""
    return render_template('cheatsheets/home.html')


@blueprint.route('/<string:id>', methods=['GET'])
def get_cheatsheet(id):
    """Return cs page by id."""
    try:
        return render_template('cheatsheets/{0}.html'.format(id))
    except Exception:
        abort(404)
