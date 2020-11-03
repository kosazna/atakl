# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from aztool_akl.schemas import *
from aztool_akl.transform.template import TypeTemplate


class TypeThreeTransformer(TypeTemplate):
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        super().__init__(data_filepath, cost_filepath)
        self.name = "PT Beverages"
        self.label = "Lavazza"
        self.output = self.working_dir.joinpath(
            f"CHARGES_{self.name}-{self.label}.xlsx")
        self.preprocessed = False
        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            undercore2space(tomeas), drop=True)
        self.data.columns = TYPE_TWO_COLUMNS[:17]
