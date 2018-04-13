from . import app
from flask import render_template
from .models import Fit


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fit/<id>')
def show_fit(id):
    
    fit = Fit.query.filter_by(id=id).first()

    if not fit:
        abort(404)

    return render_template(
                'fit.html',
                fit=fit,
                id=id
            )

@app.route('/418')
def about():
    return '418 I am teapot'

