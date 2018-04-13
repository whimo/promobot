from flask_wtf import FlaskForm, IntegerField
from flask_wtf.file import FileForm, FileRequired


class DataForm(FlaskForm):
    file_data = FileField(validators=[FileRequired()])


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


class GetPredictForm(FlaskForm):
    category = RadioField(u'Category', choices=[(cat, cat) for cat in _categories])
    num_of_entries = IntegerField(validators=[Required()])

