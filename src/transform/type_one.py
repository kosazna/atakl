import pandas as pd
from pathlib import Path
from ..schemas import *
from ..validate.data import TypeOneValidator


class TypeOneTransformer:
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.working_dir = self.data_file.parent
        self.output = self.working_dir.joinpath("Processed_Data.xlsx")
        self.preprocessed = False
        self.data = pd.read_excel(self.data_file).sort_values(DATA_SORT).dropna(
            subset=[undercore2space(pelatis)]).reset_index(drop=True)
        self.costs = pd.read_excel(self.cost_file).set_index(tomeas, drop=True)
        self.data.columns = TYPE_ONE_COLUMNS[:12]
        self.validator = TypeOneValidator(self.data)

    def _check_next_idx(self, index, column):
        try:
            return self.data[index, column] == self.data[index + 1, column]
        except KeyError:
            return False

    def _get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0
        else:
            try:
                if quantity is None:
                    return self.costs.loc[region, material]

                if material == paleta:
                    if region != 'ΑΤΤΙΚΗ':
                        return self.costs.loc[region, material] * quantity
                    else:
                        if quantity >= 21:
                            return 175
                        elif quantity >= 11:
                            return quantity * 11.5
                        elif quantity > 0:
                            return quantity * 15
                        else:
                            return 0
                else:
                    return self.costs.loc[region, material] * quantity
            except KeyError:
                return 0

    def _preprocess(self):
        self.data[kena_varelia] = self.data[kena_varelia].fillna(0).astype(int)

        self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

        self.preprocessed = True

    def process(self):
        if not self.preprocessed:
            self._preprocess()

        self.validator.validate()

        self.data[paletes_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], paleta, x[paletes]), axis=1)

        self.data[kivotia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], kivotio, x[kivotia]), axis=1)

        self.data[varelia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], vareli, x[varelia]), axis=1)

        self.data[kena_varelia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], keno_vareli, x[kena_varelia]),
            axis=1)

        self.data[total_charge] = sum(
            [self.data[paletes_charge],
             self.data[kivotia_charge],
             self.data[varelia_charge],
             self.data[kena_varelia_charge]])

        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            same_name = self._check_next_idx(i.Index, pelatis)

            same_date = self._check_next_idx(i.Index, imerominia)

            same_region = self._check_next_idx(i.Index, tomeas)

            same_delivery = self._check_next_idx(i.Index, paradosi)

            minimum = self._get_cost(i.Γεωγραφικός_Τομέας, elaxisti)

            if all([same_name, same_date, same_region, same_delivery]):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    if sum(hold) > minimum:
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

        self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

        self.data.loc[self.data[apostoli] == idiofortosi, final_charge] = 0

        self.data.columns = TYPE_ONE_COLUMNS

        print(f"  -> Data Process Complete: [{self.data.shape[0]}] records\n")

    def export(self):
        self.data.to_excel(self.output, index=False)
        print(f"  -> Exported file: {self.output}\n\n\n\n")
