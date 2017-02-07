# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    'vendor/bootstrap/dist/css/bootstrap.css',
    'css/x_creative.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'vendor/jQuery/dist/jquery.js',
    'vendor/bootstrap/dist/js/bootstrap.js',
    'js/x_creative.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
