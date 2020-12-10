# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

from atakl.transform import *
from atakl.utilities import *
from atakl.validate import *


if __name__ == "__main__":
    import sys

    try:
        mode = sys.argv[1]
    except IndexError:
        mode = "CMD"

    if mode == 'CMD':
        print("ATTIKH KINISI LOGISTICS S.A.\n")

        while True:
            print("=" * 40)
            print("Choose an action:\n")

            action = validate_input("action")

            transformer = load_tranformer(action)
            transformer.validate()

            transformer.process()
            transformer.export()
    elif mode == 'POR':
        process = sys.argv[2]
        costs = sys.argv[3]
        db_data = sys.argv[4]
        out = sys.argv[5]
    elif mode == "GUI":
        from atakl.gui import *

        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()

        ui = UiAKL(main_window)
        ui.set_essential_data(paths=paths, transformer_map=transformer_mapper)

        main_window.show()
        sys.exit(app.exec_())
    else:
        pass
