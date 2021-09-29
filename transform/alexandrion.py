# -*- coding: utf-8 -*-

from atakl.transform.template import *


class Alexandrion(TypeTemplate):
    def __init__(self,
                 data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Alexandrion"
        self.label = ""
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator = Validator(self.data, self.map_name, mode)

        self.except_sheet = pd.read_excel(self.cost_file,
                                          sheet_name="Alexandrion-Special Areas")

        self.except_areas = self._make_exceptions()

    def _make_exceptions(self):
        exceptions = {}
        for col in self.except_sheet.columns:
            region, cat = col.split('_')
            _unique = self.except_sheet[col].tolist()
            unique = list(filter(lambda elm: isinstance(elm, str), _unique))
            if region in exceptions:
                exceptions[region][int(cat)] = unique
            else:
                exceptions[region] = {int(cat): unique}

        return exceptions

    def _area_props(self, region, subregion):
        if region in self.except_areas:
            found_exception = False
            for area, cat_areas in self.except_areas.items():
                for cat_id, subareas in cat_areas.items():
                    for subarea in subareas:
                        if subarea in subregion:
                            _area = area
                            _cat_id = cat_id
                            found_exception = True
            if found_exception:
                return (_area, _cat_id)
            return (region, 0)
        else:
            return (region, 0)

    def get_cost(self, region: str, material: str, quantity: int = None, subregion=None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00

        try:
            area, area_cat = self._area_props(region, subregion)

            c = self.costs.loc[(self.costs.index == area) & (
                self.costs["Κατηγορία Περιοχής"] == area_cat), material]

            return round2(c * quantity)
        except KeyError as e:
            self.log(e, Display.ERROR)
            return 0.00

    def get_minimum(self, region: str, subregion: str):
        try:
            area, area_cat = self._area_props(region, subregion)

            c = self.costs.loc[(self.costs.index == area) & (
                self.costs["Κατηγορία Περιοχής"] == area_cat), elaxisti].values[0]

            return c
        except KeyError:
            return 0.00

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []
        ksila_pals = []
        kiv_charge = []

        for i in self.data.itertuples():
            minimum = self.get_minimum(
                i.Γεωγραφικός_Τομέας, i.Περιοχή_Παράδοσης)
            maximum = round2(self.get_cost(i.Γεωγραφικός_Τομέας,
                          paleta, 1, i.Περιοχή_Παράδοσης))

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
                ksila_pals.append(i.ksila)
                kiv_charge.append(i.Χρέωση_Κιβωτίων)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)
                    ksila_pals.append(i.ksila)
                    kiv_charge.append(i.Χρέωση_Κιβωτίων)

                    whole = round2(sum(hold))
                    whole_kiv = round2(sum(kiv_charge))

                    if whole_kiv > maximum:
                        sum_ksila = sum(ksila_pals)
                        if sum_ksila != 0:
                            multiplier = max(ksila_pals)
                            _index = ksila_pals.index(multiplier)
                            _df_index = hold_idx[_index]
                            self.data.loc[_df_index, final_charge] = maximum * multiplier
                        else:
                            self.log(f"Maybe missing PAL order - {i.Index}")
                            self.data.loc[i.Index, final_charge] = maximum
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
                    ksila_pals = []
                    kiv_charge = []
                else:
                    if i.Χρέωση_Κιβωτίων > maximum:
                        self.data.loc[i.Index, final_charge] = maximum * i.ksila
                    elif i.Συνολική_Χρέωση < minimum:
                        self.data.loc[i.Index, final_charge] = minimum
                    else:
                        self.data.loc[i.Index, final_charge] = i.Συνολική_Χρέωση

    def _preprocess(self):
        self.data[paletes] = self.data[paletes].fillna(0).astype(int)
        self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
        self.data[temaxia] = self.data[temaxia].fillna(0).astype(int)

        self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

        self.preprocessed = True

    def process_pals(self):
        for i in self.data.itertuples():
            wall = round2(self.get_cost(i.Γεωγραφικός_Τομέας,
                          paleta, 1, i.Περιοχή_Παράδοσης))

            if i.Τελική_Χρέωση > wall:
                try:
                    c = self.data.loc[self.data[kodikos_arxikis_paraggelias]
                                      == i.Κωδικός_Παραγγελίας, ksila_paleton].values[0]
                except IndexError:
                    c = 0

                if c:
                    self.data.loc[i.Index, final_charge] = c * wall

    def process(self):
        auth = Authorize(self.map_name, self.log)

        if auth.user_is_licensed():
            self._preprocess()

            self.log("Processing...", Display.INFO)

            pals = self.data.loc[self.data[kodikos_paraggelias].str.startswith(
                "PAL")][[kodikos_arxikis_paraggelias, ksila_paleton]]
            pals = pals.rename(columns={kodikos_arxikis_paraggelias: 'kodikos',
                                        ksila_paleton: 'ksila'})

            self.data = self.data.merge(pals,
                                        how="left",
                                        left_on=kodikos_paraggelias,
                                        right_on='kodikos').drop("kodikos", axis=1)

            self.data['ksila'] = self.data['ksila'].fillna(0).astype(int)

            # ckiv = self.data.apply(lambda x: self.get_cost(x[tomeas],
            #                                                kivotio,
            #                                                x[kivotia],
            #                                                x[paradosi]),
            #                        axis=1)

            # cpal = self.data.apply(lambda x: self.get_cost(x[tomeas],
            #                                                paleta,
            #                                                x[paletes],
            #                                                x[paradosi]),
            #                        axis=1)

            self.data[kivotia_charge] = self.data.apply(lambda x: self.get_cost(x[tomeas],
                                                           kivotio,
                                                           x[kivotia],
                                                           x[paradosi]),
                                   axis=1)
            self.data[paletes_charge] = self.data.apply(lambda x: self.get_cost(x[tomeas],
                                                           paleta,
                                                           x[paletes],
                                                           x[paradosi]),
                                   axis=1)

            self.data[total_charge] = self.data[kivotia_charge] + self.data[paletes_charge]

            self.process_rows(insert_into='max')
            # self.process_pals()

            self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")
            self.data[strech] = ''

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data.loc[self.data[kodikos_paraggelias].str.startswith(
                'PAL', na=False), final_charge] = 0.00

            self.data[kola_dist_charge] = self.data[final_charge]

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Can't process data. Contact Support", Display.INFO)
