# -*- coding: utf-8 -*-

from atakl.transform.template import *


class GiochiCrate(TypeTemplate):
    def __init__(self, data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Giochi"
        self.label = "Crate"
        self.map_name = f"{self.name} - {self.label}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator = Validator(self.data, self.map_name, mode)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _preprocess(self):
        self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
        self.data[lampades] = self.data[lampades].fillna(0).astype(int)
        self.data[temaxia] = self.data[temaxia].fillna(0).astype(int)

        self.preprocessed = True

    def process(self):
        self._preprocess()
        self.log("Processing...", Display.INFO)

        self.data[total_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], kivotio, x[kivotia]),
            axis=1)

        self.process_rows()

        self.process_epinaulo()
        
        self.data[kivotio_charge] = self.data[final_charge]

        self.data = self.data[info_map[self.map_name]['akl_cols']]

        self.data.columns = info_map[self.map_name]['formal_cols']

        self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                 Display.INFO)

        self.to_export = True
