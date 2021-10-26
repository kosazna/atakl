# -*- coding: utf-8 -*-

from re import sub
from atakl.transform.template import *


class Siganos(TypeTemplate):
    def __init__(self,
                 data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Siganos"
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator = Validator(self.data, self.map_name, mode)

        self.check_data = None

    def get_cost(self, region: str, material: str, quantity: int = None,
                 client_name: str = None, subregion: str = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        elif region == "ΑΤΤΙΚΗ" and material == paleta_dist_charge and "ΣΙΓΑΝΟΣ" in client_name and "ΠΑΡΑΣΚΕΥΗ" in subregion:
            if quantity > 10:
                return 140
            elif 5 <= quantity <= 9:
                return quantity * 14
            else:
                return quantity * 16
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(f"'Γεωγραφικός Τομέας' null value.", Display.ERROR)
                return 0.00

    def _preprocess(self):
        self.data[paletes] = self.data[paletes].fillna(0).astype(int)
        self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
        self.data[temaxia] = self.data[temaxia].fillna(0).astype(int)

        self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

        self.preprocessed = True

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []
        hold_kivs = []
        hold_pals = []
        ksila = []
        maximums = []

        for i in self.data.itertuples():
            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας)
            maximum = self.get_cost(i.Γεωγραφικός_Τομέας,
                                    paleta_dist_charge,
                                    1,
                                    i.Επωνυμία_Πελάτη,
                                    i.Περιοχή_Παράδοσης)

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
                hold_kivs.append(i.Χρέωση_Διανομής_Κιβωτίου)
                hold_pals.append(i.Χρέωση_Διανομής_Παλέτας)
                ksila.append(i.ksila)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)
                    hold_kivs.append(i.Χρέωση_Διανομής_Κιβωτίου)
                    hold_pals.append(i.Χρέωση_Διανομής_Παλέτας)
                    ksila.append(i.ksila)

                    whole = round2(sum(hold))
                    whole_kivs = round2(sum(hold_kivs))

                    if whole_kivs > maximum:
                        max_ksila = max(ksila)
                        _position = ksila.index(max_ksila)
                        _df_index = hold_idx[_position]
                        self.data.loc[_df_index,
                                      final_charge] = max_ksila * maximum
                    elif whole < minimum:
                        if insert_into == 'last':
                            self.data.loc[i.Index, final_charge] = minimum
                        else:
                            _position = hold.index(max(hold))
                            _df_index = hold_idx[_position]
                            self.data.loc[_df_index, final_charge] = minimum
                    else:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, final_charge] = value

                    hold_idx = []
                    hold = []
                    hold_kivs = []
                    hold_pals = []
                    ksila = []
                else:
                    if i.Χρέωση_Διανομής_Κιβωτίου > maximum:
                        self.data.loc[i.Index, final_charge] = maximum * i.ksila
                    elif i.Συνολική_Χρέωση < minimum:
                        self.data.loc[i.Index, final_charge] = minimum
                    else:
                        self.data.loc[i.Index, final_charge] = i.Συνολική_Χρέωση

    def process(self):
        self._preprocess()

        self.log("Processing...", Display.INFO)
        self.log()

        temaxia_values = self.data[[
            kodikos_arxikis_paraggelias, temaxia]].copy()
        temaxia_values = temaxia_values.rename(columns={kodikos_arxikis_paraggelias: 'og',
                                                        temaxia: 'ksila'})

        self.data = self.data.merge(
            temaxia_values, how='left', left_on=kodikos_paraggelias, right_on='og')
        self.data['ksila'] = self.data['ksila'].fillna(0).astype(int)

        self.data[paletes_dist_charge] = self.data.apply(
            lambda x: self.get_cost(
                x[tomeas], paleta_dist_charge, x[paletes], x[pelatis],
                x[paradosi]),
            axis=1)

        self.data[kivotia_dist_charge] = self.data.apply(
            lambda x: self.get_cost(
                x[tomeas], kivotia_costs_dist_charge, x[kivotia], x[pelatis],
                x[paradosi]),
            axis=1)

        self.data[total_charge] = self.data[paletes_dist_charge] + \
            self.data[kivotia_dist_charge]

        self.process_rows(insert_into='max')

        self.data.loc[
            self.data[apostoli] == idiofortosi, final_charge] = 0.00

        self.data.loc[self.data[kodikos_paraggelias].str.startswith(
            'PAL', na=False), final_charge] = 0.00

        self.data[kola_dist_charge] = self.data[final_charge]
        self.data[strech] = ''

        self.check_data = self.data.copy()

        self.data = self.data[info_map[self.map_name]['akl_cols']]

        self.data.columns = info_map[self.map_name]['formal_cols']

        self.log()

        self.log(f"Data Process Complete: [{self.data.shape[0]}] records",
                 Display.INFO)

        self.to_export = True
