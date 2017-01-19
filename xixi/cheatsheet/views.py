# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from .models import Order

blueprint = Blueprint('xchange', __name__, static_folder='../static')


@blueprint.route('/trade.do')
@login_required
def trade():
    """List members."""
    return render_template('users/members.html')
