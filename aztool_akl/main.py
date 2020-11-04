# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

import sys
from aztool_akl.validate import *
from aztool_akl.transform import *

general_costs = ".templates\\Region_Costs.xlsx"
dt_mapper = {"1": {"data": "DB_Data\\Concepts.xlsx",
                   "tranformer": TypeOneTransformer},
             "2": {"data": "DB_Data\\PT Beverages-Spirits.xlsx",
                   "tranformer": TypeTwoTransformer},
             "3": {"data": "DB_Data\\PT Beverages-Lavazza.xlsx",
                   "tranformer": TypeThreeTransformer}
             }


def load_tranformer(_action: str):
    cwd = Path(sys.argv[1])

    _data = validate_path("File with the database data:\n")
    _costs = validate_path("File with costs per region:\n")

    data_path = cwd.joinpath(
        dt_mapper[_action]['data']) if _data is None else _data

    costs_path = cwd.joinpath(general_costs) if _costs is None else _costs

    _tranformer = dt_mapper[action]['tranformer'](data_filepath=data_path,
                                                  cost_filepath=costs_path)

    return _tranformer


if __name__ == "__main__":
    print("ATTIKH KINISI LOGISTICS S.A.\n\n")
    while True:
        action = validate_input("action")

        transformer = load_tranformer(action)

        transformer.process()
        transformer.export()
