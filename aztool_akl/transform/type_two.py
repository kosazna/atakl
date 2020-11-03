# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from aztool_akl.schemas import *
from aztool_akl.validate.data import TypeOneValidator
from aztool_akl.transform.type_template import TypeTemplate


class TypeTwoTransformer(TypeTemplate):
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        super().__init__(data_filepath, cost_filepath)
        self.name = "PT Beverages"
        self.label = "Spirits"
        self.output = self.working_dir.joinpath(
            f"{self.name}-{self.label}_Processed.xlsx")
        self.preprocessed = False
        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            undercore2space(tomeas), drop=True)
        self.data.columns = TYPE_TWO_COLUMNS[:17]
        # self.validator = TypeOneValidator(self.data)

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

    def _finalize_cost(self, region: str, charge: float):
        wall = self._get_cost(region, paleta, 1)
        if charge > wall:
            return wall
        return charge

    def _minimum_charge(self, region: str, charge: float):
        minimum = self._get_cost(region, elaxisti)
        if charge > minimum:
            return charge
        return minimum

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

        # self.validator.validate()

        self.data[paletes_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], paleta, x[paletes]), axis=1)

        self.data[kivotia_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], kivotio, x[kivotia]), axis=1)

        self.data[tsantes_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], tsanta, x[tsantes]), axis=1)

        self.data[varelia_charge] = 0.0

        self.data[ompreles_charge] = self.data.apply(
            lambda x: self._get_cost(x[tomeas], omprela, x[ompreles]), axis=1)

        self.data[kivotia_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[kivotia_charge]), axis=1)

        self.data[tsantes_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[tsantes_charge]), axis=1)

        self.data[ompreles_charge] = self.data.apply(
            lambda x: self._finalize_cost(x[tomeas], x[ompreles_charge]),
            axis=1)

        self.data[final_charge] = sum(
            [self.data[paletes_charge],
             self.data[kivotia_charge],
             self.data[varelia_charge],
             self.data[tsantes_charge],
             self.data[ompreles_charge]])

        self.data[final_charge] = self.data.apply(
            lambda x: self._minimum_charge(x[tomeas], x[final_charge]),
            axis=1)

        self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

        self.data.loc[self.data[apostoli] == idiofortosi, final_charge] = 0

        self.data.columns = list(map(undercore2space, TYPE_TWO_COLUMNS))

        print(f"  -> Data Process Complete: [{self.data.shape[0]}] records\n")