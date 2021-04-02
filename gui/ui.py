# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from atakl.gui.designer import *
from atakl.validate.input import validate_proper_and_existent_path
from atakl.utilities.utils import *

blue = "rgba(13, 110, 253, 0.8)"
green = "rgba(42, 214, 107, 0.8)"
teal = "rgba(32, 201, 151, 0.8)"
red = "rgba(239, 62, 79, 0.8)"
grey = "rgba(108, 117, 125, 0.8)"
yellow = "rgba(255, 193, 7, 0.8)"
cyan = "rgba(13, 202, 240, 0.8)"
orange = "rgba(253, 126, 20, 0.8)"
dark = "rgba(33, 37, 41, 0.8)"
white = "rgba(248, 248, 255, 0.8)"


def make_stylesheet(color, radius=5):
    _stylesheet = (f"background-color: {color};\n"
                   "border-width:4px;\n"
                   "border-color:black;\n"
                   "border-style:offset;\n"
                   f"border-radius:{radius}px;")
    return _stylesheet


def make_bt_stylesheet(color, radius=5):
    _stylesheet = (f"background-color: {color};\n"
                   "color: rgb(0, 0, 0);\n"
                   "border-width:10px;"
                   f"border-radius:{radius}px;")

    return _stylesheet


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

        self.is_validated = False

        self.browse_costs.clicked.connect(self.browse_costs_func)
        self.browse_db_data.clicked.connect(self.browse_db_data_func)
        self.browse_output.clicked.connect(self.browse_output_func)
        self.tick_default.stateChanged.connect(self.check_default_box)
        self.button_insert.clicked.connect(self.insert_to_db_data)
        self.process_list.currentIndexChanged.connect(
            self.change_paths_per_process)
        self.tick_export_new.stateChanged.connect(self.check_export_new)

        self.button_validate_data.clicked.connect(self.validate_data)

        self.button_process.clicked.connect(self.process_execute)

    # STYLING

    def mask_line_edit(self, line, status, text):
        if text:
            _text = text
            _placeholder = ""
        else:
            _text = ""
            _placeholder = "Paste path here or browse..."

        if status == 'enabled':
            stylesheet = make_stylesheet(white)
            line.setStyleSheet(stylesheet)
            line.setEnabled(True)
            line.setText(_text)
            line.setPlaceholderText(_placeholder)
        else:
            stylesheet = make_stylesheet(dark)
            line.setStyleSheet(stylesheet)
            line.setEnabled(False)
            line.setPlaceholderText("")
            line.setText("")

    def change_process_button(self, status):
        if status == 'ok':
            stylesheet = make_bt_stylesheet(blue)
            self.button_process.setGeometry(QtCore.QRect(670, 270, 120, 40))
            self.button_process.setStyleSheet(stylesheet)
        elif status == 'success':
            stylesheet = make_bt_stylesheet(teal)
            self.button_process.setGeometry(QtCore.QRect(670, 270, 120, 40))
            self.button_process.setStyleSheet(stylesheet)
        else:
            stylesheet = make_bt_stylesheet(grey)
            self.button_process.setGeometry(QtCore.QRect(670, 275, 120, 30))
            self.button_process.setStyleSheet(stylesheet)

    def change_validate_button(self, status):
        if status == 'sucess':
            stylesheet = make_bt_stylesheet(teal)
            self.button_validate_data.setStyleSheet(stylesheet)
        elif status == 'warning':
            stylesheet = make_bt_stylesheet(red)
            self.button_validate_data.setStyleSheet(stylesheet)
        else:
            stylesheet = make_bt_stylesheet(blue)
            self.button_validate_data.setStyleSheet(stylesheet)

    # FUNCTIONAL
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

    def insert_to_db_data(self):
        process = self.process_list.currentText()
        _current_text = self.text_db_data.text()

        if process == 'Essse':
            _new = _current_text + '@Distribution'
        else:
            _new = _current_text + '@Διανομή'

        self.text_db_data.setText(_new)

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

                self.text_general.setText(self.transformer.log.get_content())
                self.is_validated = True

                if self.transformer.validator.validation_passed:
                    self.change_validate_button('success')
                else:
                    self.change_validate_button('warning')

                self.change_process_button('ok')
            else:
                to_display = f"Some of the input files are missing!\n" \
                             f"Check 'Costs' and 'DB_Data' files."
                self.text_general.setText(to_display)
        else:
            to_display = "Input files should end with either '.xls' or '.xlsx'"
            self.text_general.setText(to_display)

    def process_execute(self):
        if self.transformer is not None:
            if self.is_validated:

                _old_txt = self.transformer.log.get_content()
                self.text_general.setText(_old_txt)

                self.transformer.process()
                self.transformer.export()

                _final_txt = _old_txt + "\n[Process Finished]"
                self.text_general.setText(_final_txt)

                self.transformer.log.erase()
                self.change_process_button('success')
            else:
                self.text_general.setText("Validate data first!")
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

        if process == 'Essse':
            self.button_insert.setText('@Distribution')
        else:
            self.button_insert.setText('@Διανομή')

        self.text_general.setText("")
        self.text_records.setText("0")

        self.transformer = None
        self.change_process_button('not ready')
        self.change_validate_button('new')

    def check_export_new(self):
        process = self.process_list.currentText()
        if self.tick_export_new.isChecked():
            if self.tick_default.isChecked():
                self.mask_line_edit(self.text_output,
                                    'enabled',
                                    self.default_export_path_mapper[process])

            else:
                _text_for_output = self.user_output if self.user_output is not None else ""
                self.mask_line_edit(
                    self.text_output, 'enabled', _text_for_output)
        else:
            self.mask_line_edit(self.text_output, 'disabled', "")

        self.text_general.setText("")
        self.transformer = None

    def check_default_box(self):
        process = self.process_list.currentText()
        if self.tick_default.isChecked():
            _text_for_costs = self.default_costs
            _text_for_db = self.default_path_mapper[process]
            _text_for_output = self.default_export_path_mapper[process]

        else:
            _text_for_costs = self.user_costs if self.user_costs is not None else ""
            _text_for_db = self.user_data if self.user_data is not None else ""
            _text_for_output = self.user_output if self.user_output is not None else ""

        self.mask_line_edit(self.text_costs,
                            'enabled',
                            _text_for_costs)
        self.mask_line_edit(self.text_db_data,
                            'enabled',
                            _text_for_db)

        if self.tick_export_new.isChecked():
            self.mask_line_edit(self.text_output,
                                'enabled',
                                _text_for_output)

        else:
            self.mask_line_edit(self.text_output,
                                'disabled',
                                "")

        self.text_general.setText("")
        self.transformer = None


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = AKLUI(main_window)
    main_window.show()
    sys.exit(app.exec_())
