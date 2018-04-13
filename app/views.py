from . import app
from flask import render_template, redirect, url_for, flash, request, abort
from .models import Fit
from .forms import DataForm, FitSearchForm
from uuid import uuid4


@app.route('/', methods=['GET', 'POST'])
def index():
    fileform = DataForm()
    searchform = FitSearchForm()

    if request.form.get('data-submit') == 'Upload file' and fileform.validate_on_submit():
        flash('Successfully uploaded your fit!')
        return redirect(url_for('index'))
    elif request.form.get('data-submit') == 'Search' and searchform.validate_on_submit():
        return redirect(url_for('show_fit', id=searchform.fit_id.data))

    return render_template('index.html',
                           fileform=fileform,
                           searchform=searchform,
                           title='Main Page')


@app.route('/fit/<id>', methods=['GET', 'POST'])
def show_fit(id):
    fit = Fit.query.filter_by(id=id).first()

    if not fit:
        abort(404)

    return render_template(
        'fit.html',
        fit=fit,
        title='Fit #' + str(fit.id)
    )


@app.route('/418')
def about():
    flash('418 I am a teapot')
    return redirect(url_for('index'))

