from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import IntegerField


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
