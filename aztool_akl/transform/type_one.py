# -*- coding: utf-8 -*-

from aztool_akl.transform.template import *


class TypeOneTransformer(TypeTemplate):
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        super().__init__(data_filepath, cost_filepath)
        self.name = "Concepts"
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.working_dir = self.data_file.parent
        self.output = self.working_dir.joinpath(f"{self.name}.xlsx")
        self.backup = self.backup = f"{self.name}.xlsx"
        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            undercore2space(tomeas), drop=True)

    def get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                if material == paleta:
                    if region != 'ΑΤΤΙΚΗ':
                        return round2(
                            self.costs.loc[region, material] * quantity)
                    else:
                        if quantity >= 21:
                            return round2(175)
                        elif quantity >= 11:
                            return round2(quantity * 11.5)
                        elif quantity > 0:
                            return round2(quantity * 15)
                        else:
                            return 0.00
                else:
                    return round2(self.costs.loc[region, material] * quantity)
            except KeyError:
                return 0.00

    def _preprocess(self):
        self.data.columns = TYPE_ONE_COLUMNS[:12]
        self.data = self.data.sort_values(DATA_SORT).reset_index(drop=True)
        self.data[paletes] = self.data[paletes].fillna(0).astype(int)
        self.data[kivotia] = self.data[kivotia].fillna(0).astype(int)
        self.data[kola] = self.data[kola].fillna(0).astype(int)
        self.data[varelia] = self.data[varelia].fillna(0).astype(int)
        self.data[kena_varelia] = self.data[kena_varelia].fillna(0).astype(int)

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

        self.data[varelia_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], vareli, x[varelia]), axis=1)

        self.data[kena_varelia_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[tomeas], keno_vareli, x[kena_varelia]),
            axis=1)

        self.data[total_charge] = sum(
            [self.data[paletes_dist_charge],
             self.data[kivotia_dist_charge],
             self.data[varelia_dist_charge],
             self.data[kena_varelia_dist_charge]])

        self.process_per_client()

        self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

        self.data.loc[self.data[apostoli] == idiofortosi, final_charge] = 0.00

        self.data.columns = list(map(undercore2space, TYPE_ONE_COLUMNS))

        print(f"  -> Data Process Complete: [{self.data.shape[0]}] records\n")
