from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pickle
from cryptography.fernet import Fernet

class pswdmng_MainWindow(object):
    def __init__(self, userloggedin):
        self.userLoggedIn = userloggedin

    def setupUi(self, MainWindow):
        self.user_details = {}
        try:
            with open("secret1.key", "rb") as key:
                self.key = key.read()
        except:
            self.key = Fernet.generate_key()
            with open("secret1.key", "wb") as key:
                key.write(self.key)
        self.fernet = Fernet(self.key)
        self.readFromPickle()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: white; border: 0")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.frame_2.setStyleSheet("background-color: red;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.search = QtWidgets.QLineEdit(self.frame_2)
        self.search.setGeometry(QtCore.QRect(440, 30, 261, 41))
        self.search.setStyleSheet("background-color: white; color: blue; font-size: 18px; font-family: \"Century Gothic\";")
        self.search.setObjectName("search")

        self.search_button = QtWidgets.QToolButton(self.frame_2)
        self.search_button.setGeometry(QtCore.QRect(730, 30, 41, 41))
        self.search_button.setStyleSheet("background-color: white; border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-search-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(30, 30))
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.search_website)

        self.add_button = QtWidgets.QToolButton(self.frame_2)
        self.add_button.setGeometry(QtCore.QRect(200, 20, 71, 51))
        self.add_button.setStyleSheet("border: 0px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons8-add-user-male-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setIconSize(QtCore.QSize(100, 100))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_user)

        self.remove_button = QtWidgets.QToolButton(self.frame_2)
        self.remove_button.setGeometry(QtCore.QRect(280, 20, 71, 61))
        self.remove_button.setStyleSheet("border: 0px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons8-denied-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon2)
        self.remove_button.setIconSize(QtCore.QSize(45, 45))
        self.remove_button.setObjectName("remove_button")
        self.remove_button.clicked.connect(self.remove_user)

        self.update_button = QtWidgets.QToolButton(self.frame_2)
        self.update_button.setGeometry(QtCore.QRect(350, 30, 71, 41))
        self.update_button.setStyleSheet("border: 0px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons8-update-user-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_button.setIcon(icon3)
        self.update_button.setIconSize(QtCore.QSize(100, 100))
        self.update_button.setObjectName("update_button")
        self.update_button.clicked.connect(self.update_user)

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 0, 131, 51))
        self.label.setStyleSheet("color: yellow; font-size: 30px; font-family: impact;")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 121, 51))
        self.label_2.setStyleSheet("color: yellow; font-size: 30px; font-family: impact;")
        self.label_2.setObjectName("label_2")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 90, 801, 41))
        self.frame.setStyleSheet("background-color: #dfffdb;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(320, 0, 71, 41))
        self.label_3.setStyleSheet("font-size: 20px; font-family: stencil; ")
        self.label_3.setObjectName("label_3")

        self.username_label = QtWidgets.QLabel(self.frame)
        self.username_label.setGeometry(QtCore.QRect(400, 0, 171, 41))
        self.username_label.setStyleSheet("font-size: 20px; font-family: \"Monotype corsiva\";")
        self.username_label.setObjectName("username_label")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 140, 801, 411))
        self.tableWidget.setStyleSheet("border: 2px; font-size: 20px; font-family: times new roman; color: #760dd9; background-color: \"white\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(260)
        #self.tableWidget.clicked.connect(self.get_clicked_row_col)
        # For the horizontal labels to be visible
        self.tableWidget.setHorizontalHeaderLabels(["Website", "Username", "Password"])
        self.tableWidget.horizontalHeader().setStyleSheet("font-size: 16px; font-family: elephant; color: black;")
        self.tableWidget.setRowCount(0)
        self.tableWidget.clicked.connect(self.get_clicked_row)

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 569, 801, 31))
        self.frame_3.setStyleSheet("background-color: red;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(290, -1, 211, 31))
        self.label_5.setStyleSheet("font-family: \"Comic Sans MS\"; font-size: 12px; color: white")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.search_button.setText(_translate("MainWindow", "..."))
        self.add_button.setText(_translate("MainWindow", "..."))
        self.remove_button.setText(_translate("MainWindow", "..."))
        self.update_button.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Manager"))
        self.label_3.setText(_translate("MainWindow", "User"))
        self.username_label.setText(_translate("MainWindow", self.userLoggedIn))
        self.label_5.setText(_translate("MainWindow", "Developed by AKASH KUMAR SINGH"))
        self.display()

    def writeToPickle(self):
        with open("user_details.pickle", 'wb') as f:
                pickle.dump(self.user_details, f)

    def readFromPickle(self):
        try:
            with open("user_details.pickle", "rb") as f:
                self.user_details = pickle.load(f)
        except:
            with open("user_details.pickle", 'wb') as f:
                pickle.dump(self.user_details, f)

    def messageBox(self, msg, flag):
        msgBox = QMessageBox()
        if flag == "i":
            msgBox.setIcon(QMessageBox.Information)
        else:
            msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg[0])
        msgBox.setWindowTitle(msg[1])
        msgBox.exec()

    def display(self):
        self.tableWidget.setRowCount(0)
        self.count = 0
        if self.userLoggedIn not in self.user_details:
            self.user_details[self.userLoggedIn] = {}
        else:
            for i in self.user_details[self.userLoggedIn]:
                for j in self.user_details[self.userLoggedIn][i]:
                    self.tableWidget.insertRow(self.count)
                    self.tableWidget.setItem(self.count, 0, QTableWidgetItem(i))
                    self.tableWidget.setItem(self.count, 1, QTableWidgetItem(j))
                    self.tableWidget.setItem(self.count, 2, QTableWidgetItem(self.fernet.decrypt(self.user_details[self.userLoggedIn][i][j]).decode()))
                    self.count += 1

    def get_clicked_row(self, item):
        self.clicked_row = item.row()

    def add_user(self):
        website_text, ok1 = QtWidgets.QInputDialog.getText(MainWindow, "WEBSITE", "Enter the website name/url: ")
        if ok1:
            username_text, ok2 = QtWidgets.QInputDialog.getText(MainWindow, "USERNAME", "Enter your username: ")
            if ok2:
                if website_text in self.user_details[self.userLoggedIn]:
                    if username_text in self.user_details[self.userLoggedIn][website_text]:
                        self.messageBox(["Username already exists.", "USER EXISTS"], "w")
                        return
                password_text, ok3 = QtWidgets.QInputDialog.getText(MainWindow, "PASSWORD", "Enter your password: ")
                password_text = self.fernet.encrypt(password_text.encode())
                if ok3:
                    if website_text in self.user_details[self.userLoggedIn]:
                         self.user_details[self.userLoggedIn][website_text][username_text] = password_text
                    else:
                        self.user_details[self.userLoggedIn][website_text] = {username_text: password_text}
                    self.writeToPickle()
                    self.display()
                    self.messageBox(["Credentials saved successfully....", "SUCCESS"], "i")
    
    def update_user(self):
        try:
            temp = [self.tableWidget.item(self.clicked_row, 0).text(), self.tableWidget.item(self.clicked_row, 1).text()]
        except:
            return
        newPassword, ok = QtWidgets.QInputDialog.getText(MainWindow, "NEW PASSWORD", "Enter your new password: ")
        if ok:
            newPassword = self.fernet.encrypt(newPassword.encode())
            self.user_details[self.userLoggedIn][temp[0]][temp[1]] = newPassword
            self.display()
        self.writeToPickle()
        self.clicked_row = None

    def remove_user(self):
        try:
            temp = [self.tableWidget.item(self.clicked_row, 0).text(), self.tableWidget.item(self.clicked_row, 1).text()]
        except:
            return
        del self.user_details[self.userLoggedIn][temp[0]][temp[1]]
        if not self.user_details[self.userLoggedIn][temp[0]]:
            del self.user_details[self.userLoggedIn][temp[0]]
        self.writeToPickle()
        self.display()
        self.clicked_row = None
        
    def search_website(self):
        searchText = self.search.text()
        self.tableWidget.setRowCount(0)
        self.count = 0
        for i in self.user_details[self.userLoggedIn]:
            if searchText in i:
                for j in self.user_details[self.userLoggedIn][i]:
                    self.tableWidget.insertRow(self.count)
                    self.tableWidget.setItem(self.count, 0, QTableWidgetItem(i))
                    self.tableWidget.setItem(self.count, 1, QTableWidgetItem(j))
                    self.tableWidget.setItem(self.count, 2, QTableWidgetItem(self.user_details[self.userLoggedIn][i][j]))
                    self.count += 1
        

class login_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.user_data = {}
        self.fill_flag = True
        try:
            with open("secret2.key", "rb") as key:
                self.key = key.read()
        except:
            self.key = Fernet.generate_key()
            with open("secret2.key", "wb") as key:
                key.write(self.key)
        self.fernet = Fernet(self.key)
        self.user()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 572)
        MainWindow.setStyleSheet("background-color: \"#383636\"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 130, 401, 381))
        self.frame.setStyleSheet("background-color: red; border-radius: 30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.icon = QtWidgets.QToolButton(self.frame)
        self.icon.setGeometry(QtCore.QRect(160, 20, 71, 61))
        self.icon.setStyleSheet("background-color: white; border-radius: 30px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-person-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(100, 100))
        self.icon.setObjectName("icon")

        self.username_label = QtWidgets.QLabel(self.frame)
        self.username_label.setGeometry(QtCore.QRect(20, 110, 101, 21))
        self.username_label.setStyleSheet("font-family: \"monotype corsiva\"; font-size: 25px;")
        self.username_label.setObjectName("username_label")

        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(30, 150, 331, 31))
        self.username.setStyleSheet("background-color: white; border-radius: 10px; font-family: \"Comic Sans MS\"; color: blue; font-size: 20px;")
        self.username.setText("")
        self.username.setObjectName("username")

        self.pswd_label = QtWidgets.QLabel(self.frame)
        self.pswd_label.setGeometry(QtCore.QRect(20, 200, 101, 21))
        self.pswd_label.setStyleSheet("font-family: \"monotype corsiva\"; font-size: 25px;")
        self.pswd_label.setObjectName("pswd_label")

        self.pswd = QtWidgets.QLineEdit(self.frame)
        self.pswd.setGeometry(QtCore.QRect(30, 240, 331, 31))
        self.pswd.setStyleSheet("background-color: white; border-radius: 10px; font-family: \"Comic Sans MS\"; color: blue; font-size: 20px;")
        self.pswd.setText("")
        self.pswd.setObjectName("pswd")
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signin = QtWidgets.QPushButton(self.frame)
        self.signin.setGeometry(QtCore.QRect(20, 320, 91, 31))
        self.signin.setStyleSheet("background-color: yellow; font-family: forte; font-size: 20px; border-radius: 5px")
        self.signin.setObjectName("signin")
        self.signin.clicked.connect(self.login_user)

        self.reset = QtWidgets.QPushButton(self.frame)
        self.reset.setGeometry(QtCore.QRect(150, 320, 91, 31))
        self.reset.setStyleSheet("background-color: yellow; font-family: forte; font-size: 20px; border-radius: 5px")
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.reset_screen)

        self.register = QtWidgets.QPushButton(self.frame)
        self.register.setGeometry(QtCore.QRect(290, 320, 91, 31))
        self.register.setStyleSheet("background-color: yellow; font-family: forte; font-size: 20px; border-radius: 5px")
        self.register.setObjectName("register_2")
        self.register.clicked.connect(self.register_user)

        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(130, 50, 281, 51))
        self.heading.setStyleSheet("color: white; font-size: 40px; font-family: impact;")
        self.heading.setObjectName("heading")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.icon.setText(_translate("MainWindow", "..."))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.pswd_label.setText(_translate("MainWindow", "Password"))
        self.signin.setText(_translate("MainWindow", "Sign In"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.register.setText(_translate("MainWindow", "Register"))
        self.heading.setText(_translate("MainWindow", "LOGIN / REGISTER"))

    def messageBox(self, msg, flag):
        msgBox = QMessageBox()
        if flag == "i":
            msgBox.setIcon(QMessageBox.Information)
        else:
            msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg[0])
        msgBox.setWindowTitle(msg[1])
        msgBox.exec()

    def validate(self):
        if not self.username.text() or not self.pswd.text():
            self.fill_flag = False
            self.messageBox(["One or more fields are empty", "TRY AGAIN"], "w")

    def user(self):
        try:
            with open("user_data.pickle", "rb") as f:
                self.user_data = pickle.load(f)
        except:
            with open("user_data.pickle", 'wb') as f:
                pickle.dump(self.user_data, f)

    def register_user(self):
        self.validate()
        if self.fill_flag:
            if self.username.text() in self.user_data:
                self.messageBox(["User already exists.", "ALREADY EXIST"], "w")
                return
            password = self.fernet.encrypt(self.pswd.text().encode())
            self.user_data[self.username.text()] = password
            with open("user_data.pickle", 'wb') as f:
                pickle.dump(self.user_data, f)
            self.messageBox(["User registered successfully....", "SUCCESS"], "i")    
        self.fill_flag = True  
    
    def login_user(self):
        self.validate()
        if self.fill_flag:
            if (self.username.text() in self.user_data):
                if self.fernet.decrypt(self.user_data[self.username.text()]).decode() == self.pswd.text():
                    self.messageBox(["You logged in successfully.", "LOGIN SUCCESS"], "i")
                    self.runPswdMng()
                else:
                    self.messageBox(["You entered wrong password.", "INCORRECT PASSWORD"], "w")
            else:
                self.messageBox(["User dosen't exist.", "INCORRECT PASSWORD"], "w")
        self.fill_flag = True

    def reset_screen(self):
        self.username.setText("")
        self.pswd.setText("")

    def runPswdMng(self):
        MainWindow.close()
        MainWindow.setStyleSheet("background-color: white")
        self.pMainWindow = QtWidgets.QMainWindow()
        self.pui = pswdmng_MainWindow(self.username.text())
        self.pui.setupUi(self.pMainWindow)
        self.pMainWindow.show()

import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    lui = login_MainWindow()
    lui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
