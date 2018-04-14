import numpy as np
import pandas

import string
from datetime import datetime

from catboost import CatBoostRegressor

FEATURE_COLUMNS = ['period_start_date', 'period_end_date', 'period', 'discount',
                   'category', 'brand', 'line_up', 'type_of_promo', 'total_promo_cost',
                   'volume_it', 'base_volume_it']

TARGET_COLUMN = 'ivolume'
TODROP = ['period_start_date', 'period_end_date', 'duration', 'total_promo_cost', 'ivolume']

PROMOS = {'display': ['display', 'discount'],
          'displayfeature': ['display', 'feature', 'discount'],
          'mega_event': ['display', 'feature', 'discount', 'mega_dicsount'],
          'tpr': ['discount'],
          'displaybanner': ['display', 'banner', 'discount'],
          '0': []}

PROMO_TYPES = ['display', 'feature', 'discount', 'mega_dicsount', 'banner']
PROMO_TYPE_COLUMN = 'type_of_promo'

PERIOD_TIMES = ('period_start_date', 'period_end_date')
PERIOD_DURATION = 13.0

NUMERICAL = ('total_promo_cost', 'ivolume')
CATEGORICAL_FEATURES = ['category', 'brand', 'line_up', 'period']


REGRESSION_PARAMS = {'depth': 4,
                     'iterations': 90,
                     'learning_rate': 0.15,
                     'loss_function': 'RMSE',
                     'verbose': False}


def prettify_str(s):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in s if ch not in exclude).strip().lower().replace(' ', '_')


def reformat_date(date, start=datetime(2000, 1, 1)):
    return (datetime.strptime(date, '%Y-%m-%d') - start).days


def generate_target(data):
    data[TARGET_COLUMN] = data['volume_it'] - data['base_volume_it']
    return data


def generate_new_features(data):
    data['cont'] = np.zeros(data.shape[0])
    for index, value in data['period'].iteritems():
        try:
            if (value + 1) % 27 == data['period'][index + 1]\
                    and data['line_up'][index] == data['line_up'][index + 1]:
                data.loc[index + 1, 'cont'] = data.loc[index, 'cont'] + 1
        except KeyError:
            pass

    return data


class PromoGenerator(object):
    def __init__(self):
        self.raw_data = None
        self.data = None
        self.target = None
        self.error = None
        self.model = None

    def fit(self, data):
        self.raw_data = data.copy()
        if not self.prepare_data(data):
            self.error = 'Invalid data provided'
            return -1

        self.model = CatBoostRegressor(**REGRESSION_PARAMS)
        cat_indexes = [list(self.data.keys()).index(i) for i in CATEGORICAL_FEATURES]
        self.model.fit(self.data.as_matrix(), self.target, cat_features=cat_indexes)

    def prepare_data(self, data):
        data = data.rename(columns={key: prettify_str(key) for key in data.keys()})

        for col in data.keys():
            if isinstance(data[col][0], str) and col not in PERIOD_TIMES:
                data[col] = data[col].apply(prettify_str)

        data = data[FEATURE_COLUMNS]
        data = generate_target(data)

        for promo_type in PROMO_TYPES:
            data['promo_{}'.format(promo_type)] = data[PROMO_TYPE_COLUMN]\
                .apply(lambda t: promo_type in PROMOS[t]).astype(np.int)

        data = data.drop(PROMO_TYPE_COLUMN, axis=1)

        data[PERIOD_TIMES[0]] = data[PERIOD_TIMES[0]].apply(reformat_date)
        data[PERIOD_TIMES[1]] = data[PERIOD_TIMES[1]].apply(reformat_date)
        data['duration'] = data[PERIOD_TIMES[1]] - data[PERIOD_TIMES[0]]
        data['period'] = data['period'] % 27

        for index, value in data['duration'].iteritems():
            if value != PERIOD_DURATION:
                for column in NUMERICAL:
                    data.loc[index, column] *= (PERIOD_DURATION / value)

        data = generate_new_features(data)
        self.target = data[TARGET_COLUMN].values
        data = data.drop(TODROP, axis=1)

        self.data = data

        return True
