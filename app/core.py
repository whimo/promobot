import numpy as np
import pandas

import string
from datetime import datetime

from catboost import CatBoostRegressor

FEATURE_COLUMNS = ['period_start_date', 'period_end_date', 'period', 'discount',
                   'category', 'brand', 'line_up', 'type_of_promo', 'total_promo_cost',
                   'ivolume', 'base_volume_it']

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
                     'logging_level': 'Silent',
                     'loss_function': 'RMSE',
                     'verbose': 0}


def prettify_str(s):
    return s.translate(None, string.punctuation).strip().lower().replace(' ', '_')


def reformat_date(date, start=datetime(2000, 1, 1)):
    return (datetime.strptime(date, '%Y-%m-%d') - start).days


def generate_target(data):
    data[TARGET_COLUMN] = data['volume_it'] - data['base_volume']
    data = data.drop('volume_it', axis=0)
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
        self.data = data
        if not self.prepare_data():
            self.error = 'Invalid data provided'
            return -1

        self.model = CatBoostRegressor(**REGRESSION_PARAMS)
        cat_indexes = [list(self.data.keys()).index(i) for i in CATEGORICAL_FEATURES]
        self.model.fit(self.data.as_matrix(), self.target, cat_features=cat_indexes)

    def prepare_data(self):
        self.data = generate_target(self.data)
        self.data = self.data.rename(columns={key: prettify_str(key) for key in self.data.keys()})

        for col in self.data.keys():
            if isinstance(self.data[col][0], str) and col not in PERIOD_TIMES:
                self.data[col] = self.data[col].apply(prettify_str)

        self.data = self.data[FEATURE_COLUMNS]

        for promo_type in PROMO_TYPES:
            self.data['promo_{}'.format(promo_type)] = self.data[PROMO_TYPE_COLUMN]\
                .apply(lambda t: promo_type in PROMOS[t]).astype(np.int)

        self.data = self.data.drop(PROMO_TYPE_COLUMN, axis=1)

        self.data[PERIOD_TIMES[0]] = self.data[PERIOD_TIMES[0]].apply(reformat_date)
        self.data[PERIOD_TIMES[1]] = self.data[PERIOD_TIMES[1]].apply(reformat_date)
        self.data['duration'] = self.data[PERIOD_TIMES[1]] - self.data[PERIOD_TIMES[0]]
        self.data['period'] = self.data['period'] % 27

        for index, value in self.data['duration'].iteritems():
            if value != PERIOD_DURATION:
                for column in NUMERICAL:
                    self.data.loc[index, NUMERICAL] *= (PERIOD_DURATION / value)

        self.data = generate_new_features(self.data)
        self.target = self.data[TARGET_COLUMN].values
        self.data = self.data.drop(TODROP, axis=1)

        return True
