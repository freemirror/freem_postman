# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freem_postman.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_toolbar = QtWidgets.QFrame(self.centralwidget)
        self.frame_toolbar.setGeometry(QtCore.QRect(0, 0, 871, 31))
        self.frame_toolbar.setStyleSheet("background-color: rgb(42, 154, 156);")
        self.frame_toolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toolbar.setObjectName("frame_toolbar")
        self.btn_main_page = QtWidgets.QPushButton(self.frame_toolbar)
        self.btn_main_page.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.btn_main_page.setStyleSheet("background-color: rgb(58, 221, 202);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_main_page.setObjectName("btn_main_page")
        self.btn_sett_page = QtWidgets.QPushButton(self.frame_toolbar)
        self.btn_sett_page.setGeometry(QtCore.QRect(100, 0, 101, 31))
        self.btn_sett_page.setStyleSheet("background-color: rgb(58, 221, 202);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_sett_page.setObjectName("btn_sett_page")
        self.frame_pages = QtWidgets.QFrame(self.centralwidget)
        self.frame_pages.setGeometry(QtCore.QRect(0, 30, 871, 531))
        self.frame_pages.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 851, 511))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.label = QtWidgets.QLabel(self.main_page)
        self.label.setGeometry(QtCore.QRect(20, 30, 31, 31))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label.setObjectName("label")
        self.ln_uid_ins = QtWidgets.QLineEdit(self.main_page)
        self.ln_uid_ins.setGeometry(QtCore.QRect(50, 30, 301, 31))
        self.ln_uid_ins.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.ln_uid_ins.setObjectName("ln_uid_ins")
        self.btn_replace = QtWidgets.QPushButton(self.main_page)
        self.btn_replace.setGeometry(QtCore.QRect(50, 80, 111, 41))
        self.btn_replace.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_replace.setObjectName("btn_replace")
        self.btn_clear = QtWidgets.QPushButton(self.main_page)
        self.btn_clear.setGeometry(QtCore.QRect(180, 80, 101, 41))
        self.btn_clear.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_uid_1 = QtWidgets.QPushButton(self.main_page)
        self.btn_uid_1.setGeometry(QtCore.QRect(460, 30, 381, 31))
        self.btn_uid_1.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_uid_1.setObjectName("btn_uid_1")
        self.btn_uid_2 = QtWidgets.QPushButton(self.main_page)
        self.btn_uid_2.setGeometry(QtCore.QRect(460, 60, 381, 31))
        self.btn_uid_2.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_uid_2.setObjectName("btn_uid_2")
        self.btn_uid_3 = QtWidgets.QPushButton(self.main_page)
        self.btn_uid_3.setGeometry(QtCore.QRect(460, 90, 381, 31))
        self.btn_uid_3.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_uid_3.setObjectName("btn_uid_3")
        self.btn_uid_4 = QtWidgets.QPushButton(self.main_page)
        self.btn_uid_4.setGeometry(QtCore.QRect(460, 120, 381, 31))
        self.btn_uid_4.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_uid_4.setObjectName("btn_uid_4")
        self.btn_uid_5 = QtWidgets.QPushButton(self.main_page)
        self.btn_uid_5.setGeometry(QtCore.QRect(460, 150, 381, 31))
        self.btn_uid_5.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_uid_5.setObjectName("btn_uid_5")
        self.lb_status_code = QtWidgets.QLabel(self.main_page)
        self.lb_status_code.setGeometry(QtCore.QRect(40, 230, 61, 41))
        self.lb_status_code.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 14pt \"Arial Rounded MT Bold\";")
        self.lb_status_code.setText("")
        self.lb_status_code.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_status_code.setObjectName("lb_status_code")
        self.txt_response = QtWidgets.QTextEdit(self.main_page)
        self.txt_response.setGeometry(QtCore.QRect(140, 230, 601, 121))
        self.txt_response.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.txt_response.setObjectName("txt_response")
        self.label_3 = QtWidgets.QLabel(self.main_page)
        self.label_3.setGeometry(QtCore.QRect(140, 200, 161, 21))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.main_page)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 81, 20))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.main_page)
        self.label_5.setGeometry(QtCore.QRect(620, 10, 101, 16))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(17, 65, 66);")
        self.label_5.setObjectName("label_5")
        self.btn_clear_2 = QtWidgets.QPushButton(self.main_page)
        self.btn_clear_2.setGeometry(QtCore.QRect(360, 30, 31, 31))
        self.btn_clear_2.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Arial Rounded MT Bold\";")
        self.btn_clear_2.setObjectName("btn_clear_2")
        self.lb_status_text = QtWidgets.QLabel(self.main_page)
        self.lb_status_text.setGeometry(QtCore.QRect(10, 280, 121, 21))
        self.lb_status_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.lb_status_text.setText("")
        self.lb_status_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_status_text.setObjectName("lb_status_text")
        self.stackedWidget.addWidget(self.main_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.label_6 = QtWidgets.QLabel(self.settings_page)
        self.label_6.setGeometry(QtCore.QRect(94, 100, 71, 20))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.settings_page)
        self.label_7.setGeometry(QtCore.QRect(94, 130, 71, 20))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.settings_page)
        self.label_8.setGeometry(QtCore.QRect(94, 160, 71, 20))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.settings_page)
        self.label_9.setGeometry(QtCore.QRect(94, 190, 81, 20))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.settings_page)
        self.label_10.setGeometry(QtCore.QRect(94, 220, 71, 20))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_10.setObjectName("label_10")
        self.ln_username = QtWidgets.QLineEdit(self.settings_page)
        self.ln_username.setGeometry(QtCore.QRect(190, 100, 461, 21))
        self.ln_username.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.ln_username.setObjectName("ln_username")
        self.ln_pass = QtWidgets.QLineEdit(self.settings_page)
        self.ln_pass.setGeometry(QtCore.QRect(190, 130, 461, 21))
        self.ln_pass.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.ln_pass.setObjectName("ln_pass")
        self.ln_auth_code = QtWidgets.QLineEdit(self.settings_page)
        self.ln_auth_code.setGeometry(QtCore.QRect(190, 160, 461, 21))
        self.ln_auth_code.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.ln_auth_code.setObjectName("ln_auth_code")
        self.ln_replace_link = QtWidgets.QLineEdit(self.settings_page)
        self.ln_replace_link.setGeometry(QtCore.QRect(190, 190, 461, 21))
        self.ln_replace_link.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.ln_replace_link.setObjectName("ln_replace_link")
        self.ln_clear_link = QtWidgets.QLineEdit(self.settings_page)
        self.ln_clear_link.setGeometry(QtCore.QRect(190, 220, 461, 21))
        self.ln_clear_link.setStyleSheet("background-color: rgb(241, 241, 241);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.ln_clear_link.setObjectName("ln_clear_link")
        self.btn_save_sett = QtWidgets.QPushButton(self.settings_page)
        self.btn_save_sett.setGeometry(QtCore.QRect(110, 270, 93, 28))
        self.btn_save_sett.setStyleSheet("background-color: rgb(42, 154, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.btn_save_sett.setObjectName("btn_save_sett")
        self.label_2 = QtWidgets.QLabel(self.settings_page)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 131, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(17, 65, 66);\n"
"font: 8pt \"Arial Rounded MT Bold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.settings_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_clear_2.clicked.connect(self.ln_uid_ins.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Freem Postman"))
        self.btn_main_page.setText(_translate("MainWindow", "Main"))
        self.btn_sett_page.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "UID"))
        self.btn_replace.setText(_translate("MainWindow", "replace UID"))
        self.btn_clear.setText(_translate("MainWindow", "clear UID"))
        self.btn_uid_1.setText(_translate("MainWindow", "UID 1"))
        self.btn_uid_2.setText(_translate("MainWindow", "UID 2"))
        self.btn_uid_3.setText(_translate("MainWindow", "UID 3"))
        self.btn_uid_4.setText(_translate("MainWindow", "UID 4"))
        self.btn_uid_5.setText(_translate("MainWindow", "UID 5"))
        self.txt_response.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Rounded MT Bold\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "response content"))
        self.label_4.setText(_translate("MainWindow", "status code"))
        self.label_5.setText(_translate("MainWindow", "UID history"))
        self.btn_clear_2.setText(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "username"))
        self.label_7.setText(_translate("MainWindow", "password"))
        self.label_8.setText(_translate("MainWindow", "auth code"))
        self.label_9.setText(_translate("MainWindow", "replace link"))
        self.label_10.setText(_translate("MainWindow", "clear link"))
        self.btn_save_sett.setText(_translate("MainWindow", "save settings"))
        self.label_2.setText(_translate("MainWindow", "Settings"))
