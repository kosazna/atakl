# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aztool_akl_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_designer(object):
    def setupUi(self, designer):
        designer.setObjectName("designer")
        designer.resize(800, 600)
        self.widget_main = QtWidgets.QWidget(designer)
        self.widget_main.setObjectName("widget_main")
        self.frame_main = QtWidgets.QFrame(self.widget_main)
        self.frame_main.setGeometry(QtCore.QRect(0, 0, 800, 600))
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
        self.frame_main.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.frame_main.setFont(font)
        self.frame_main.setAutoFillBackground(False)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.label_process = QtWidgets.QLabel(self.frame_main)
        self.label_process.setGeometry(QtCore.QRect(10, 100, 60, 30))
        self.label_process.setObjectName("label_process")
        self.label_costs = QtWidgets.QLabel(self.frame_main)
        self.label_costs.setGeometry(QtCore.QRect(10, 180, 60, 30))
        self.label_costs.setObjectName("label_costs")
        self.label_db_data = QtWidgets.QLabel(self.frame_main)
        self.label_db_data.setGeometry(QtCore.QRect(10, 220, 60, 30))
        self.label_db_data.setObjectName("label_db_data")
        self.label_records = QtWidgets.QLabel(self.frame_main)
        self.label_records.setGeometry(QtCore.QRect(10, 330, 60, 30))
        self.label_records.setObjectName("label_records")
        self.label_backup = QtWidgets.QLabel(self.frame_main)
        self.label_backup.setGeometry(QtCore.QRect(10, 370, 60, 30))
        self.label_backup.setObjectName("label_backup")
        self.label_data_paths = QtWidgets.QLabel(self.frame_main)
        self.label_data_paths.setGeometry(QtCore.QRect(10, 140, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_data_paths.setFont(font)
        self.label_data_paths.setObjectName("label_data_paths")
        self.label_action = QtWidgets.QLabel(self.frame_main)
        self.label_action.setGeometry(QtCore.QRect(10, 60, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_action.setFont(font)
        self.label_action.setObjectName("label_action")
        self.label_results = QtWidgets.QLabel(self.frame_main)
        self.label_results.setGeometry(QtCore.QRect(10, 290, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_results.setFont(font)
        self.label_results.setObjectName("label_results")
        self.line_1 = QtWidgets.QFrame(self.frame_main)
        self.line_1.setGeometry(QtCore.QRect(10, 90, 780, 3))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(self.frame_main)
        self.line_2.setGeometry(QtCore.QRect(10, 170, 780, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_main)
        self.line_3.setGeometry(QtCore.QRect(10, 320, 780, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.process_list = QtWidgets.QComboBox(self.frame_main)
        self.process_list.setGeometry(QtCore.QRect(69, 100, 311, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.process_list.setFont(font)
        self.process_list.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-radius:10px;")
        self.process_list.setEditable(False)
        self.process_list.setFrame(False)
        self.process_list.setObjectName("process_list")
        self.process_list.addItem("")
        self.process_list.addItem("")
        self.process_list.addItem("")
        self.button_process = QtWidgets.QToolButton(self.frame_main)
        self.button_process.setGeometry(QtCore.QRect(650, 470, 140, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_process.setFont(font)
        self.button_process.setAutoFillBackground(False)
        self.button_process.setStyleSheet(
            "background-color: rgba(207, 14, 30, 0.8);\n"
            "color: rgb(72, 72, 72);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.button_process.setCheckable(False)
        self.button_process.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.button_process.setAutoRaise(False)
        self.button_process.setObjectName("button_process")
        self.button_change_costs = QtWidgets.QToolButton(self.frame_main)
        self.button_change_costs.setGeometry(QtCore.QRect(650, 100, 140, 35))
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
        self.text_costs = QtWidgets.QLineEdit(self.frame_main)
        self.text_costs.setGeometry(QtCore.QRect(69, 180, 691, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_costs.setFont(font)
        self.text_costs.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                      "border-width:4px;\n"
                                      "border-color:black;\n"
                                      "border-style:offset;\n"
                                      "border-radius:10px;")
        self.text_costs.setFrame(True)
        self.text_costs.setObjectName("text_costs")
        self.text_db_data = QtWidgets.QLineEdit(self.frame_main)
        self.text_db_data.setGeometry(QtCore.QRect(69, 220, 691, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_db_data.setFont(font)
        self.text_db_data.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.text_db_data.setObjectName("text_db_data")
        self.text_records = QtWidgets.QLabel(self.frame_main)
        self.text_records.setGeometry(QtCore.QRect(69, 330, 711, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.text_records.setFont(font)
        self.text_records.setText("")
        self.text_records.setObjectName("text_records")
        self.text_backup = QtWidgets.QLabel(self.frame_main)
        self.text_backup.setGeometry(QtCore.QRect(69, 370, 711, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.text_backup.setFont(font)
        self.text_backup.setText("")
        self.text_backup.setObjectName("text_backup")
        self.akl_logo = QtWidgets.QTextBrowser(self.frame_main)
        self.akl_logo.setGeometry(QtCore.QRect(10, 1, 781, 61))
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
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.akl_logo.setFont(font)
        self.akl_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.akl_logo.setObjectName("akl_logo")
        self.browse_costs = QtWidgets.QToolButton(self.frame_main)
        self.browse_costs.setGeometry(QtCore.QRect(760, 180, 30, 30))
        self.browse_costs.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.browse_costs.setObjectName("browse_costs")
        self.browse_db_data = QtWidgets.QToolButton(self.frame_main)
        self.browse_db_data.setGeometry(QtCore.QRect(760, 220, 30, 30))
        self.browse_db_data.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.browse_db_data.setObjectName("browse_db_data")
        self.text_general = QtWidgets.QTextEdit(self.frame_main)
        self.text_general.setGeometry(QtCore.QRect(10, 410, 631, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.text_general.setFont(font)
        self.text_general.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.text_general.setObjectName("text_general")
        self.tick_default = QtWidgets.QCheckBox(self.frame_main)
        self.tick_default.setGeometry(QtCore.QRect(420, 100, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tick_default.setFont(font)
        self.tick_default.setAutoFillBackground(False)
        self.tick_default.setStyleSheet("")
        self.tick_default.setChecked(True)
        self.tick_default.setTristate(False)
        self.tick_default.setObjectName("tick_default")
        self.label_output = QtWidgets.QLabel(self.frame_main)
        self.label_output.setGeometry(QtCore.QRect(10, 260, 60, 30))
        self.label_output.setObjectName("label_output")
        self.text_output = QtWidgets.QLineEdit(self.frame_main)
        self.text_output.setGeometry(QtCore.QRect(69, 260, 691, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.text_output.setFont(font)
        self.text_output.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                       "border-width:4px;\n"
                                       "border-color:black;\n"
                                       "border-style:offset;\n"
                                       "border-radius:10px;")
        self.text_output.setObjectName("text_output")
        self.browse_output = QtWidgets.QToolButton(self.frame_main)
        self.browse_output.setGeometry(QtCore.QRect(760, 260, 30, 30))
        self.browse_output.setStyleSheet(
            "background-color: rgb(209, 209, 209);\n"
            "border-width:4px;\n"
            "border-color:black;\n"
            "border-style:offset;\n"
            "border-radius:10px;")
        self.browse_output.setObjectName("browse_output")
        self.button_validate_data = QtWidgets.QToolButton(self.frame_main)
        self.button_validate_data.setGeometry(QtCore.QRect(650, 410, 140, 51))
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
        self.label_backup.raise_()
        self.label_data_paths.raise_()
        self.label_action.raise_()
        self.label_results.raise_()
        self.line_1.raise_()
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
        designer.setCentralWidget(self.widget_main)
        self.menubar = QtWidgets.QMenuBar(designer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        designer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(designer)
        self.statusbar.setObjectName("statusbar")
        designer.setStatusBar(self.statusbar)

        self.retranslateUi(designer)
        QtCore.QMetaObject.connectSlotsByName(designer)

    def retranslateUi(self, designer):
        _translate = QtCore.QCoreApplication.translate
        designer.setWindowTitle(_translate("designer", "AKL"))
        self.label_process.setText(_translate("designer", "Process"))
        self.label_costs.setText(_translate("designer", "Costs"))
        self.label_db_data.setText(_translate("designer", "DB Data"))
        self.label_records.setText(_translate("designer", "Records"))
        self.label_backup.setText(_translate("designer", "Backup"))
        self.label_data_paths.setText(
            _translate("designer", "Choose data paths"))
        self.label_action.setText(
            _translate("designer", "Choose process action"))
        self.label_results.setText(_translate("designer", "Processing results"))
        self.process_list.setItemText(0, _translate("designer", "Concepts"))
        self.process_list.setItemText(1, _translate("designer",
                                                    "PT Beverages - Spirits"))
        self.process_list.setItemText(2, _translate("designer",
                                                    "PT Beverages - Lavazza"))
        self.button_process.setText(_translate("designer", "Process"))
        self.button_change_costs.setText(_translate("designer", "Change Costs"))
        self.akl_logo.setHtml(_translate("designer",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic\'; font-size:18pt; color:#434343;\">Attiki Kinisi Logistics SA</span></p>\n"
                                         "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Century Gothic\';\"><br /></p></body></html>"))
        self.browse_costs.setText(_translate("designer", "..."))
        self.browse_db_data.setText(_translate("designer", "..."))
        self.tick_default.setText(
            _translate("designer", "Use default file paths"))
        self.label_output.setText(_translate("designer", "Output"))
        self.browse_output.setText(_translate("designer", "..."))
        self.button_validate_data.setText(
            _translate("designer", "Validate data"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    designer = QtWidgets.QMainWindow()
    ui = Ui_designer()
    ui.setupUi(designer)
    designer.show()
    sys.exit(app.exec_())
