from PyQt5 import QtWidgets, uic
from http import HTTPStatus
import requests
import sys, os

from visual_structure import Ui_MainWindow 


SETTINGS = {
    'username': 0,
    'password': 1,
    'auth_code': 2,
    'replace_link': 3,
    'clear_link': 4
}

SETT_LIST_FULL = 5

UID_HISTORY_FULL = 5


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = ()
        self.uid_history = []

        self.msg_empty_sett = QtWidgets.QMessageBox()
        self.msg_empty_sett.setWindowTitle("Warning")
        self.msg_empty_sett.setText('The settings are not filled in')
        self.msg_empty_sett.setIcon(QtWidgets.QMessageBox.Warning)

        self.msg_accepted_sett = QtWidgets.QMessageBox()
        self.msg_accepted_sett.setWindowTitle("Saved")
        self.msg_accepted_sett.setText('The settings are accepted')
        self.msg_accepted_sett.setIcon(QtWidgets.QMessageBox.Information)

        self.ui.btn_main_page.clicked.connect(self.btn_main_page)
        self.ui.btn_sett_page.clicked.connect(self.btn_sett_page)
        self.ui.btn_save_sett.clicked.connect(self.btn_save_sett)
        self.ui.btn_replace.clicked.connect(self.btn_replace)
        self.ui.btn_clear.clicked.connect(self.btn_clear)
        self.ui.btn_uid_1.clicked.connect(self.btn_set_uid_1)
        self.ui.btn_uid_2.clicked.connect(self.btn_set_uid_2)
        self.ui.btn_uid_3.clicked.connect(self.btn_set_uid_3)
        self.ui.btn_uid_4.clicked.connect(self.btn_set_uid_4)
        self.ui.btn_uid_5.clicked.connect(self.btn_set_uid_5)


    def btn_set_uid_1(self):
        if 'UID ' not in self.ui.btn_uid_1.text():
            self.ui.ln_uid_ins.setText(self.ui.btn_uid_1.text())


    def btn_set_uid_2(self):
        if 'UID ' not in self.ui.btn_uid_2.text():
            self.ui.ln_uid_ins.setText(self.ui.btn_uid_2.text())


    def btn_set_uid_3(self):
        if 'UID ' not in self.ui.btn_uid_3.text():
            self.ui.ln_uid_ins.setText(self.ui.btn_uid_3.text())


    def btn_set_uid_4(self):
        if 'UID ' not in self.ui.btn_uid_4.text():
            self.ui.ln_uid_ins.setText(self.ui.btn_uid_4.text())


    def btn_set_uid_5(self):
        if 'UID ' not in self.ui.btn_uid_5.text():
            self.ui.ln_uid_ins.setText(self.ui.btn_uid_5.text())


    def btn_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)


    def btn_sett_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page)


    def fill_obj_sett(self):
        self.settings = (self.ui.ln_username.text(),self.ui.ln_pass.text(),self.ui.ln_auth_code.text(),
              self.ui.ln_replace_link.text(),self.ui.ln_clear_link.text())


    def check_ins_sett(self):
        result_ins = (self.ui.ln_username.text(),self.ui.ln_pass.text(),self.ui.ln_auth_code.text(),
              self.ui.ln_replace_link.text(),self.ui.ln_clear_link.text())
        if '' not in result_ins:
            return True
        else:
            self.msg_empty_sett.exec()


    def btn_save_sett(self):
        if self.check_ins_sett():
            self.fill_obj_sett()
            with open(current_dir + '\conf.txt', 'w') as file:
                file.write('\n'.join(self.settings))
            self.msg_accepted_sett.exec()


    def fill_form_setting(self, settings):
        self.ui.ln_username.setText(settings[SETTINGS['username']])
        self.ui.ln_pass.setText(settings[SETTINGS['password']])
        self.ui.ln_auth_code.setText(settings[SETTINGS['auth_code']])
        self.ui.ln_replace_link.setText(settings[SETTINGS['replace_link']])
        self.ui.ln_clear_link.setText(settings[SETTINGS['clear_link']])
        self.fill_obj_sett()


    def btn_replace(self):
        try:
            uid = self.ui.ln_uid_ins.text()
            response = requests.post(
                f'{self.settings[SETTINGS["replace_link"]]}?code={self.settings[SETTINGS["auth_code"]]}', 
                json={
                    "username": f"{self.settings[SETTINGS['username']]}",
                    "password": f"{self.settings[SETTINGS['password']]}", 
                    "patientId": f"{uid}"
                })
            if response.status_code != 200:
                self.ui.txt_response.setText(response.json().get('description'))
            else:
                self.ui.txt_response.setText('Replacement is complite')
                self.add_uid_to_history(uid)
            self.ui.lb_status_code.setText(str(response.status_code))
            self.ui.lb_status_text.setText(HTTPStatus(response.status_code).phrase)
        except:
            self.ui.txt_response.setText('Could not send request')


    def fill_form_history(self, history):
        self.ui.btn_uid_1.setText(history[0])
        try:
            self.ui.btn_uid_2.setText(history[1])
            self.ui.btn_uid_3.setText(history[2])
            self.ui.btn_uid_4.setText(history[3])
            self.ui.btn_uid_5.setText(history[4])
        except:
            pass


    def fill_obj_history(self, history):
        for uid in history:
            self.uid_history.append(uid)
        self.fill_form_history(history)


    def update_uid_history(self):
        self.fill_form_history(self.uid_history)
        with open(current_dir + '\history.txt', 'w') as file:
                file.write('\n'.join(self.uid_history))


    def add_uid_to_history(self, uid):
        if uid not in self.uid_history:
            self.uid_history.insert(0, uid)
            if len(self.uid_history) > UID_HISTORY_FULL:
                self.uid_history.pop()
            self.update_uid_history()
        elif self.uid_history.index(uid) != 0:
            self.uid_history.insert(0,self.uid_history.pop(self.uid_history.index(uid)))
            self.update_uid_history()


    def btn_clear(self):
        try:
            response = requests.post(
                f'{self.settings[SETTINGS["clear_link"]]}?code={self.settings[SETTINGS["auth_code"]]}', 
                json={
                    "username": f"{self.settings[SETTINGS['username']]}",
                    "password": f"{self.settings[SETTINGS['password']]}",
                })
            self.ui.lb_status_code.setText(str(response.status_code))
            self.ui.lb_status_text.setText(HTTPStatus(response.status_code).phrase)
            self.ui.txt_response.setText('Clearing is complite')
        except:
            self.ui.txt_response.setText('Could not send request')




if __name__ == '__main__':
    current_dir = os.getcwd()

    #при возврате на главную страницу сохранять настройки

    try:
        with open(current_dir + '\history.txt') as file:
            file_history = list(file.read().split('\n'))
    except:
        file_history = []
    try:
        with open(current_dir + '\conf.txt') as file:
            file_settings = tuple(file.read().split('\n'))
    except:
        file_settings = ()
    app = QtWidgets.QApplication([])
    application = window()
    if len(file_history) > 0 and len(file_history) < 6:
        if file_history[0] != '':
            application.fill_obj_history(file_history)
    if len(file_settings) == SETT_LIST_FULL:
        application.fill_form_setting(file_settings)
    application.show()

    sys.exit(app.exec())