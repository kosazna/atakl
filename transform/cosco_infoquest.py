# -*- coding: utf-8 -*-

from atakl.transform.template import *


class CoscoInfoquest(TypeTemplate):
    def __init__(self,
                 data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Cosco"
        self.label = "Infoquest"
        self.map_name = f"{self.name} - {self.label}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator = Validator(self.data, self.map_name, mode)

        self.except_areas = pd.read_excel(self.cost_file,
                                          sheet_name="Cosco-Special Areas")
        self.kuklades_exceptions = self.except_areas["ΚΥΚΛΑΔΕΣ"].tolist()

    def _get_special_cost(self):
        pass

    def get_cost(self, region: str, material: str, quantity: int = None, subregion=None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00

        if material == kuviko_metro:
            try:
                if region in ("ΑΤΤΙΚΗ", "Ν.ΘΕΣΣΑΛΟΝΙΚΗΣ"):
                    if quantity < 8:
                        return round2(self.costs.loc[region, ogkos_small] * quantity)
                    elif 8 <= quantity <= 16:
                        return round2(self.costs.loc[region, ogkos_medium] * quantity)
                    elif quantity > 16:
                        return round2(self.costs.loc[region, ogkos_large] * quantity)
                    else:
                        return 0.0
                elif region == "ΚΥΚΛΑΔΕΣ":
                    found_exception = False

                    for area in self.kuklades_exceptions:
                        if area in subregion:
                            found_exception = True
                            break

                    if found_exception:
                        return round2(self.costs.loc[region, kuviko_eidiki_xreosi] * quantity)
                    else:
                        return round2(self.costs.loc[region, kuviko_metro] * quantity)
                else:
                    return round2(self.costs.loc[region, kuviko_metro] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _preprocess(self):
        self.data[sunolika_temaxia] = self.data[sunolika_temaxia].fillna(
            0).astype(int)
        self.data[sinolikos_ogkos] = self.data[sinolikos_ogkos].fillna(
            0.0).astype(float)
        self.data[kivotia_under_007] = self.data[kivotia_under_007].fillna(
            0).astype(int)
        self.data[ogkos_over_007] = self.data[ogkos_over_007].fillna(
            0.0).astype(float)

        self.data[perioxi] = self.data[perioxi].fillna("<NULL>")

        self.preprocessed = True

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []
        separate = False

        for i in self.data.itertuples():
            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας)
            maximum = self.get_maximum(i.Γεωγραφικός_Τομέας)

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                if i.Συνολική_Χρέωση > maximum:
                    self.data.loc[i.Index, final_charge] = maximum
                    separate = True
                else:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    whole = round2(sum(hold))

                    if separate:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, final_charge] = value
                    elif whole > maximum:
                        if insert_into == 'last':
                            self.data.loc[i.Index, final_charge] = maximum
                        else:
                            _position = hold.index(max(hold))
                            _df_index = hold_idx[_position]
                            self.data.loc[_df_index, final_charge] = maximum
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
                    separate = False
                else:
                    if i.Συνολική_Χρέωση > maximum:
                        self.data.loc[i.Index, final_charge] = maximum
                    elif i.Συνολική_Χρέωση < minimum:
                        self.data.loc[i.Index, final_charge] = minimum
                    else:
                        self.data.loc[i.Index, final_charge] = i.Συνολική_Χρέωση

    def process(self):
        auth = Authorize(self.map_name, self.log)

        if auth.user_is_licensed():
            self._preprocess()

            self.log("Processing...", Display.INFO)

            stock1 = self.data.apply(lambda x: self.get_cost(x[tomeas],
                                                            c_2space(
                                                                kivotia_under_007),
                                                            x[kivotia_under_007]),
                                    axis=1)

            stock2 = self.data.apply(lambda x: self.get_cost(x[tomeas],
                                                            c_2space(
                                                                ogkos_over_007),
                                                            x[ogkos_over_007]),
                                    axis=1)

            self.data[stock_out_charge] = stock1 + stock2

            self.data['subregion'] = self.data[perioxi] + ' ' + self.data[paradosi_address]

            self.data[ogkos_dist_charge] = self.data.apply(lambda x: self.get_cost(x[tomeas],
                                                                                kuviko_metro,
                                                                                x[sinolikos_ogkos],
                                                                                x['subregion']), axis=1)

            self.data[total_charge] = self.data[ogkos_dist_charge]

            self.process_rows(insert_into='max')

            self.data[perioxi] = self.data[perioxi].replace("<NULL>", "")

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data.loc[self.data[kodikos_paraggelias].str.startswith(
                'PAL', na=False), final_charge] = 0.00

            self.data[final_dist_charge] = self.data[final_charge]

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                    Display.INFO)

            self.to_export = True
        else:
            self.log("Can't process data. Contact Support", Display.INFO)
