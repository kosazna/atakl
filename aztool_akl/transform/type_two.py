# -*- coding: utf-8 -*-

from aztool_akl.transform.template import *


class TypeTwoTransformer(TypeTemplate):
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        super().__init__(data_filepath, cost_filepath)
        self.name = "PT Beverages"
        self.label = "Spirits"
        self.output = self.working_dir.joinpath(
            f"CHARGES_{self.name}-{self.label}.xlsx")
        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            undercore2space(tomeas), drop=True)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                if material == paleta or material == mixani:
                    if region != 'ΑΤΤΙΚΗ':
                        return round2(
                            self.costs.loc[region, material] * quantity)
                    else:
                        if quantity >= 21:
                            return round2(quantity * 9)
                        elif quantity >= 11:
                            return round2(quantity * 12)
                        elif quantity > 0:
                            return round2(quantity * 13)
                        else:
                            return 0.0
                else:
                    return round2(self.costs.loc[region, material] * quantity)
            except KeyError:
                return 0.00

    def _finalize_cost(self, region: str, charge: float):
        wall = round2(self.get_cost(region, paleta, 1))
        if charge > wall:
            return wall
        return charge

    def _preprocess(self):
        self.data.columns = TYPE_TWO_COLUMNS[:17]
        self.data = self.data.sort_values(DATA_SORT).reset_index(drop=True)
        self.data[paletes] = self.data[paletes].fillna(0).astype(int)
        self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
        self.data[tsantes] = self.data[tsantes].fillna(0).astype(int)
        self.data[temaxia] = self.data[temaxia].fillna(0).astype(int)
        self.data[varelia] = self.data[varelia].fillna(0).astype(int)
        self.data[ompreles] = self.data[ompreles].fillna(0).astype(int)
        self.data[paletes_san] = self.data[paletes_san].fillna(0).astype(int)
        self.data[kola] = self.data[kola].fillna(0).astype(int)

        self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

        self.preprocessed = True

    def process(self):
        if not self.preprocessed:
            self._preprocess()

        self.validator.validate()

        self.data[paletes_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], paleta, x[paletes]), axis=1)

        self.data[kivotia_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], kivotio, x[kivotia]), axis=1)

        self.data[tsantes_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], tsanta, x[tsantes]), axis=1)

        self.data[varelia_dist_charge] = 0.0

        self.data[ompreles_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], omprela, x[ompreles]), axis=1)

        self.data[kivotia_dist_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[kivotia_dist_charge]),
            axis=1)

        self.data[tsantes_dist_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[tsantes_dist_charge]),
            axis=1)

        self.data[ompreles_dist_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[ompreles_dist_charge]),
            axis=1)

        self.data[total_charge] = sum(
            [self.data[paletes_dist_charge],
             self.data[kivotia_dist_charge],
             self.data[varelia_dist_charge],
             self.data[tsantes_dist_charge],
             self.data[ompreles_dist_charge]])

        self.process_per_client()

        self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

        self.data.loc[self.data[apostoli] == idiofortosi, final_charge] = 0.00

        self.data.columns = list(map(undercore2space, TYPE_TWO_COLUMNS))

        print(f"  -> Data Process Complete: [{self.data.shape[0]}] records\n")
