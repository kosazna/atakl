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
