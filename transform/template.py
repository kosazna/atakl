# -*- coding: utf-8 -*-

import pandas as pd
from atakl.utilities import *
from atakl.validate.data import Validator


class TypeTemplate:
    def __init__(self, data_filepath,
                 cost_filepath: Union[str, Path],
                 mode='GUI'):
        self.data_file = Path(parse_xlsx(data_filepath)[0])
        self.cost_file = Path(cost_filepath)
        self.costs = pd.DataFrame()

        self.log = Display(mode)
        self.validator = Validator(mode=mode)

        self.prev_count = count_files(paths.akl_home.joinpath(".history"))

        self.data = None

        self.output = None
        self.backup = None
        self.map_name = None
        self.sheet_name = None

        self.preprocessed = False
        self.to_process = False
        self.to_export = False
        self.has_missing = False

    def set_data(self, data_filepath, process_name):
        keep_cols = info_map[process_name]['init_ncols']

        _db, _sheet = parse_xlsx(data_filepath)
        self.sheet_name = _sheet

        _data = pd.read_excel(_db, sheet_name=_sheet)
        nrows, ncols = _data.shape

        if nrows != 0 and ncols != 0:
            if ncols >= keep_cols:
                _data = _data.iloc[:, :keep_cols]
                _data.columns = info_map[process_name]['formal_cols'][
                                :keep_cols]
                _data = _data.dropna(subset=info_map[self.map_name]['drop'],
                                     how="all")
                return _data
            else:
                self.log("There are less than necessary columns in data.",
                         Display.ERROR)
                return None
        else:
            self.log("There are no data in the specified excel or sheet.\n"
                     "      Check the data file again or make sure\n"
                     "      you entered the correct sheet name.",
                     Display.INFO)
            return None

    def _preprocess(self):
        pass

    def get_cost(self, *args, **kwargs):
        pass

    def process(self):
        pass

    def _check_next_idx(self, index, column):
        try:
            return self.data.loc[index, column] == self.data.loc[
                index + 1, column]
        except KeyError:
            return False

    def _check_idxs(self, index, cols: list):
        bools = []
        for col in cols:
            idx1 = self.data.loc[index, col]
            try:
                idx2 = self.data.loc[index + 1, col]
            except KeyError:
                idx2 = None

            bools.append(idx1 == idx2)

        return all(bools)

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

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας)

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
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
                        if insert_into == 'last':
                            self.data.loc[i.Index, final_charge] = minimum
                        else:
                            _position = hold.index(max(hold))
                            _df_index = hold_idx[_position]
                            self.data.loc[_df_index, final_charge] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

    def export(self, output=None):
        if self.to_export:
            self.log("Saving data...", Display.INFO)

            if self.sheet_name == 0 or self.sheet_name is None:
                sheet_name = 'Τιμολόγηση'
            else:
                sheet_name = f'Τιμολόγηση_{self.sheet_name}'

            if output is None:
                if not self.output:
                    with pd.ExcelWriter(self.data_file,
                                        engine='openpyxl',
                                        mode='a') as xlsx:
                        self.data.to_excel(xlsx, sheet_name=sheet_name,
                                           index=False)

                    self.log(
                        f"Appended new sheet '{sheet_name}' to original data",
                        Display.INFO)
                else:
                    self.data.to_excel(self.output,
                                       sheet_name=sheet_name,
                                       index=False)
                    self.log(f"Exported file: {self.output}", Display.INFO)
            else:
                with pd.ExcelWriter(output,
                                    mode='a') as xlsx:
                    self.data.to_excel(xlsx, sheet_name=sheet_name,
                                       index=False)

                self.log(
                    f"Appended new sheet '{sheet_name}' to original data",
                    Display.INFO)
        else:
            self.log("Can't export data. No processing was performed",
                     Display.INFO)

    def create_backup(self):
        backup_dir = paths.akl_home.joinpath(".history")
        backup_id = str(self.prev_count).zfill(5)
        backup_title = backup_dir.joinpath(
            f"{backup_id} - {datestamp()} - {self.backup}")

        if backup_dir.exists():
            self.data.to_excel(backup_title, index=False)

            self.log(f"Backup file: {backup_title}\n", Display.INFO)

            return str(backup_title)
        return 'None'
