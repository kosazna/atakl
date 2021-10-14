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
        elif region == "ΑΤΤΙΚΗ" and material == paleta_dist_charge and "ΣΙΓΑΝΟΣ" in client_name and "ΑΓΙΑ ΠΑΡΑΣΚΕΥΗ" in subregion:
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

    def process_pals(self):
        for i in self.data.itertuples():
            pals = i.ksila
            pal_cost = self.get_cost(i.Γεωγραφικός_Τομέας,
                                     paleta_dist_charge,
                                     pals,
                                     i.Επωνυμία_Πελάτη,
                                     i.Περιοχή_Παράδοσης)
            if i.Χρέωση_Διανομής_Κιβωτίου > i.Χρέωση_Διανομής_Παλέτας:

                self.data.loc[i.Index, final_charge] = pal_cost
                pals = i.Ατόφια_Παλέτα
                if pals > 0:
                    kivs = i.Κιβώτια

                    pal_cost = self.get_cost(i.Γεωγραφικός_Τομέας,
                                             paleta_dist_charge,
                                             pals)

                    if kivs == 0:
                        self.data.loc[i.Index, final_charge] = pal_cost
                    else:
                        self.data.loc[i.Index, final_charge] = 0
                        self.log(f"Row: {i.Index + 2} -> Κιβώτια: {kivs}",
                                 Display.WARNING)

    def process(self):
        auth = Authorize(self.map_name, self.log)

        if auth.user_is_licensed():
            self._preprocess()

            self.log("Processing...", Display.INFO)
            self.log()

            temaxia_values = self.data[[
                kodikos_arxikis_paraggelias, temaxia]].copy()
            temaxia_values = temaxia_values.rename(columns={kodikos_arxikis_paraggelias: 'og',
                                                            temaxia: 'ksila'})

            self.data = self.data.merge(
                temaxia_values, left_on=kodikos_paraggelias, right_on='og')

            self.data[paletes_dist_charge] = self.data.apply(
                lambda x: self.get_cost(
                    x[tomeas], paleta_dist_charge, x[paletes], x[pelatis],
                    x[perioxi]),
                axis=1)

            self.data[kivotia_dist_charge] = self.data.apply(
                lambda x: self.get_cost(
                    x[tomeas], kivotia_costs_dist_charge, x[kivotia], x[pelatis],
                    x[perioxi]),
                axis=1)

            self.data[total_charge] = self.data[paletes_dist_charge] + \
                self.data[kivotia_dist_charge]

            self.process_rows(insert_into='max')

            self.process_pals()

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data.loc[self.data[kodikos_paraggelias].str.startswith(
                'PAL', na=False), final_charge] = 0.00

            self.data[final_dist_charge] = self.data[final_charge]

            self.check_data = self.data.copy()

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log()

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Can't process data. Contact Support", Display.INFO)
