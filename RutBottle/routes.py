"""
Routes and views for the bottle application.
"""

from bottle import route, view,request
from datetime import datetime
from rut import *

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/rut') #@get('/rut')
@view('rut')
def rut():
    """RUT"""
    RUT = request.forms.get('rut')
    rutc = rutController("  13.881.929-9  ")
    return dict(
        rut_str=rutc.limpiar(),
        year=datetime.now().year
    )

@route('/rut', method='POST')
def do_verif():
    rut = request.forms.get('rut')
    rutc = rutController("13881929-9")
    if rutc.validar():
        return "<p>Your rut information was correct.</p>"
    else:
        return "<p>rut failed.</p>"