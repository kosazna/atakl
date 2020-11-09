# -*- coding: utf-8 -*-

import os
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog
from aztool_akl.gui.designer import *
from aztool_akl.validate.input import validate_proper_and_existent_path


class UiAKL(Ui_designer):
    def __init__(self, window):
        self.setupUi(window)

        self.home_dir = ""
        self.default_costs = ""
        self.last_visited = None
        self.default_path_mapper = {}
        self.default_export_path_mapper = {}
        self.transformer_mapper = {}
        self.transformer = None

        self.browse_costs.clicked.connect(self.browse_costs_func)
        self.browse_db_data.clicked.connect(self.browse_db_data_func)
        self.browse_output.clicked.connect(self.browse_output_func)
        self.tick_default.stateChanged.connect(self.check_default_box)
        self.button_change_costs.clicked.connect(self.change_costs)
        self.process_list.currentIndexChanged.connect(
            self.change_paths_per_process)

        self.button_validate_data.clicked.connect(self.validate_data)

        self.button_process.clicked.connect(self.process_execute)

    def set_essential_data(self, paths, transformer_map):
        self.set_home_dir(paths.akl_home)
        self.set_default_costs(paths.default_costs)
        self.set_default_path_mapper(paths.default_path_mapper)
        self.set_default_export_path_mapper(paths.default_export_path_mapper)
        self.set_transformers(transformer_map)
        self.gui_startup_paths()

    def gui_startup_paths(self):
        start_process = "Concepts"
        self.text_costs.setText(self.default_costs)

        try:
            self.text_db_data.setText(
                self.default_path_mapper[start_process])
            self.text_output.setText(
                self.default_export_path_mapper[start_process])
        except KeyError:
            self.text_db_data.setText("")
            self.text_output.setText("")

    def get_last_visit(self):
        if self.last_visited is None:
            return self.home_dir
        return self.last_visited

    def set_last_visit(self, chosen_path):
        self.last_visited = str(Path(chosen_path).parent)

    def change_costs(self):
        os.startfile(self.default_costs)

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

        self.transformer = tranformer_process(data_filepath=db_data,
                                              cost_filepath=costs_path,
                                              output_path=output)

        self.text_records.setText(str(self.transformer.data.shape[0]))
        self.transformer.validate()

    def process_execute(self):
        self.transformer.process()
        self.text_backup.setText(self.transformer.export())

    def change_paths_per_process(self):
        process = self.process_list.currentText()
        if self.tick_default.isChecked():
            self.text_costs.setText(self.default_costs)

            try:
                self.text_db_data.setText(self.default_path_mapper[process])
                self.text_output.setText(
                    self.default_export_path_mapper[process])
            except KeyError:
                self.text_db_data.setText("")
                self.text_output.setText("")
        else:
            self.text_costs.setText("Paste path here or browse...")
            self.text_db_data.setText("Paste path here or browse...")
            self.text_output.setText("Paste path here or browse...")

        self.text_records.setText("")
        self.text_backup.setText("")

    def browse_costs_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.get_last_visit())
        file_path = filename[0]
        if file_path:
            self.text_costs.setText(file_path)
            self.set_last_visit(file_path)

    def browse_db_data_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.get_last_visit())
        file_path = filename[0]
        if file_path:
            self.text_db_data.setText(file_path)
            self.set_last_visit(file_path)

    def browse_output_func(self):
        filename = QFileDialog.getSaveFileName(directory=self.get_last_visit())
        file_path = filename[0]
        if file_path:
            export_file = validate_proper_and_existent_path(file_path)
            self.text_output.setText(export_file)
            self.set_last_visit(file_path)

    def check_default_box(self):
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

            self.text_output.setStyleSheet(
                "background-color: rgb(209, 209, 209);\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

            process = self.process_list.currentText()
            self.text_costs.setText(self.default_costs)

            try:
                self.text_db_data.setText(self.default_path_mapper[process])
                self.text_output.setText(
                    self.default_export_path_mapper[process])
            except KeyError:
                self.text_db_data.setText("")
                self.text_output.setText("")

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

            self.text_output.setStyleSheet(
                "background-color: white;\n"
                "border-width:4px;\n"
                "border-color:black;\n"
                "border-style:offset;\n"
                "border-radius:10px;")

            self.text_costs.setText("Paste path here or browse...")
            self.text_db_data.setText("Paste path here or browse...")
            self.text_output.setText("Paste path here or browse...")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiAKL(main_window)
    main_window.show()
    sys.exit(app.exec_())
