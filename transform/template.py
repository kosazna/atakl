# -*- coding: utf-8 -*-

import pandas as pd
from atakl.utilities import *
from atakl.validate.data import Validator


class TypeTemplate:
    def __init__(self, data_filepath: (str, Path),
                 cost_filepath: (str, Path),
                 mode='GUI'):
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.log = Display(mode)
        self.output = ""
        self.backup = ""
        self.map_name = ""
        self.preprocessed = False
        self.data = None
        self.prev_count = count_files(paths.akl_home.joinpath(".history"))
        self.costs = pd.DataFrame()
        self.validator = Validator(self.data, mode)
        self.to_process = False
        self.to_export = False
        self.has_missing = False

    @staticmethod
    def set_data(data_filepath, process_name, sheet_name=0):
        keep_cols = data_integrity_map[process_name]['init']
        _data = pd.read_excel(data_filepath,
                              sheet_name=sheet_name).iloc[:, :keep_cols]
        _data.columns = data_integrity_map[process_name]['names'][:keep_cols]
        _data = _data.dropna(subset=DATA_DROP, how="all")

        return _data

    def _preprocess(self):
        pass

    def get_cost(self, region: str, material: str, quantity: int = None):
        pass

    def process(self):
        pass

    def _check_next_idx(self, index, column):
        try:
            return self.data.loc[index, column] == self.data.loc[
                index + 1, column]
        except KeyError:
            return False

    def get_minimum(self, region: str):
        try:
            if region == "ΕΞΑΓΩΓΗ":
                return 0.00
            else:
                return round2(self.costs.loc[region, elaxisti])
        except KeyError:
            return 0.00

    def validate(self):
        self.to_process = self.validator.columns(self.map_name)
        if self.to_process:
            self.has_missing = self.validator.missing()

        self.log.add_message(self.validator.log.get_raw())

    def process_per_client(self, last_sort_element=paradosi):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            same_name = self._check_next_idx(i.Index, pelatis)

            same_date = self._check_next_idx(i.Index, imerominia)

            same_region = self._check_next_idx(i.Index, tomeas)

            same_delivery = self._check_next_idx(i.Index, last_sort_element)

            same_loading = self._check_next_idx(i.Index, apostoli)

            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας)

            if all([same_name, same_date, same_region,
                    same_delivery, same_loading]):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    whole = round2(sum(hold))

                    if whole > minimum:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, final_charge] = value
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

        self.to_export = True

    def export(self):
        if self.to_export:
            self.log("Creating excel files...", Display.INFO)
            self.data.to_excel(self.output, index=False)
            backup_title = paths.akl_home.joinpath(
                f".history\\{self.prev_count:0>5}-{timestamp()}-{self.backup}")

            try:
                self.data.to_excel(backup_title, index=False)
            except FileNotFoundError:
                display_error("Backup failed")

            self.log(f"Exported file: {self.output}", Display.INFO)
            self.log(f"Backup file: {backup_title}\n", Display.INFO)

            return str(backup_title)
