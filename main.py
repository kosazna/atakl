# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

from atakl.transform import *
from atakl.validate import *


if __name__ == "__main__":
    import sys

    try:
        mode = str(sys.argv[1])
    except IndexError:
        mode = "GUI"

    if mode == 'CMD':
        print("ATTIKH KINISI LOGISTICS S.A.\n")

        while True:
            print("=" * 40)
            print("Choose an action:\n")

            action = validate_input("action")

            transformer = load_tranformer(action, mode=mode)
            transformer.validate()

            transformer.process()
            transformer.export()
    elif mode == 'POR':
        process = str(sys.argv[2])

        costs = Path(sys.argv[3])
        db_data = Path(sys.argv[4])
        out = Path(sys.argv[5])

        transformer = load_tranformer(process,
                                      mode=mode,
                                      path_list=[costs,
                                                 db_data,
                                                 out])
        transformer.validate()

        transformer.process()
        transformer.export()
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
