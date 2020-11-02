# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from aztool_akl.schemas import *
from aztool_akl.validate.data import TypeOneValidator


class TypeTwoTransformer:
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        self.name = "PT Beverages - Spirits"
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.working_dir = self.data_file.parent
        self.output = self.working_dir.joinpath("Processed_Data.xlsx")
        self.preprocessed = False
        self.data = pd.read_excel(self.data_file).sort_values(DATA_SORT).dropna(
            subset=[undercore2space(pelatis)]).reset_index(drop=True)
        self.costs = pd.read_excel(self.cost_file).set_index(
            undercore2space(tomeas), drop=True)
        self.data.columns = TYPE_ONE_COLUMNS[:12]
        self.validator = TypeOneValidator(self.data)

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
                            return quantity * 9
                        elif quantity >= 11:
                            return quantity * 12
                        elif quantity > 0:
                            return quantity * 13
                        else:
                            return 0
                else:
                    return self.costs.loc[region, material] * quantity
            except KeyError:
                return 0

    def _preprocess(self):
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

        self.data[paletes_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], paleta, x[paletes]), axis=1)

        self.data[kivotia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], kivotio, x[kivotia]), axis=1)

        self.data[varelia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], vareli, x[varelia]), axis=1)

        self.data[kena_varelia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], keno_vareli, x[kena_varelia]),
            axis=1)

    def export(self):
        self.data.to_excel(self.output, index=False)
        print(f"  -> Exported file: {self.output}\n\n\n\n")
