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
        # process = validate_input("process")

        working_dir = Path(sys.argv[1])

        _data_path = validate_path("File with the database data:\n")
        _costs_path = validate_path("File with costs per region:\n")

        if _data_path is None:
            data_path = working_dir.joinpath("DB_Data.xlsx")
        else:
            data_path = _data_path

        if _costs_path is None:
            costs_path = working_dir.joinpath("templates\\Region_Costs.xlsx")
        else:
            costs_path = _costs_path

        tranformer = TypeOneTransformer(data_filepath=data_path,
                                        cost_filepath=costs_path)
        tranformer.process()
        tranformer.export()
