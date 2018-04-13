from . import app
from flask import render_template, redirect, url_for, flash
from .models import Fit
from .forms import DataForm, FitSearchForm


@app.route('/')
def index():
    fileform = DataForm()
    searchform = FitSearchForm()

    if fileform.data_submit.data and fileform.validate_on_submit():
        return 'file sent'

    elif searchform.fit_search_submit.data and searchform.validate_on_submit():
        return redirect(url_for('show_fit', id=searchform.fit_id))

    return render_template('index.html',
                            fileform=fileform,
                            searchform=searchform,
                            title='Main Page')

@app.route('/fit/<id>')
def show_fit(id):
    fit = Fit.query.filter_by(id=id).first()

    if not fit:
        abort(404)

    return render_template(
                'fit.html',
                fit=fit,
                title='Fit #'+str(fit.id)
            )

@app.route('/418')
def about():
    flash('418 I am a teapot')
    return redirect(url_for('index'))

