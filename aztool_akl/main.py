# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

import sys
from aztool_akl.validate import *
from aztool_akl.transform import *


if __name__ == "__main__":
    print("ATTIKH KINISI LOGISTICS S.A.\n\n")

    action = validate_input("action")

    if action == "1":
        working_dir = Path(sys.argv[1])

        _data = validate_path("File with the database data:\n")
        costs = validate_path("File with costs per region:\n")

        data_path = working_dir.joinpath(
            "DB_Data.xlsx") if _data is None else _data

        costs_path = working_dir.joinpath(
            ".templates\\Region_Costs.xlsx") if costs is None else costs

        tranformer = TypeOneTransformer(data_filepath=data_path,
                                        cost_filepath=costs_path)
        tranformer.process()
        tranformer.export()
