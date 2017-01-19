# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, abort


blueprint = Blueprint('cheatsheet', __name__, url_prefix='/cheatsheet', static_folder='../static')


@blueprint.route('/')
def home():
    """List members."""
    return render_template('cheatsheets/home.html')

@blueprint.route('/<string:page>', methods=['GET'])
def get_cheatsheet(page):
    try:
        return render_template('cheatsheets/{0}.html'.format(page))
    except:
        abort(404)
