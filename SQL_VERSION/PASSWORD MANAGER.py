from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from cryptography.fernet import Fernet
import mysql.connector as sql

class pswdmng_MainWindow(object):
    def __init__(self, userloggedin, host, DBuser, DBpswd, DBname):
        self.userLoggedIn = userloggedin
        self.host = host
        self.DBuser = DBuser
        self.DBpswd = DBpswd
        self.DBname = DBname

    def setupUi(self, MainWindow):
        self.temp = ()
        self.user_details = []
        try:
            with open("secret1.key", "rb") as key:
                self.key = key.read()
        except:
            self.key = Fernet.generate_key()
            with open("secret1.key", "wb") as key:
                key.write(self.key)
        self.fernet = Fernet(self.key)
        self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
        self.cur = self.mydb.cursor()
        self.readFromDatabase()

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
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.clicked.connect(self.get_clicked_row)
        self.tableWidget.doubleClicked.connect(self.viewPassword)

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
        self.username_label.setText(_translate("MainWindow", self.userLoggedIn.lower()))
        self.label_5.setText(_translate("MainWindow", "Developed by AKASH KUMAR SINGH"))
        self.display()

    def readFromDatabase(self):
        try:
            self.cur.execute(f"SELECT * FROM {self.userLoggedIn.lower()} ORDER BY Website, Username")
            self.user_details = self.cur.fetchall()
        except:
            self.cur.execute(f"CREATE TABLE {self.userLoggedIn.lower()} (Website varchar(250) NOT NULL, Username varchar(250) NOT NULL, Password text NOT NULL)")

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
        for i in self.user_details:
            self.tableWidget.insertRow(self.count)
            self.tableWidget.setItem(self.count, 0, QTableWidgetItem(i[0]))
            self.tableWidget.setItem(self.count, 1, QTableWidgetItem(i[1]))
            self.tableWidget.setItem(self.count, 2, QTableWidgetItem("********"))
            self.count += 1

    def viewPassword(self, item):
        for i in range(len(self.user_details)):
            self.tableWidget.setItem(i, 2, QTableWidgetItem("********"))
        row = item.row()
        token = bytes(self.user_details[row][2][2:], 'ascii')
        self.tableWidget.setItem(row, 2, QTableWidgetItem(self.fernet.decrypt(token).decode()))

    def get_clicked_row(self, item):
        self.clicked_row = item.row()

    def add_user(self):
        website_text, ok1 = QtWidgets.QInputDialog.getText(MainWindow, "WEBSITE", "Enter the website name/url: ")
        if ok1:
            username_text, ok2 = QtWidgets.QInputDialog.getText(MainWindow, "USERNAME", "Enter your username: ")
            if ok2:
                self.cur.execute(f"SELECT Username FROM {self.userLoggedIn.lower()} WHERE Website = '{website_text}'")
                users = self.cur.fetchall()
                temp = [i[0] for i in users]
                if username_text in temp:
                    self.messageBox(["Username already exists.", "USER EXISTS"], "w")
                    return
                password_text, ok3 = QtWidgets.QInputDialog.getText(MainWindow, "PASSWORD", "Enter your password: ")
                password_text = self.fernet.encrypt(password_text.encode())
                if ok3:
                    self.cur.execute(f"INSERT INTO {self.userLoggedIn.lower()} VALUES ('{website_text}','{username_text}',\"{password_text}\")") 
                    self.mydb.commit() 
                self.readFromDatabase()
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
            self.cur.execute(f"UPDATE {self.userLoggedIn} SET Password = \"{newPassword}\" WHERE Website = '{temp[0]}' AND Username = '{temp[1]}'")
            self.mydb.commit()
            self.readFromDatabase()
            self.display()
        self.clicked_row = None

    def remove_user(self):
        try:
            temp = [self.tableWidget.item(self.clicked_row, 0).text(), self.tableWidget.item(self.clicked_row, 1).text()]
        except:
            return
        self.cur.execute(f"DELETE FROM {self.userLoggedIn.lower()} WHERE Website = '{temp[0]}' AND Username LIKE BINARY '{temp[1]}'")
        self.mydb.commit()
        self.readFromDatabase()
        self.display()
        self.clicked_row = None
        
    def search_website(self):
        searchText = self.search.text()
        self.tableWidget.setRowCount(0)
        self.count = 0
        self.cur.execute(f"SELECT * FROM {self.userLoggedIn} WHERE Website REGEXP '.*{searchText}.*' ORDER BY Website, Username")
        temp = self.cur.fetchall()
        for i in temp:
            self.tableWidget.insertRow(self.count)
            self.tableWidget.setItem(self.count, 0, QTableWidgetItem(i[0]))
            self.tableWidget.setItem(self.count, 1, QTableWidgetItem(i[1]))
            self.tableWidget.setItem(self.count, 2, QTableWidgetItem("********"))
            self.count += 1
        

class login_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.DBname = None
        self.fill_flag = True
        try:
            with open("secret2.key", "rb") as key:
                self.key = key.read()
        except:
            self.key = Fernet.generate_key()
            with open("secret2.key", "wb") as key:
                key.write(self.key)
        self.fernet = Fernet(self.key)
        self.loginToDB()
        # To validate login credentials.
        try:
            self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd)
            self.cur = self.mydb.cursor()
        except:
            self.messageBox(["You entered wrong credentials.", "ERROR"], "w")
            sys.exit()
        if not self.DBname:
            self.connectToDB()
        # To validate database exists or not
        try:
            self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
            with open("DB.key", "w") as f:
                    f.write(f"{self.host} {self.DBuser} {self.DBpswd} {self.DBname}")
            self.cur = self.mydb.cursor()
        except:
            ok = self.messageBox(["No database with specified name exists. Do you want to create one?", "NO DATABASE"], "w")
            if ok ==  QMessageBox.Ok:
                self.cur.execute(f"CREATE DATABASE {self.DBname}")
                with open("DB.key", "w") as f:
                    f.write(f"{self.host} {self.DBuser} {self.DBpswd} {self.DBname}")
                self.messageBox(["Database created successfully", "SUCCESS"], "i")
                self.mydb.commit()
                self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
                self.cur = self.mydb.cursor()
            else:
                sys.exit()
        self.readFromDatabase()

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

        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(220, 495, 91, 31))
        self.delete.setStyleSheet("background-color: yellow; font-family: forte; font-size: 20px; border-radius: 5px")
        self.delete.setObjectName("reset")
        self.delete.clicked.connect(self.delete_user)

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
        self.delete.setText(_translate("MainWindow", "Delete"))
        self.register.setText(_translate("MainWindow", "Register"))
        self.heading.setText(_translate("MainWindow", "LOGIN / REGISTER"))

    def loginToDB(self):
        try:
            with open("DB.key", "r") as f:
                temp = f.read()
            self.host, self.DBuser, self.DBpswd, self.DBname = temp.split()
            return
        except:
            self.host, ok1 = QtWidgets.QInputDialog.getText(MainWindow, "HOST", "Enter the hostname (localhost/IP address): ")
            if ok1:
                self.DBuser, ok2 = QtWidgets.QInputDialog.getText(MainWindow, "DB USER", "Enter the username of MySQL database: ")
                if ok2:
                    self.DBpswd, ok3 = QtWidgets.QInputDialog.getText(MainWindow, "PASSWORD", "Enter your password for database: ")
                    if ok3:
                        return
        sys.exit()

    def connectToDB(self):
        self.DBname, ok = QtWidgets.QInputDialog.getText(MainWindow, "DB NAME", "Enter the name of MySQL database: ")
        if ok:
            return

    def readFromDatabase(self):
        try:
            self.cur.execute(f"SELECT Username FROM login")
            self.users = self.cur.fetchall()
            self.users = [i[0] for i in self.users]
        except:
            self.cur.execute("CREATE TABLE login (Username varchar(250) NOT NULL, Password text NOT NULL)")
            self.users = []

    def messageBox(self, msg, flag):
        msgBox = QMessageBox()
        if flag == "i":
            msgBox.setIcon(QMessageBox.Information)
        else:
            msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg[0])
        msgBox.setWindowTitle(msg[1])
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec()

    def validate(self):
        if not self.username.text() or not self.pswd.text():
            self.fill_flag = False
            self.messageBox(["One or more fields are empty", "TRY AGAIN"], "w")

    def register_user(self):
        self.validate()
        if self.fill_flag:
            if self.username.text().lower() in self.users:
                self.messageBox(["User already exists.", "ALREADY EXIST"], "w")
                return
            password = self.fernet.encrypt(self.pswd.text().encode())
            self.cur.execute(f"INSERT INTO login VALUE ('{self.username.text().lower()}', \"{password}\")")
            self.mydb.commit()
            self.messageBox(["User registered successfully....", "SUCCESS"], "i")   
            self.readFromDatabase() 
        self.fill_flag = True
    
    def login_user(self):
        self.validate()
        if self.fill_flag:
            if (self.username.text().lower() in self.users):
                self.cur.execute(f"SELECT Password FROM login WHERE Username = '{self.username.text().lower()}'")
                token = self.cur.fetchall()
                token = bytes(token[0][0][2:], 'ascii')
                password = self.fernet.decrypt(token).decode()
                if password == self.pswd.text():
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

    def delete_user(self):
        self.validate()
        if self.fill_flag:
            if (self.username.text().lower() in self.users):
                self.cur.execute(f"SELECT Password FROM login WHERE Username = '{self.username.text().lower()}'")
                token = self.cur.fetchall()
                token = bytes(token[0][0][2:], 'ascii')
                password = self.fernet.decrypt(token).decode()
                if password == self.pswd.text():
                    self.cur.execute(f"DROP TABLE {self.username.text().lower()}")
                    self.cur.execute(f"DELETE FROM login WHERE Username = '{self.username.text().lower()}'")
                    self.mydb.commit()
                    self.readFromDatabase()
                    self.messageBox(["User data deleted successfully.", "DELETE SUCCESS"], "i")
                else:
                    self.messageBox(["You entered wrong password.", "INCORRECT PASSWORD"], "w")
            else:
                self.messageBox(["User dosen't exist.", "INCORRECT PASSWORD"], "w")
        self.fill_flag = True

    def runPswdMng(self):
        MainWindow.close()
        MainWindow.setStyleSheet("background-color: white")
        self.pMainWindow = QtWidgets.QMainWindow()
        self.pui = pswdmng_MainWindow(self.username.text(), self.host, self.DBuser, self.DBpswd, self.DBname)
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
