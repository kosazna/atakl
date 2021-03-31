# -*- coding: utf-8 -*-

import pandas as pd
from atakl.utilities import *


class Validator:
    def __init__(self, data: pd.DataFrame, process_name, mode=None):
        self.data = data
        self.log = Display(mode)
        self.map_name = process_name

        self.has_missing = False
        self.value_warnings = False
        self.duplicates = False

    def set_data(self, data: pd.DataFrame):
        self.data = data

    def set_process_name(self, name):
        self.map_name = name

    def col_has_na(self, column):
        return col_has_na(self.data, column, idx_shift=2)

    def col_values_equal_zero(self, column):
        return col_values_equal_zero(self.data, column, idx_shift=2)

    def col_values_not_equal_zero(self, column):
        return col_values_not_equal_zero(self.data, column, idx_shift=2)

    def col_values_over(self, column, value):
        return col_values_over(self.data, column, value, idx_shift=2)

    def col_values_over_or_equal(self, column, value):
        return col_values_over_or_equal(self.data, column, value, idx_shift=2)

    def col_values_under(self, column, value):
        return col_values_under(self.data, column, value, idx_shift=2)

    def col_values_under_or_equal(self, column, value):
        return col_values_under_or_equal(self.data, column, value, idx_shift=2)

    def duplicated_data(self, columns):
        if columns:
            return duplicated_data(self.data, columns, idx_shift=2)
        return False, list()

    def validate(self):
        cols_not_na = info_map[self.map_name].get(
            'validator', {}).get('missing', [])
        cols_under = info_map[self.map_name].get(
            'validator', {}).get('missing', [])
        cols_zero = info_map[self.map_name].get(
            'validator', {}).get('missing', [])

        missing_bools = []
        missing_idxs = []
        missing_col = []
        for idx, col in enumerate(cols_not_na):
            _has_missing, _missing_idxs = self.col_has_na(col)
            missing_bools.append(_has_missing)
            missing_idxs.append(_missing_idxs)
            missing_col.append(idx)

        under_bools = []
        under_idxs = []
        under_col = []
        for idx, (col, value) in enumerate(cols_under):
            _has_under, _under_idxs = self.col_values_over(col, value)
            under_bools.append(_has_under)
            under_idxs.append(_under_idxs)
            under_col.append(idx)

        nonzero_bools = []
        nonzero_idxs = []
        nonzero_col = []
        for idx, (col, value) in cols_zero:
            _has_nonzero, _nonzero_idxs = self.col_values_not_equal_zero(
                col, value)
            nonzero_bools.append(_has_nonzero)
            nonzero_idxs.append(_nonzero_idxs)
            nonzero_col.append(idx)

        _sub = info_map[self.map_name].get(
            'validator', {}).get('no_duplicates', [])
        duplicated_bool, duplicated_idxs = self.duplicated_data(_sub)

        self.has_missing = True if any(missing_bools) else False
        self.value_warnings = True if any(
            [any(under_bools), any(nonzero_bools)]) else False
        self.duplicates = duplicated_bool

        if self.has_missing:
            for i in missing_col:
                self.log(f"Missing values from: {cols_not_na[i]}\n",
                         Display.ERROR)
                self.log(f"Indexes: {'-'.join(missing_idxs[i])}")

        if self.value_warnings:
            for i in under_col:
                self.log(f"Column: {cols_under[i][0]} has values over {cols_under[i][1]}\n",
                         Display.WARNING)
                self.log(f"Indexes: {'-'.join(under_idxs[i])}")
            for i in under_col:
                self.log(f"Column: {cols_under[i][0]} has non zero values\n",
                         Display.WARNING)
                self.log(f"Indexes: {'-'.join(nonzero_idxs[i])}")

        if self.duplicates:
            self.log(f"Duplicated Data: [{'-'.join(_sub)}]\n",
                     Display.WARNING)
            self.log(f"Indexes: {'-'.join(duplicated_idxs)}")
