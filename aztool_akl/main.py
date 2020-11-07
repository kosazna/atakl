# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

import sys
import os
from aztool_akl.validate import *
from aztool_akl.transform import *
from aztool_akl.gui import *

general_costs = ".templates\\Region_Costs.xlsx"
dt_mapper = {"1": {"data": "DB_Data\\Concepts.xlsx",
                   "tranformer": TypeOneTransformer},
             "2": {"data": "DB_Data\\PT Beverages-Spirits.xlsx",
                   "tranformer": TypeTwoTransformer},
             "3": {"data": "DB_Data\\PT Beverages-Lavazza.xlsx",
                   "tranformer": TypeThreeTransformer}
             }

dt_gui_mapper = {"Concepts": {"data": "DB_Data\\Concepts.xlsx",
                              "tranformer": TypeOneTransformer},
                 "PT Beverages - Spirits": {
                     "data": "DB_Data\\PT Beverages-Spirits.xlsx",
                     "tranformer": TypeTwoTransformer},
                 "PT Beverages - Lavazza": {
                     "data": "DB_Data\\PT Beverages-Lavazza.xlsx",
                     "tranformer": TypeThreeTransformer}
                 }


def load_tranformer(_action: str, wd=None):
    cwd = Path(sys.argv[1]) if wd is None else wd

    _data = validate_path("File with the database data:\n")
    _costs = validate_path("File with costs per region:\n")

    data_path = cwd.joinpath(
        dt_mapper[_action]['data']) if _data is None else _data

    costs_path = cwd.joinpath(general_costs) if _costs is None else _costs

    _tranformer = dt_mapper[_action]['tranformer'](data_filepath=data_path,
                                                   cost_filepath=costs_path)

    return _tranformer


def gui_execute():
    _action = ui.get_process_action()
    data_path =
    costs_path =
    _tranformer = dt_mapper[_action]['tranformer'](data_filepath=data_path,
                                                   cost_filepath=costs_path)
    _tranformer.process()
    _tranformer.export()


def open_costs_excel(path):
    os.startfile(path)


if __name__ == "__main__":
    # print("ATTIKH KINISI LOGISTICS S.A.\n")
    while True:
        cwdir = Path(sys.argv[1])
        costs = cwdir.joinpath(general_costs)
        app = QtWidgets.QApplication(sys.argv)
        akl_windows = QtWidgets.QMainWindow()
        ui = Ui_akl_windows()
        ui.setupUi(akl_windows)
        # ui.process_data = gui_execute
        akl_windows.show()
        sys.exit(app.exec_())

        # print("=" * 40)
        # print("Choose an action:\n")
        #
        # action = validate_input("action")
        #
        # transformer = load_tranformer(action)
        #
        # transformer.process()
        # transformer.export()
