# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aztool_akl_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


class Ui_akl_windows(object):
    def setupUi(self, akl_windows):
        akl_windows.setObjectName("akl_windows")
        akl_windows.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(akl_windows)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_process = QtWidgets.QLabel(self.frame)
        self.label_process.setGeometry(QtCore.QRect(10, 110, 60, 30))
        self.label_process.setObjectName("label_process")
        self.label_costs = QtWidgets.QLabel(self.frame)
        self.label_costs.setGeometry(QtCore.QRect(10, 190, 60, 30))
        self.label_costs.setObjectName("label_costs")
        self.label_db_data = QtWidgets.QLabel(self.frame)
        self.label_db_data.setGeometry(QtCore.QRect(10, 230, 60, 30))
        self.label_db_data.setObjectName("label_db_data")
        self.label_records = QtWidgets.QLabel(self.frame)
        self.label_records.setGeometry(QtCore.QRect(10, 340, 60, 30))
        self.label_records.setObjectName("label_records")
        self.label_output = QtWidgets.QLabel(self.frame)
        self.label_output.setGeometry(QtCore.QRect(10, 380, 60, 30))
        self.label_output.setObjectName("label_output")
        self.label_data_paths = QtWidgets.QLabel(self.frame)
        self.label_data_paths.setGeometry(QtCore.QRect(10, 150, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_data_paths.setFont(font)
        self.label_data_paths.setObjectName("label_data_paths")
        self.label_action = QtWidgets.QLabel(self.frame)
        self.label_action.setGeometry(QtCore.QRect(10, 70, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_action.setFont(font)
        self.label_action.setObjectName("label_action")
        self.label_results = QtWidgets.QLabel(self.frame)
        self.label_results.setGeometry(QtCore.QRect(10, 300, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_results.setFont(font)
        self.label_results.setObjectName("label_results")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 100, 780, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 180, 780, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(10, 330, 780, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.process_list = QtWidgets.QComboBox(self.frame)
        self.process_list.setGeometry(QtCore.QRect(80, 110, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.process_list.setFont(font)
        self.process_list.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.process_list.setEditable(False)
        self.process_list.setFrame(False)
        self.process_list.setObjectName("process_list")
        self.process_list.addItem("")
        self.process_list.addItem("")
        self.process_list.addItem("")
        self.button_process = QtWidgets.QToolButton(self.frame)
        self.button_process.setGeometry(QtCore.QRect(650, 480, 140, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_process.setFont(font)
        self.button_process.setAutoFillBackground(False)
        self.button_process.setStyleSheet("background-color: rgb(72, 72, 72);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-width:4px;\n"
                                          "border-color:black;\n"
                                          "border-style:offset;\n"
                                          "border-radius:10px;")
        self.button_process.setCheckable(False)
        self.button_process.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.button_process.setAutoRaise(False)
        self.button_process.setObjectName("button_process")
        self.button_change_costs = QtWidgets.QToolButton(self.frame)
        self.button_change_costs.setGeometry(QtCore.QRect(650, 110, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_change_costs.setFont(font)
        self.button_change_costs.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.button_change_costs.setObjectName("button_change_costs")
        self.text_costs = QtWidgets.QLineEdit(self.frame)
        self.text_costs.setGeometry(QtCore.QRect(80, 190, 680, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.text_costs.setFont(font)
        self.text_costs.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                      "border-width:4px;\n"
                                      "border-color:black;\n"
                                      "border-style:offset;\n"
                                      "border-radius:10px;")
        self.text_costs.setFrame(True)
        self.text_costs.setObjectName("text_costs")
        self.text_db_data = QtWidgets.QLineEdit(self.frame)
        self.text_db_data.setGeometry(QtCore.QRect(80, 230, 680, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.text_db_data.setFont(font)
        self.text_db_data.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.text_db_data.setObjectName("text_db_data")
        self.text_records = QtWidgets.QLabel(self.frame)
        self.text_records.setGeometry(QtCore.QRect(80, 340, 700, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_records.setFont(font)
        self.text_records.setText("")
        self.text_records.setObjectName("text_records")
        self.text_backup = QtWidgets.QLabel(self.frame)
        self.text_backup.setGeometry(QtCore.QRect(80, 380, 700, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_backup.setFont(font)
        self.text_backup.setText("")
        self.text_backup.setObjectName("text_backup")
        self.akl_logo = QtWidgets.QTextBrowser(self.frame)
        self.akl_logo.setGeometry(QtCore.QRect(10, 1, 781, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.akl_logo.setPalette(palette)
        self.akl_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.akl_logo.setObjectName("akl_logo")
        self.browse_costs = QtWidgets.QToolButton(self.frame)
        self.browse_costs.setGeometry(QtCore.QRect(760, 190, 30, 30))
        self.browse_costs.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.browse_costs.setObjectName("browse_costs")
        self.browse_db_data = QtWidgets.QToolButton(self.frame)
        self.browse_db_data.setGeometry(QtCore.QRect(760, 230, 30, 30))
        self.browse_db_data.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.browse_db_data.setObjectName("browse_db_data")
        self.text_general = QtWidgets.QTextEdit(self.frame)
        self.text_general.setGeometry(QtCore.QRect(10, 430, 631, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.text_general.setFont(font)
        self.text_general.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.text_general.setObjectName("text_general")
        self.tick_default = QtWidgets.QCheckBox(self.frame)
        self.tick_default.setGeometry(QtCore.QRect(420, 110, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tick_default.setFont(font)
        self.tick_default.setAutoFillBackground(False)
        self.tick_default.setStyleSheet("")
        self.tick_default.setChecked(True)
        self.tick_default.setTristate(False)
        self.tick_default.setObjectName("tick_default")
        self.label_output = QtWidgets.QLabel(self.frame)
        self.label_output.setGeometry(QtCore.QRect(10, 270, 60, 30))
        self.label_output.setObjectName("label_output")
        self.text_output = QtWidgets.QLineEdit(self.frame)
        self.text_output.setGeometry(QtCore.QRect(80, 270, 680, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.text_output.setFont(font)
        self.text_output.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                       "border-width:4px;\n"
                                       "border-color:black;\n"
                                       "border-style:offset;\n"
                                       "border-radius:10px;")
        self.text_output.setObjectName("text_output")
        self.browse_output = QtWidgets.QToolButton(self.frame)
        self.browse_output.setGeometry(QtCore.QRect(760, 270, 30, 30))
        self.browse_output.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.browse_output.setObjectName("browse_output")
        self.button_validate_data = QtWidgets.QToolButton(self.frame)
        self.button_validate_data.setGeometry(QtCore.QRect(650, 430, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_validate_data.setFont(font)
        self.button_validate_data.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.button_validate_data.setObjectName("button_validate_data")
        self.label_process.raise_()
        self.label_costs.raise_()
        self.label_db_data.raise_()
        self.label_records.raise_()
        self.label_output.raise_()
        self.label_data_paths.raise_()
        self.label_action.raise_()
        self.label_results.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.process_list.raise_()
        self.button_change_costs.raise_()
        self.text_costs.raise_()
        self.text_db_data.raise_()
        self.text_records.raise_()
        self.text_backup.raise_()
        self.akl_logo.raise_()
        self.browse_costs.raise_()
        self.browse_db_data.raise_()
        self.button_process.raise_()
        self.text_general.raise_()
        self.tick_default.raise_()
        self.label_output.raise_()
        self.text_output.raise_()
        self.browse_output.raise_()
        self.button_validate_data.raise_()
        akl_windows.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(akl_windows)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        akl_windows.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(akl_windows)
        self.statusbar.setObjectName("statusbar")
        akl_windows.setStatusBar(self.statusbar)

        self.retranslateUi(akl_windows)
        QtCore.QMetaObject.connectSlotsByName(akl_windows)

        ###########################################################################
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

    def retranslateUi(self, akl_windows):
        _translate = QtCore.QCoreApplication.translate
        akl_windows.setWindowTitle(_translate("akl_windows", "AKL"))
        self.label_process.setText(_translate("akl_windows", "Process"))
        self.label_costs.setText(_translate("akl_windows", "Costs"))
        self.label_db_data.setText(_translate("akl_windows", "DB Data"))
        self.label_records.setText(_translate("akl_windows", "Records"))
        self.label_output.setText(_translate("akl_windows", "Backup"))
        self.label_data_paths.setText(
            _translate("akl_windows", "Choose data paths"))
        self.label_action.setText(
            _translate("akl_windows", "Choose process action"))
        self.label_results.setText(
            _translate("akl_windows", "Processing results"))
        self.process_list.setItemText(0, _translate("akl_windows", "Concepts"))
        self.process_list.setItemText(1, _translate("akl_windows",
                                                    "PT Beverages - Spirits"))
        self.process_list.setItemText(2, _translate("akl_windows",
                                                    "PT Beverages - Lavazza"))
        self.button_process.setText(_translate("akl_windows", "Process"))
        self.button_change_costs.setText(
            _translate("akl_windows", "Change Costs"))
        self.akl_logo.setHtml(_translate("akl_windows",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Century Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#434343;\">Attiki Kinisi Logistics S.A.</span></p>\n"
                                         "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#434343;\">powered by aztool</span></p></body></html>"))
        self.browse_costs.setText(_translate("akl_windows", "..."))
        self.browse_db_data.setText(_translate("akl_windows", "..."))
        self.tick_default.setText(
            _translate("akl_windows", "Use default file paths"))
        self.label_output.setText(_translate("akl_windows", "Output"))
        self.browse_output.setText(_translate("akl_windows", "..."))
        self.button_validate_data.setText(
            _translate("akl_windows", "Validate data"))

    ###########################################################################

    def init_paths(self):
        start_process = "Concepts"
        self.text_costs.setText(self.default_costs)

        try:
            self.text_db_data.setText(self.default_path_mapper[start_process])
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
        self.default_path_mapper = {k: str(v) for k, v in path_mapper.items()}

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
        transformer.export()

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

    def browse_costs_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.home_dir)
        self.text_costs.setText(filename[0])

    def browse_db_data_func(self):
        filename = QFileDialog.getOpenFileName(directory=self.home_dir)
        self.text_db_data.setText(filename[0])

    def browse_output_func(self):
        filename = QFileDialog.getSaveFileName(directory=self.home_dir)
        export_file = filename[0] + ".xlsx"
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    akl_windows = QtWidgets.QMainWindow()
    ui = Ui_akl_windows()
    ui.setupUi(akl_windows)
    akl_windows.show()
    sys.exit(app.exec_())
