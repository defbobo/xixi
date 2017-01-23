# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, abort, render_template

blueprint = Blueprint('cheatsheet', __name__, url_prefix='/cheatsheet', static_folder='../static')


@blueprint.route('/')
def home():
    """Cheatsheet home."""
    return render_template('cheatsheets/home.html')


@blueprint.route('/<string:page>', methods=['GET'])
def get_cheatsheet(page):
    """Return cs page by page."""
    try:
        return render_template('cheatsheets/{0}.html'.format(page))
    except Exception:
        abort(404)
