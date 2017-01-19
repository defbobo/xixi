# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from .models import Order

blueprint = Blueprint('cheatsheet', __name__, static_folder='../static')


@blueprint.route('/')
@login_required
def home():
    """List members."""
    # return render_template('users/members.html')
    return 123
