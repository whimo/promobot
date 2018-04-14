from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import IntegerField, RadioField, DecimalField, SelectMultipleField, FieldList, FormField, ValidationError


def DataForm_FileRequired():
    return FileRequired(message='You need to upload input data')


class DataForm(FlaskForm):
    file_data = FileField(validators=[DataForm_FileRequired()])


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

_lines = ['After Shave Fusion/ProGl', 'Always Liners Trio',
       'Always Platinum Duo', 'Always Platinum Single', 'Always Sens Duo',
       'Always Ultra Duo', 'Always Ultra Quadro', 'Always Ultra Single',
       'Ariel Ambrosia LT 12', 'Ariel Ambrosia LT 15',
       'Ariel Ambrosia LT 23', 'Ariel Ambrosia LT 3',
       'Ariel Ambrosia LT 30', 'Ariel Gel 1105ml/1300ml',
       'Ariel Gel 1690ml/1950ml', 'Ariel Gel 2600ml',
       'Ariel Gel 975ml/1040ml', 'Ariel HS 450g', 'Ariel LS 1500g',
       'Ariel LS 3000g', 'Ariel LS 4500g', 'Ariel LS 450g',
       'Ariel LS 5400g', 'Ariel LS 6000g', 'Ariel LS 9000g',
       'Aussie sh/cnd 300/250', 'BAM 3D White', 'BAM 3D White Luxe',
       'BAM Complete7', 'BAM Pro-Expert 100ml', 'Discreet 100',
       'Discreet 50/60', 'Fairy ADW 10/12', 'Fairy ADW 18/24',
       'Fairy ADW 27/36', 'Fairy ADW 37/48', 'Fairy ADW 50/60',
       'Fairy ADW 84', 'Fairy Base line 1000ml/900ml',
       'Fairy Base line 500ml/450ml', 'Fairy Base line 650ml',
       'Fairy Platinum/ProDerma 500/480/450/430ml',
       'Fairy Platinum/ProDerma 750/720/650ml', 'Fusion Gel ShvP 200ml',
       'Fusion ProGlide Flexball 1up', 'Fusion ProGlide Flexball 2up',
       'Fusion ProGlide Gel/Foam ShvP 200/250ml',
       'Fusion ProGlide ProShield 1up',
       'Fusion ProGlide ProShield Chill 1up', 'Gillette Foam ShvP 200 ml',
       'H&S sh200/cnd180', 'H&S sh400/cnd360',
       'Lenor Concentrate 1L/930ml', 'Lenor Concentrate 2L/1800ml',
       'Lenor Dilute 1L', 'Lenor Dilute 2L', 'Lenor Dilute 4L',
       'Mach3 1up', 'Mach3 2up', 'Mach3 Gel ShvP 200 ml', 'Myth 1L',
       'Myth 500ml', 'Myth Gel 1625ml/1560ml', 'Myth Gel 2470ml/2080ml',
       'Myth HS 400g', 'Myth LS 2000g', 'Myth LS 4000g', 'Myth LS 400g',
       'Myth LS 6000g', 'Myth LS 9000g', 'Naturella Liners 100',
       'Naturella Liners 50/58/60', 'Naturella Ultra Duo',
       'Naturella Ultra Quadro', 'Old Spice Deo Spray',
       'Old Spice Deo Stick', 'Old Spice Shower 250ml',
       'Oral-B Complex Deep Clean/Antibac',
       'Oral-B Green, Black Tea, Ultrathin, 3D White\\Fresh, 5Way Clean',
       'Oral-B Rinse 250 ml LUXE', 'Oral-B Rinse 250ml',
       'Oral-B Vitality D12 3DWLuxe/Pro-Expert', 'PPV sh/cnd250/200',
       'PPV sh/cnd400/360', 'Proper 1.5L', 'Proper 1L', 'Proper 500ml',
       'Proper 750ml', 'Series Gel ShvP 200 ml', 'Tampax Compak 16',
       'Tampax Pearl 18', 'Tide Ambrosia LT15', 'Tide Ambrosia LT20/LT23',
       'Tide Ambrosia LT26/LT30', 'Tide Gel 1300ml/1235ml',
       'Tide Gel 1950ml/1820ml', 'Tide Gel 2470ml', 'Tide HS 400g',
       'Tide LS 12000g', 'Tide LS 1500g', 'Tide LS 2400g Baby',
       'Tide LS 3000g', 'Tide LS 3500g', 'Tide LS 4500g',
       'Tide LS 4500g Baby', 'Tide LS 450g', 'Tide LS 5400g',
       'Tide LS 5400g Baby', 'Tide LS 6000g', 'Tide LS 6000g Baby',
       'Tide LS 9000g', 'Venus 1up-2up', 'Venus Embrace 1up-2up',
       'Venus Proskin 1up-2up', 'Venus Swirl 1up',
       'Wella PS sh/cnd 500ml', 'After Shave Gillette 75 ml',
       'After Shave Mach3', 'After Shave Series', 'Always Classic',
       'Always Liners Duo', 'Always Liners Platinum 50',
       'Always Liners Single', 'Always Sens Single',
       'Ariel Ambrosia LT 38', 'BAM 3Effect', 'BAM Anti-cavity',
       'BAM BIO', 'BAM Pillar 1 Clinic Line 75 ml', 'BAM Pro-Expert 75ml',
       'BAM Toothbrushes', 'BAM Whitestrips', 'Blue 2 Disposables',
       'Blue 3 Disposables', 'Discreet 16/20', 'Fairy 5L', 'Fusion 1up',
       'Fusion 2up', 'Fusion CRT 4', 'Fusion CRT 8', 'Fusion PWR 1up',
       'Fusion PWR CRT 4', 'Fusion PWR CRT 8', 'Fusion ProGlide 1up',
       'Fusion ProGlide CRT 2', 'Fusion ProGlide CRT 4',
       'Fusion ProGlide PWR 1up', 'Fusion ProGlide PWR CRT 2',
       'Fusion ProGlide PWR CRT 4', 'Fusion ProGlide PWR CRT 8',
       'Fusion ProShield CRT 2', 'Fusion ProShield CRT 4',
       'Gillette 2 Disposables', 'Gillette Clear Gel',
       'Gillette Power Beads', 'H&S sh600', 'H&S sh90/75',
       'H&S treatments', 'Mach3 CRT 2', 'Mach3 CRT 4', 'Mach3 CRT 8',
       'Mach3 Foam ShvP 250 ml', 'Mach3 Turbo 1up', 'Mach3 Turbo 2up',
       'Mach3 Turbo CRT 4', 'Mach3 Turbo CRT 8', 'Naturella Classic Duo',
       'Naturella Classic Single', 'Naturella Liners 16/20',
       'Naturella Ultra Single', 'Old Spice After Shave',
       'Old Spice Clear Gels', 'Oral-B Brushes',
       'Oral-B CrossAction Power', 'Oral-B Floss', 'Oral-B KIDS D10',
       'Oral-B KIDS Stages', 'Oral-B Maxi Clean',
       'Oral-B Pro Expert AiO, NEON',
       'Oral-B Pro Expert Extra Clean, Antibac, Massager, Pro-Flex, Compact, Brilliance',
       'Oral-B Professional Care 500/Trizone 500', 'Oral-B Pulsar',
       'Oral-B Rinse 250 ml Complete', 'Oral-B Rinse 250 ml Pro Expert',
       'PPV Expert sh/cnd250/200', 'PPV sh/cnd600', 'PPV treatments',
       'Proper HS 400g', 'SATIN CARE Gel 200ml', 'Safeguard Bar Soap',
       'Safeguard Liquid', 'Series Foam ShvP 250 ml', 'Slalom 1up',
       'Slalom CRT 5', 'Tampax CEF 16', 'Tide HS 450g',
       'Venus & Olay 1up-2up', 'Venus & Olay CRT 2', 'Venus & Olay CRT 4',
       'Venus 2 Disposables', 'Venus 3 Disposables', 'Venus Breeze 2up',
       'Venus Breeze CRT 4', 'Venus CRT 2', 'Venus CRT 4',
       'Venus Embrace CRT 2', 'Venus Embrace CRT 4',
       'Venus Proskin CRT 4', 'Venus Swirl CRT 2', 'Venus Swirl CRT 4',
       'Wella treatments', 'Wipes Baby Fresh Duo ',
       'Wipes Baby Fresh Quadro ', 'Wipes Baby Fresh Single',
       'Wipes Naturally Clean Duo ', 'Wipes Sensitive Duo ',
       'Wipes Sensitive Single']

_brands = _lines

_promo_types = ['Display',
                'Display&Feature',
                'Mega Event',
                'TPR',
                'Display&Banner',
                'None']


class EntryForm(FlaskForm):
    sale_from = DecimalField()
    sale_to = DecimalField()
    promo_type = RadioField(_promo_types[0], choices=[(t, t) for t in _promo_types], default=_promo_types[-1])
    brand = SelectMultipleField(_brands[0], choices=[(b, b) for b in _brands])
    repeat_count = IntegerField()


class GetPredictForm(FlaskForm):
    category = RadioField(_categories[0], choices=[(cat, cat) for cat in _categories], default=_categories[0])
    num_of_entries = IntegerField()
    promo_budget = DecimalField()
    per_entry_params = FieldList(FormField(EntryForm), min_entries=1)
