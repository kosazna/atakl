# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from atakl.gui.designer import *
from atakl.validate.input import validate_proper_and_existent_path
from atakl.utilities.utils import *


def show_popup(main_text, info='', icon=QMessageBox.Information):
    msg = QMessageBox()
    msg.setWindowTitle("AKL Dialog")
    msg.setText(main_text)
    msg.setIcon(icon)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)
    msg.setInformativeText(info)
    msg.exec_()


class AKLUI(Ui_designer):
    def __init__(self, window):
        self.setupUi(window)

        self.home_dir = ""
        self.default_costs = ""
        self.last_visited = None
        self.default_path_mapper = {}
        self.default_export_path_mapper = {}
        self.transformer_mapper = {}
        self.transformer = None

        self.user_costs = None
        self.user_data = None
        self.user_output = None

        self.browse_costs.clicked.connect(self.browse_costs_func)
        self.browse_db_data.clicked.connect(self.browse_db_data_func)
        self.browse_output.clicked.connect(self.browse_output_func)
        self.tick_default.stateChanged.connect(self.check_default_box)
        self.button_change_costs.clicked.connect(self.change_costs)
        self.process_list.currentIndexChanged.connect(
            self.change_paths_per_process)
        self.tick_export_new.stateChanged.connect(self.check_export_new)

        self.button_validate_data.clicked.connect(self.validate_data)

        self.button_process.clicked.connect(self.process_execute)

    def change_process_color(self, color):
        if color == 'yellow':
            self.button_process.setStyleSheet(
                "background-color: rgba(227, 209, 48, 0.8);\n"
                "color: rgb(72, 72, 72);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")
        elif color == 'green':
            self.button_process.setStyleSheet(
                "background-color: rgba(15, 196, 12, 0.8);\n"
                "color: rgb(72, 72, 72);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")
        else:
            self.button_process.setStyleSheet(
                "background-color: rgba(207, 14, 30, 0.8);\n"
                "color: rgb(72, 72, 72);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

    def set_essential_data(self, paths, transformer_map):
        self.set_home_dir(paths.akl_home)
        self.set_default_costs(paths.default_costs)
        self.set_default_path_mapper(paths.default_path_mapper)
        self.set_default_export_path_mapper(paths.default_export_path_mapper)
        self.set_transformers(transformer_map)
        self.gui_startup_paths(paths)

    def gui_startup_paths(self, paths):
        start_process = "Cavino"

        if paths.akl_home.exists():
            self.text_costs.setText(self.default_costs)

            try:
                self.text_db_data.setText(
                    self.default_path_mapper[start_process])
            except KeyError:
                self.text_db_data.setText("")
                self.text_output.setText("")
        else:
            self.tick_default.toggle()

    def get_last_visit(self):
        if self.last_visited is None:
            return self.home_dir
        return self.last_visited

    def set_last_visit(self, chosen_path):
        self.last_visited = str(Path(chosen_path).parent)

    def change_costs(self):
        if Path(self.default_costs).exists():
            startfile(self.default_costs)
        else:
            to_display = "Can't open costs file.\n" \
                         "AKL home directory is missing."
            self.text_general.setText(to_display)

    def set_home_dir(self, path):
        self.home_dir = str(path)

    def set_default_costs(self, path):
        self.default_costs = str(path)

    def set_default_path_mapper(self, path_mapper):
        self.default_path_mapper = {k: str(v) for k, v in
                                    path_mapper.items()}

    def set_default_export_path_mapper(self, path_mapper):
        self.default_export_path_mapper = {k: str(v) for k, v in
                                           path_mapper.items()}

    def set_transformers(self, mapper):
        self.transformer_mapper = mapper

    def validate_data(self):
        process = self.process_list.currentText()
        tranformer_process = self.transformer_mapper[process]
        costs_path = self.text_costs.text()
        db_data = self.text_db_data.text()
        output = self.text_output.text()

        db_file, sheet = parse_xlsx(db_data)

        db_exists = db_file.exists()
        db_ext = db_file.suffix

        costs_exists = Path(costs_path).exists()
        costs_ext = Path(costs_path).suffix

        accepted_exts = ['.xls', '.xlsx']

        if costs_ext in accepted_exts and db_ext in accepted_exts:

            if all([costs_exists, db_exists]):
                self.transformer = tranformer_process(data_filepath=db_data,
                                                      cost_filepath=costs_path,
                                                      output_path=output)

                if self.transformer.data is None:
                    self.text_records.setText('0')
                else:
                    self.text_records.setText(
                        str(self.transformer.data.shape[0]))

                self.transformer.validate()

                if self.transformer.to_process:
                    if self.transformer.has_missing:
                        self.change_process_color('yellow')
                    else:
                        self.change_process_color('green')

                self.text_general.setText(self.transformer.log.get_content())
                self.transformer.log.erase()
            else:
                to_display = f"Some of the input files are missing!\n" \
                             f"Check 'Costs' and 'DB_Data' files."
                self.text_general.setText(to_display)
        else:
            to_display = "Input files should end with either '.xls' or '.xlsx'"
            self.text_general.setText(to_display)

    def process_execute(self):
        if self.transformer is not None:
            if self.transformer.to_process:

                _old_txt = self.transformer.log.get_content()
                self.text_general.setText(_old_txt)

                self.transformer.process()
                self.transformer.export()

                _final_txt = _old_txt + "\n[Process Finished]"
                self.text_general.setText(_final_txt)

                self.text_backup.setText(self.transformer.create_backup())
                self.transformer.log.erase()
            else:
                self.text_general.setText("Can't process data.")
        else:
            self.text_general.setText("Validate data first!")

    def change_paths_per_process(self):
        process = self.process_list.currentText()
        if self.tick_default.isChecked():
            self.text_costs.setText(self.default_costs)

            try:
                self.text_db_data.setText(self.default_path_mapper[process])
                if self.tick_export_new.isChecked():
                    self.text_output.setText(
                        self.default_export_path_mapper[process])
                else:
                    self.text_output.setText("")
                    self.text_output.setPlaceholderText("")
            except KeyError:
                self.text_db_data.setText("")
                self.text_output.setText("")
        else:
            if self.user_costs is None:
                self.text_costs.setText("")
                self.text_costs.setPlaceholderText(
                    "Paste path here or browse...")
            else:
                self.text_costs.setText(self.user_costs)
            if self.user_data is None:
                self.text_db_data.setText("")
                self.text_db_data.setPlaceholderText(
                    "Paste path here or browse...")
            else:
                self.text_db_data.setText(self.user_data)
            if self.user_output is None:
                if self.tick_export_new.isChecked():
                    self.text_output.setText("")
                    self.text_output.setPlaceholderText(
                        "Paste path here or browse...")
                else:
                    self.text_output.setText("")
            else:
                self.text_output.setText(self.user_output)

        self.text_general.setText("")
        self.text_records.setText("")
        self.text_backup.setText("")

        self.change_process_color('red')

        self.transformer = None

    def browse_costs_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.get_last_visit())
        file_path = filename[0]
        if file_path:
            self.text_costs.setText(file_path)
            self.set_last_visit(file_path)
            self.user_costs = file_path

    def browse_db_data_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.get_last_visit())
        file_path = filename[0]
        if file_path:
            self.text_db_data.setText(file_path)
            self.set_last_visit(file_path)
            self.user_data = file_path

    def browse_output_func(self):
        filename = QFileDialog.getSaveFileName(directory=self.get_last_visit())
        file_path = filename[0]
        if file_path:
            export_file = str(validate_proper_and_existent_path(file_path))
            self.text_output.setText(export_file)
            self.user_output = export_file

    def check_export_new(self):
        process = self.process_list.currentText()
        if self.tick_export_new.isChecked():
            if self.tick_default.isChecked():
                self.text_output.setStyleSheet(
                    "background-color: rgb(209, 209, 209);\n"
                    "border-width:4px;\n"
                    "border-color:black;\n"
                    "border-style:offset;\n"
                    "border-radius:10px;")
                self.text_output.setText(
                    self.default_export_path_mapper[process])
            else:
                self.text_output.setStyleSheet(
                    "background-color: white;\n"
                    "border-width:4px;\n"
                    "border-color:black;\n"
                    "border-style:offset;\n"
                    "border-radius:10px;")

                if self.user_output is None:
                    self.text_output.setText("")
                    self.text_output.setPlaceholderText(
                        "Paste path here or browse...")
                else:
                    self.text_output.setText(self.user_output)

        else:
            self.text_output.setStyleSheet(
                "background-color: rgb(109, 109, 109);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")
            self.text_output.setText('')
            self.text_output.setPlaceholderText("")

        self.change_process_color('red')

        self.text_general.setText("")
        self.transformer = None

    def check_default_box(self):
        process = self.process_list.currentText()
        if self.tick_default.isChecked():
            self.text_costs.setStyleSheet(
                "background-color: rgb(209, 209, 209);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

            self.text_db_data.setStyleSheet(
                "background-color: rgb(209, 209, 209);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

            if self.tick_export_new.isChecked():
                self.text_output.setStyleSheet(
                    "background-color: rgb(209, 209, 209);\n"
                    "border-width:4px;\n"
                    "border-color:black;\n"
                    "border-style:offset;\n"
                    "border-radius:10px;")
                try:
                    self.text_output.setText(
                        self.default_export_path_mapper[process])
                except KeyError:
                    self.text_output.setText("")
            else:
                self.text_output.setStyleSheet(
                    "background-color: rgb(109, 109, 109);\n"
                    "border-width:4px;\n"
                    "border-color:black;\n"
                    "border-style:offset;\n"
                    "border-radius:10px;")

                self.text_output.setText("")

            self.text_costs.setText(self.default_costs)

            try:
                self.text_db_data.setText(self.default_path_mapper[process])
            except KeyError:
                self.text_db_data.setText("")

            self.change_process_color('red')

        else:
            self.text_costs.setStyleSheet(
                "background-color: white;\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

            self.text_db_data.setStyleSheet(
                "background-color: white;\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

            if self.tick_export_new.isChecked():
                self.text_output.setStyleSheet(
                    "background-color: white;\n"
                    "border-width:4px;\n"
                    "border-color:black;\n"
                    "border-style:offset;\n"
                    "border-radius:10px;")

                if self.user_output is None:
                    self.text_output.setText("")
                    self.text_output.setPlaceholderText(
                        "Paste path here or browse...")
                else:
                    self.text_output.setText(self.user_output)
            else:
                self.text_output.setStyleSheet(
                    "background-color: rgb(109, 109, 109);\n"
                    "border-width:4px;\n"
                    "border-color:black;\n"
                    "border-style:offset;\n"
                    "border-radius:10px;")

                self.text_output.setText("")

            if self.user_costs is None:
                self.text_costs.setText("")
                self.text_costs.setPlaceholderText(
                    "Paste path here or browse...")
            else:
                self.text_costs.setText(self.user_costs)
            if self.user_data is None:
                self.text_db_data.setText("")
                self.text_db_data.setPlaceholderText(
                    "Paste path here or browse...")
            else:
                self.text_db_data.setText(self.user_data)

        self.change_process_color('red')

        self.text_general.setText("")
        self.transformer = None


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = AKLUI(main_window)
    main_window.show()
    sys.exit(app.exec_())
