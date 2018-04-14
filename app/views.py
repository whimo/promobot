from . import app, s3, db
from flask import render_template, redirect, url_for, flash, request, abort
from .models import Fit
from .forms import DataForm, FitSearchForm, GetPredictForm
from uuid import uuid4
from os import path
import pandas

@app.route('/', methods=['GET', 'POST'])
def index():
    fileform = DataForm()
    searchform = FitSearchForm()

    if request.form.get('data-submit') == 'Upload file':
        if fileform.validate_on_submit():
            real_file = fileform.file_data.data
            ext = real_file.filename.split('.')[-1]

            if ext in ['xls', 'xlsx']:
                csv = pandas.read_excel(real_file.stream).to_csv()

            elif ext in ['csv']:
                csv = real_file.stream.read()

            else:
                flash('Unrecognized document notation')
                return redirect(url_for('index'))

            fit = Fit(filename=str(uuid4()) + '.csv', done=False)
            db.session.add(fit)
            db.session.commit()

            s3.put_object(Body=csv, Bucket='just-a-name', Key='csv/' + fit.filename)

            flash('Successfully uploaded your fit!')
            return redirect(url_for('index'))

        else:
            for _, err_list in fileform.errors.items():
                for err in err_list:
                    flash('New Fit - ' + err, 'error')

    elif request.form.get('data-submit') == 'Search':
        if searchform.validate_on_submit():
            return redirect(url_for('show_fit', id=searchform.fit_id.data))
        else:
            for _, err_list in searchform.errors.items():
                for err in err_list:
                    flash('Existing Fit - ' + err, 'error')

    return render_template('index.html',
                           fileform=fileform,
                           searchform=searchform,
                           title='Main Page')


@app.route('/fit/<id>', methods=['GET', 'POST'])
def show_fit(id):
    fit = Fit.query.filter_by(id=id).first()

    if not fit:
        abort(404)

    superform = GetPredictForm()

    if superform.validate_on_submit():
        return 'OK!'

    return render_template(
        'fit.html',
        fit=fit,
        form=superform,
        title='Fit #' + str(fit.id)
    )


@app.route('/418')
def about():
    flash('418 I am a teapot')
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
                           title='404 Not Found'), 404
