# -*- coding: utf-8 -*-

from aztool_akl.gui.designer import *
from PyQt5.QtWidgets import QFileDialog
import os


class UiAKL(Ui_designer):
    def __init__(self, window):
        self.setupUi(window)

        self.home_dir = ""
        self.default_costs = ""
        self.default_path_mapper = {}
        self.default_export_path_mapper = {}
        self.transformer_mapper = {}

        self.browse_costs.clicked.connect(self.browse_costs_func)
        self.browse_db_data.clicked.connect(self.browse_db_data_func)
        self.browse_output.clicked.connect(self.browse_output_func)
        self.tick_default.stateChanged.connect(self.check_default_box)
        self.button_change_costs.clicked.connect(self.change_costs)
        self.process_list.currentIndexChanged.connect(
            self.change_paths_per_process)

        self.button_process.clicked.connect(self.process_execute)

    def init_paths(self):
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

    def change_costs(self):
        os.startfile(self.default_costs)

    def set_home(self, path):
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

    def process_execute(self):
        process = self.process_list.currentText()
        tranformer_process = self.transformer_mapper[process]
        costs_path = self.text_costs.text()
        db_data = self.text_db_data.text()
        output = self.text_output.text()

        transformer = tranformer_process(data_filepath=db_data,
                                         cost_filepath=costs_path)

        transformer.process()

        self.text_records.setText(str(transformer.data.shape[0]))
        self.text_backup.setText(transformer.export())

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
        filename = QFileDialog.getOpenFileName(directory=self.home_dir)
        file_path = filename[0]
        if file_path:
            self.text_costs.setText(file_path)

    def browse_db_data_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.home_dir)
        file_path = filename[0]
        if file_path:
            self.text_db_data.setText(file_path)

    def browse_output_func(self):
        filename = QFileDialog.getSaveFileName(directory=self.home_dir)
        file_path = filename[0]
        if file_path:
            export_file = file_path + ".xlsx"
            self.text_output.setText(export_file)

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
