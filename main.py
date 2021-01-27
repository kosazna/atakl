# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

from atakl.transform import *
from atakl.validate import *
import warnings

warnings.filterwarnings('ignore')


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
            backup_file = transformer.create_backup()
            print(backup_file)
    elif mode == 'POR':
        por_log = Display(mode)

        process = str(sys.argv[2])

        costs = Path(sys.argv[3])
        db_data = sys.argv[4]

        try:
            _out = sys.argv[5]
            if _out:
                out = Path(sys.argv[5])
            else:
                out = ""
        except IndexError:
            out = ""

        try:
            transformer = load_tranformer(process,
                                          mode=mode,
                                          path_list=[costs,
                                                     db_data,
                                                     out])
            transformer.validate()

            transformer.process()
            transformer.export()
        except Exception as e:
            por_log(e)
            text = por_log.get_content()
        else:
            text = f"AKL v{AKL_VERSION}\n" \
                   f"Datetime: {dtstamp()}\n" \
                   f"Process called: {transformer.map_name}\n\n" \
                   f"{transformer.log.get_content()}"

        with open(paths.logger, 'w') as f:
            f.write(text)

    elif mode == "GUI":
        from atakl.gui import *

        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()

        ui = AKLUI(main_window)
        ui.set_essential_data(paths=paths, transformer_map=transformer_mapper)

        main_window.show()
        sys.exit(app.exec_())
    else:
        pass
