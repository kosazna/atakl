# -*- coding: utf-8 -*-

from atakl.transform.template import *


class Giochi(TypeTemplate):
    def __init__(self, data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Giochi"
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator.set_data(self.data)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _finalize_cost(self, region: str, charge: float):
        wall = round2(self.get_cost(region, paleta, 1))
        if charge > wall:
            return wall
        return charge

    def _preprocess(self):
        if self.to_process:
            keep = info_map[self.map_name]['init_ncols']
            self.data.columns = info_map[self.map_name]['akl_cols'][:keep]
            sort_rule = info_map[self.map_name]['sort']
            self.data = self.data.sort_values(sort_rule).reset_index(drop=True)

            self.data[paletes] = self.data[paletes].fillna(0).astype(int)
            self.data[ogkos] = self.data[ogkos].fillna(0.0).astype(float)

            self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

            self.preprocessed = True

    def process(self):
        self._preprocess()
        if self.preprocessed:
            self.log("Processing...", Display.INFO)

            self.data[paletes_dist_charge] = self.data.apply(
                lambda x: self.get_cost(x[tomeas], paleta, x[paletes]),
                axis=1)

            self.data[kivotia_lampades_dist_charge] = ''
            self.data[kivotia_paixnidia_dist_charge] = ''

            self.data[ogkos_dist_charge] = self.data.apply(
                lambda x: self.get_cost(x[tomeas], kuviko, x[ogkos]),
                axis=1)

            self.data[total_charge] = sum([self.data[paletes_dist_charge],
                                           self.data[ogkos_dist_charge]])

            self.process_rows()




            self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

            order = self.data[kodikos_paraggelias].str.split('-').str[
                    :-1].str.join('-')
            og_orger = self.data[kodikos_arxikis_paraggelias].str.split(
                '-').str[:-1].str.join('-')

            order_idsx = order.loc[order.isin(og_orger)].index
            og_orger_idxs = og_orger.loc[og_orger.isin(order)].index

            _charge = self.data.loc[order_idsx, final_charge]
            _multiplier = self.data.loc[og_orger_idxs, temaxia]

            to_replace = _charge * _multiplier

            self.data.loc[order_idsx, final_charge] = to_replace

            self.data.loc[
                self.data[apostoli] == idiofortosi, final_charge] = 0.00

            self.data[kola_dist_charge] = self.data[final_charge]
            self.data[strech] = ""

            self.data = self.data[info_map[self.map_name]['akl_cols']]

            self.data.columns = info_map[self.map_name]['formal_cols']

            self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                     Display.INFO)

            self.to_export = True
        else:
            self.log("Process did not execute due to errors.", Display.INFO)
