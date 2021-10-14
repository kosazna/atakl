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

        self.validation_passed = True

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

    def cavino_check(self):
        kivotia_count = len(self.data.loc[self.data[kivotia] > 10])
        pal_count = len(
            self.data.loc[self.data[kodikos_paraggelias].str.startswith('PAL', na=False)])

        return kivotia_count != pal_count, kivotia_count, pal_count

    def cavino_extra_check(self):
        mask1 = self.data[pelatis] == 'ΧΛΑΜΠΕΑ ΑΦΟΙ ΟΕ'

        _nas = self.data.loc[mask1]
        _idxs = (_nas.index + 2).tolist()

        return not _nas.empty, _idxs

    def essse_check(self):

        grouper = [distribution_date,
                   customer_name,
                   delivery_area,
                   city]

        _grouped = self.data.groupby(grouper, as_index=False)[
            [cartons, weight]].sum()

        _grouped['Must_Have_PAL'] = _grouped.apply(
            lambda x: 1 if (x[weight]/6 + x[cartons]) >= 11 else 0, axis=1)

        must_have_pal = _grouped.loc[_grouped['Must_Have_PAL'] == 1].copy()

        has_pal = self.data.loc[self.data[order_code].str.startswith('PAL', na=False)][[order_code, distribution_date,
                                                                                        customer_name,
                                                                                        delivery_area,
                                                                                        city]]

        df = must_have_pal.merge(has_pal, how='outer',
                                 on=grouper).sort_values(grouper)
        df['Must_Have_PAL'] = df['Must_Have_PAL'].fillna(0).astype(int)

        has_zeros = all(df['Must_Have_PAL'] == 1)
        has_nas = all(df[order_code].notna())

        passes = has_zeros and has_nas

        return passes, df

    def kitsanelis_check(self):
        v = self.data.copy()
        v['kivotia_sum'] = v[kivotia_diafimistikou] + \
            v[kivotia_ximou] + v[kivotia_6fialon] + v[kivotia_12fialon]
        must_pals = v.loc[v['kivotia_sum'] > 10, [kodikos_paraggelias]]
        pals = v.loc[v[kodikos_paraggelias].str.startswith(
            'PAL', na=False)][kodikos_arxikis_paraggelias]
        result = must_pals.merge(
            pals, how='left', left_on=kodikos_paraggelias, right_on=kodikos_arxikis_paraggelias)
        missing_pals = result.loc[result[kodikos_arxikis_paraggelias].isna(
        ), kodikos_paraggelias].tolist()

        return missing_pals

    def siganos_check(self):
        prob = self.data.loc[(~self.data[kodikos_paraggelias].str.startswith(
            'PAL')) & (self.data[temaxia] != 0)].index + 2
        return prob.tolist()

    def validate(self):
        cols_not_na = info_map[self.map_name].get(
            'validator', {}).get('missing', [])
        cols_under = info_map[self.map_name].get(
            'validator', {}).get('ensure_under', [])
        cols_zero = info_map[self.map_name].get(
            'validator', {}).get('ensure_zero', [])
        _sub = info_map[self.map_name].get(
            'validator', {}).get('no_duplicates', [])

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
        for idx, col in enumerate(cols_zero):
            _has_nonzero, _nonzero_idxs = self.col_values_over(col, 0)
            nonzero_bools.append(_has_nonzero)
            nonzero_idxs.append(_nonzero_idxs)
            nonzero_col.append(idx)

        duplicated_bool, duplicated_idxs = self.duplicated_data(_sub)

        self.has_missing = True if any(missing_bools) else False
        self.value_warnings = True if any(
            [any(under_bools), any(nonzero_bools)]) else False
        self.duplicates = duplicated_bool

        if self.has_missing:
            self.validation_passed = False
            for i in missing_col:
                if missing_bools[i]:
                    self.log(f"[{cols_not_na[i]}] contains [{len(missing_idxs[i])}] missing values",
                             Display.WARNING)
                    self.log(f"Index: {'-'.join(map(str, missing_idxs[i]))}\n",
                             Display.INFO)

                self.log()

        if self.value_warnings:
            self.validation_passed = False
            for i in under_col:
                if under_bools[i]:
                    self.log(f"[{cols_under[i][0]}] contains [{len(under_idxs[i])}] values over {cols_under[i][1]}",
                             Display.WARNING)
                    self.log(f"Index: {'-'.join(map(str, under_idxs[i]))}\n",
                             Display.INFO)
                    self.log()
            for i in nonzero_col:
                if nonzero_bools[i]:
                    self.log(f"[{cols_zero[i]}] contains [{len(nonzero_idxs[i])}] non-zero values",
                             Display.WARNING)
                    self.log(f"Index: {'-'.join(map(str, nonzero_idxs[i]))}\n",
                             Display.INFO)
                    self.log()

        if self.duplicates:
            self.validation_passed = False
            self.log(f"[{'-'.join(_sub)}] contains duplicated data",
                     Display.WARNING)
            self.log(
                f"Index: {'-'.join(map(str, duplicated_idxs))}\n", Display.INFO)
            self.log()

        if self.map_name == 'Cavino':
            cav_diff, kivotia_count, pal_count = self.cavino_check()
            has_certain_client, idxs = self.cavino_extra_check()

            if cav_diff:
                self.validation_passed = False
                self.log(f"[{kivotia_count}] records with 'Κιβώτια' > 10",
                         Display.WARNING)
                self.log(f"[{pal_count}] records with 'Κωδικός Παραγγελίας' starting with PAL\n",
                         Display.WARNING)
                self.log()

            if has_certain_client:
                self.validation_passed = False
                self.log(f"Data contains client 'ΧΛΑΜΠΕΑ ΑΦΟΙ ΟΕ'",
                         Display.WARNING)
                self.log(f"Index: {'-'.join(map(str, idxs))}\n", Display.INFO)

                self.log()

        if self.map_name == 'Essse':
            passes, df = self.essse_check()

            if not passes:
                self.validation_passed = False
                self.log("Clients that must have orders starting with PAL start with 1:",
                         Display.INFO)
                self.log("Clients that should NOT have orders starting with PAL but do have, start with 0:\n",
                         Display.INFO)

                for i in df.itertuples():
                    _pal = f'{" "*17}' if pd.isna(
                        i.Order_Code) else i.Order_Code
                    self.log(
                        f"{i.Must_Have_PAL} | {_pal} | {i.Distribution_Date:%d/%m/%Y} | {i.Customer_Name} | {i.Delivery_Area}")
                    self.log("-" * 150)
                self.log()

        if self.map_name == "Kitsanelis":
            missing_pals = self.kitsanelis_check()

            if missing_pals:
                self.validation_passed = False
                self.log("Orders that must have orders starting with PAL and don't:",
                         Display.INFO)

                for order in missing_pals:
                    self.log(f"  - {order}")
                self.log()

        if self.map_name == "Siganos":
            probs = self.siganos_check()

            if probs:
                self.validation_passed = False
                self.log(f"Order not starting with PAL contains [{temaxia}] - Count: {len(probs)}",
                         Display.WARNING)
                self.log(f"Index: {'-'.join(map(str, probs))}\n", Display.INFO)

        if self.validation_passed:
            self.log('Data Validation: Successful', Display.INFO)
