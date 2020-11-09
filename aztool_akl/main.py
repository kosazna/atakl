# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)


from aztool_akl.gui import *
from aztool_akl.transform import *
from aztool_akl.utilities import *
from aztool_akl.validate import *


transformer_mapper = {
    "Concepts": TypeOneTransformer,
    "PT Beverages - Spirits": TypeTwoTransformer,
    "PT Beverages - Lavazza": TypeThreeTransformer}


def load_tranformer(_action: str):
    _data = validate_path("File with the database data:\n")
    _costs = validate_path("File with costs per region:\n")

    if _data is None:
        data_path = paths.default_path_mapper[_action]
    else:
        paths.user_path_mapper[_action] = _data
        data_path = _data

    if _costs is None:
        costs_path = paths.default_costs
    else:
        paths.user_costs = _costs
        costs_path = _costs

    _tranformer = transformer_mapper[_action](data_filepath=data_path,
                                              cost_filepath=costs_path)

    return _tranformer


if __name__ == "__main__":
    import sys

    try:
        mode = sys.argv[1]
    except IndexError:
        mode = "GUI"

    if mode == 'CMD':
        print("ATTIKH KINISI LOGISTICS S.A.\n")

        while True:
            print("=" * 40)
            print("Choose an action:\n")

            action = validate_input("action")

            transformer = load_tranformer(action)

            transformer.process()
            transformer.export()
    else:
        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()

        ui = UiAKL(main_window)
        ui.set_home(paths.akl_home)
        ui.set_default_costs(paths.default_costs)
        ui.set_default_path_mapper(paths.default_path_mapper)
        ui.set_default_export_path_mapper(paths.default_export_path_mapper)
        ui.set_transformers(transformer_mapper)
        ui.init_paths()

        main_window.show()
        sys.exit(app.exec_())
