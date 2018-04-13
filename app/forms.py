from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import IntegerField, SubmitField, RadioField, DecimalField, SelectMultipleField, FieldList, FormField


class DataForm(FlaskForm):
    file_data = FileField(validators=[FileRequired()])


class FitSearchForm(FlaskForm):
    fit_id = IntegerField()


_categories = ['Shave Prep',
               'Fem Care',
               'Laundry',
               'Hair Care',
               'Oral Care ',
               'Dish Care',
               'Blades & Razors',
               'Fabric Enhancers',
               'APDO/PCC',
               'Surface Care',
               'Wipes']

_brands = ['Proglide',
           'Always',
           'Ariel',
           'Aussie',
           'BAM',
           'Discreet',
           'Fairy',
           'Fusion',
           'Gillette',
           'Head & Shoulders',
           'Lenor',
           'Mach3',
           'Myth',
           'Naturella',
           'Old Spice',
           'Oral-B',
           'Pantene',
           'Mr. Proper',
           'Series',
           'Tampax',
           'Tide',
           'Venus',
           'Wella Pro',
           'Blue 2',
           'Blue 3',
           'Gillette 2',
           'Gillette APDO',
           'Satin Care',
           'Safeguard',
           'Slalom',
           'Venus 2',
           'Venus 3',
           'Wipes']


_promo_types = ['Display',
                'Display&Feature',
                'Mega Event',
                'TPR',
                'Display&Banner',
                'None']


class EntryForm(FlaskForm):
    budget_from = DecimalField()
    budget_to = DecimalField()
    promo_type = RadioField(_promo_types[0], choices=[(t, t) for t in _promo_types])
    brand = SelectMultipleField(_brands[0], choices=[(b, b) for b in _brands])
    repeat_count = IntegerField()


class GetPredictForm(FlaskForm):
    category = RadioField(_categories[0], choices=[(cat, cat) for cat in _categories])
    num_of_entries = IntegerField()
    promo_budget = DecimalField()
    per_entry_params = FieldList(FormField())
