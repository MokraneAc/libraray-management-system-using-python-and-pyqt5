import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3


class window(QMainWindow):
    def __init__(self):
        super().__init__()

    ## Qmessages boxs ####"
    def warning(self, message):
        self.msg = QtWidgets.QMessageBox(self)
        self.msg.setWindowTitle('Warning')
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setStyleSheet("background-color: white")
        self.msg.setText(message)
        self.msg.show()

    def information(self, message):
        self.msg1 = QtWidgets.QMessageBox(self)
        self.msg1.setWindowTitle('Infos')
        self.msg1.setIcon(QtWidgets.QMessageBox.Information)
        self.msg1.setStyleSheet("background-color: white")
        self.msg1.setText(message)
        self.msg1.show()

    def text(self, message):
        self.msg2 = QtWidgets.QMessageBox(self)
        self.msg2.setWindowTitle('Book Match')
        self.msg2.setIcon(QtWidgets.QMessageBox.Information)
        self.msg2.setStyleSheet("background-color: white;"
                                "font-weight: bold;"
                                "color: black;"
                                "font-size: 13")
        self.msg2.setText(message)
        self.msg2.show()

    ###### transition screens####
    def b_update_update(self):
        self.b_update_view(False)
        self.Bupdate()

    def update_home(self):
        self.update_view(False)
        self.home_screen()

    def b_update_home(self):
        self.b_update_view(False)
        self.home_screen()

    def home_b_update(self):
        self.bt1.hide()
        self.bt2.hide()
        self.bt3.hide()
        self.bt4.hide()
        self.bt5.hide()
        self.bt6.hide()
        self.bt7.hide()
        self.lb3.hide()
        self.lb4.hide()
        self.lb5.hide()
        self.lb6.hide()
        self.b_update()

    def login_to_home(self):
        self.login_screen_view(False)
        self.home_screen()

    def logout(self):
        self.home_screen_view(False)
        self.login_screen()

    def home_screen_add(self):
        self.bt1.hide()
        self.bt2.hide()
        self.bt3.hide()
        self.bt4.hide()
        self.bt5.hide()
        self.bt6.hide()
        self.bt7.hide()
        self.lb3.hide()
        self.lb4.hide()
        self.lb5.hide()
        self.lb6.hide()
        self.add()

    def add_home_screen(self):
        self.add_view(False)
        self.home_screen()

    def home_screen_delete(self):
        self.bt1.hide()
        self.bt2.hide()
        self.bt3.hide()
        self.bt4.hide()
        self.bt5.hide()
        self.bt6.hide()
        self.bt7.hide()
        self.lb3.hide()
        self.lb4.hide()
        self.lb5.hide()
        self.lb6.hide()
        self.delete()

    def delete_home(self):
        self.delete_view(False)
        self.home_screen()

    def home_search(self):
        self.bt1.hide()
        self.bt2.hide()
        self.bt3.hide()
        self.bt4.hide()
        self.bt5.hide()
        self.bt6.hide()
        self.bt7.hide()
        self.lb3.hide()
        self.lb4.hide()
        self.lb5.hide()
        self.lb6.hide()
        self.search()

    def search_home(self):
        self.search_view(False)
        self.home_screen()

    def home_profile(self):
        self.bt1.hide()
        self.bt2.hide()
        self.bt3.hide()
        self.bt4.hide()
        self.bt5.hide()
        self.bt6.hide()
        self.bt7.hide()
        self.lb3.hide()
        self.lb4.hide()
        self.lb5.hide()
        self.lb6.hide()
        self.profile()

    def profile_home(self):
        self.profile_view(False)
        self.home_screen()

    def allbooks_home(self):
        self.view_allbooks(False)
        self.home_screen()

    def home_allbooks(self):
        self.bt1.hide()
        self.bt2.hide()
        self.bt3.hide()
        self.bt4.hide()
        self.bt5.hide()
        self.bt6.hide()
        self.bt7.hide()
        self.lb3.hide()
        self.lb4.hide()
        self.lb5.hide()
        self.lb6.hide()
        self.all_books()

    ## hide and show widgets ####

    def update_view(self, ordre):
        if ordre == True:
            self.liness1.show()
            self.liness2.show()
            self.liness3.show()
            self.liness4.show()
            self.liness5.show()
            self.boto1.show()
            self.boto2.show()
        if ordre == False:
            self.liness1.hide()
            self.liness2.hide()
            self.liness3.hide()
            self.liness4.hide()
            self.liness5.hide()
            self.boto1.hide()
            self.boto2.hide()

    def login_screen_view(self, ordre):
        if ordre == False:
            self.btn1.hide()
            self.lab.hide()
            self.box2.hide()
            self.box1.hide()
        if ordre == True:
            self.btn1.show()
            self.lab.show()
            self.box2.show()
            self.box1.show()

    def home_screen_view(self, ordre):
        if ordre == True:
            self.bt1.show()
            self.bt2.show()
            self.bt3.show()
            self.bt4.show()
            self.bt5.show()
            self.bt6.show()
            self.bt7.show()
            self.lb.show()
            self.lb2.show()
            self.lb3.show()
            self.lb4.show()
            self.lb5.show()
            self.lb6.show()
        if ordre == False:
            self.bt1.hide()
            self.bt2.hide()
            self.bt3.hide()
            self.bt4.hide()
            self.bt5.hide()
            self.bt6.hide()
            self.bt7.hide()
            self.lb.hide()
            self.lb2.hide()
            self.lb3.hide()
            self.lb4.hide()
            self.lb5.hide()
            self.lb6.hide()

    def add_view(self, ordre):
        if ordre == True:
            self.bn1.show()
            self.bn2.show()
            self.bn3.show()
            self.bn4.show()
            self.bn5.show()
            self.butt1.show()
            self.butt2.show()
        if ordre == False:
            self.bn1.hide()
            self.bn2.hide()
            self.bn3.hide()
            self.bn4.hide()
            self.bn5.hide()
            self.butt1.hide()
            self.butt2.hide()

    def delete_view(self, ordre):
        if ordre == True:
            self.button1.show()
            self.button2.show()
            self.ligne.show()
        if ordre == False:
            self.button1.hide()
            self.button2.hide()
            self.ligne.hide()

    def search_view(self, ordre):
        if ordre == True:
            self.lig.show()
            self.butto1.show()
            self.butto2.show()
        if ordre == False:
            self.lig.hide()
            self.butto1.hide()
            self.butto2.hide()

    def profile_view(self, ordre):
        if ordre == True:
            self.bo1.show()
            self.bo2.show()
            self.li1.show()
            self.li2.show()
            self.li3.show()
        if ordre == False:
            self.bo1.hide()
            self.bo2.hide()
            self.li1.hide()
            self.li2.hide()
            self.li3.hide()

    def view_allbooks(self, ordre):
        if ordre == True:
            self.boto1.show()
            self.boto2.show()
            self.tblTable.show()
        if ordre == False:
            self.boto2.hide()
            self.boto1.hide()
            self.tblTable.hide()

    def update_view(self, ordre):
        if ordre == True:
            self.liness1.show()
            self.liness2.show()
            self.boto1.show()
            self.boto2.show()
        if ordre == False:
            self.liness1.hide()
            self.liness2.hide()
            self.boto1.hide()
            self.boto2.hide()

    def b_update_view(self,ordre):
        if ordre == True:
            self.lignes.show()
            self.buttons1.show()
            self.buttons2.show()
        if ordre == False:
            self.lignes.hide()
            self.buttons1.hide()
            self.buttons2.hide()
    ### main view functions ####"
    # 000018

    def login_screen(self):
        self.setGeometry(200, 200, 800, 470)
        self.setWindowTitle('Library Management System')
        self.setStyleSheet("background-color: white")
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(QtCore.QRect(285, 330, 211, 51))
        self.btn1.setText('Login')
        self.btn1.setFont(QtGui.QFont('Arial', 11))
        self.btn1.setStyleSheet("background-color: black;"
                                "border :1px solid;"
                                "border-color: black;"
                                "border-radius: 10px;"
                                "font-weight: bold;"
                                "color: white")
        self.btn1.clicked.connect(self.check_login)
        self.box1 = QtWidgets.QLineEdit(self)
        self.box1.setGeometry(QtCore.QRect(250, 190, 281, 41))
        self.box1.setStyleSheet("background-color: white;"
                                "border :2px solid;"
                                "border-top-color: white;"
                                "border-right-color: white;"
                                "border-bottom-color: black;"
                                "border-left-color: white;"
                                "font-weight: bold;")
        self.box1.setPlaceholderText('Username')
        self.box1.setFont(QtGui.QFont('Arial', 12))
        self.box2 = QtWidgets.QLineEdit(self)
        self.box2.setPlaceholderText('Password')
        self.box2.setFont(QtGui.QFont('Arial', 12))
        self.box2.setStyleSheet("background-color: white;"
                                "border :2px solid;"
                                "border-top-color: white;"
                                "border-right-color: white;"
                                "border-bottom-color: black;"
                                "border-left-color: white;"
                                "font-weight: bold;")
        self.box2.setGeometry(QtCore.QRect(250, 250, 281, 41))
        self.box2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lab = QtWidgets.QLabel(self)
        self.lab.setGeometry(QtCore.QRect(330, 40, 128, 128))
        self.lab.setPixmap(QtGui.QPixmap('main_icon.png'))
        self.show()
        self.login_screen_view(True)

    def home_screen(self):
        self.lb = QtWidgets.QLabel(self)
        self.lb.setGeometry(QtCore.QRect(0, 0, 191, 471))
        self.lb.setStyleSheet("background-color: black")
        self.lb2 = QtWidgets.QLabel(self)
        self.lb2.setGeometry(QtCore.QRect(30, 20, 128, 138))
        self.lb2.setStyleSheet("background-color: black")
        self.lb2.setPixmap(QtGui.QPixmap('main_icon2.png'))
        self.lb3 = QtWidgets.QLabel(self)
        self.lb3.setGeometry(QtCore.QRect(190, 100, 611, 20))
        self.lb3.setStyleSheet("background-color: black")
        self.lb4 = QtWidgets.QLabel(self)
        self.lb4.setGeometry(QtCore.QRect(420, 30, 128, 138))
        self.lb4.setStyleSheet("background-color: white")
        self.lb4.setPixmap(QtGui.QPixmap('main_icon.png'))
        self.lb5 = QtWidgets.QLabel(self)
        self.lb5.setGeometry(QtCore.QRect(320, 240, 128, 138))
        self.lb5.setStyleSheet("background-color: white")
        self.lb5.setPixmap(QtGui.QPixmap('admin_w.png'))
        self.lb6 = QtWidgets.QLabel(self)
        self.lb6.setGeometry(QtCore.QRect(510, 270, 111, 31))
        self.lb6.setFont(QtGui.QFont('Arial', 11))
        self.lb6.setText('Edit Profile')
        self.lb6.setStyleSheet("background-color: white;"
                               "font-weight: bold;"
                               "color: black")
        self.bt1 = QtWidgets.QPushButton(self)
        self.bt1.setGeometry(QtCore.QRect(5, 170, 181, 41))
        self.bt1.setText('Add')
        self.bt1.setFont(QtGui.QFont('Arial', 11))
        self.bt1.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: white;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt1.clicked.connect(self.home_screen_add)
        self.bt2 = QtWidgets.QPushButton(self)
        self.bt2.setGeometry(QtCore.QRect(5, 220, 181, 41))
        self.bt2.setText('Delete')
        self.bt2.setFont(QtGui.QFont('Arial', 11))
        self.bt2.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: white;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt2.clicked.connect(self.home_screen_delete)
        self.bt3 = QtWidgets.QPushButton(self)
        self.bt3.setGeometry(QtCore.QRect(5, 270, 181, 41))
        self.bt3.setText('Update')
        self.bt3.setFont(QtGui.QFont('Arial', 11))
        self.bt3.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: white;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt3.clicked.connect(self.home_b_update)
        self.bt4 = QtWidgets.QPushButton(self)
        self.bt4.setGeometry(QtCore.QRect(5, 320, 181, 41))
        self.bt4.setText('AllBooks')
        self.bt4.setFont(QtGui.QFont('Arial', 11))
        self.bt4.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: white;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt4.clicked.connect(self.home_allbooks)
        self.bt5 = QtWidgets.QPushButton(self)
        self.bt5.setGeometry(QtCore.QRect(5, 370, 181, 41))
        self.bt5.setText('Search')
        self.bt5.setFont(QtGui.QFont('Arial', 11))
        self.bt5.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: white;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt5.clicked.connect(self.home_search)
        self.bt6 = QtWidgets.QPushButton(self)
        self.bt6.setGeometry(QtCore.QRect(5, 420, 181, 41))
        self.bt6.setText('Logout')
        self.bt6.setFont(QtGui.QFont('Arial', 11))
        self.bt6.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: white;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt6.clicked.connect(self.logout)
        self.bt7 = QtWidgets.QPushButton(self)
        self.bt7.setGeometry(QtCore.QRect(510, 320, 181, 41))
        self.bt7.setText('Edit')
        self.bt7.setFont(QtGui.QFont('Arial', 11))
        self.bt7.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: black;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bt7.clicked.connect(self.home_profile)

        self.home_screen_view(True)

    def add(self):
        self.bn1 = QtWidgets.QLineEdit(self)
        self.bn1.setGeometry(QtCore.QRect(260, 70, 371, 41))
        self.bn1.setFont(QtGui.QFont('Arial', 12))
        self.bn1.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.bn1.setPlaceholderText('ID')
        self.bn2 = QtWidgets.QLineEdit(self)
        self.bn2.setGeometry(QtCore.QRect(260, 130, 371, 41))
        self.bn2.setFont(QtGui.QFont('Arial', 12))
        self.bn2.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.bn2.setPlaceholderText('Title')
        self.bn3 = QtWidgets.QLineEdit(self)
        self.bn3.setGeometry(QtCore.QRect(260, 190, 371, 41))
        self.bn3.setFont(QtGui.QFont('Arial', 12))
        self.bn3.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.bn3.setPlaceholderText('Author')
        self.bn4 = QtWidgets.QLineEdit(self)
        self.bn4.setGeometry(QtCore.QRect(260, 250, 371, 41))
        self.bn4.setFont(QtGui.QFont('Arial', 12))
        self.bn4.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.bn4.setPlaceholderText('Price')
        self.bn5 = QtWidgets.QLineEdit(self)
        self.bn5.setGeometry(QtCore.QRect(260, 310, 371, 41))
        self.bn5.setFont(QtGui.QFont('Arial', 12))
        self.bn5.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.bn5.setPlaceholderText('Quantity')
        self.butt1 = QtWidgets.QPushButton(self)
        self.butt1.setGeometry(QtCore.QRect(360, 380, 181, 41))
        self.butt1.setText('ADD')
        self.butt1.setFont(QtGui.QFont('Arial', 11))
        self.butt1.setStyleSheet("background-color: black;"
                                 "border :1px solid;"
                                 "border-color: black;"
                                 "border-radius: 10px;"
                                 "font-weight: bold;"
                                 "color: white")
        self.butt1.clicked.connect(self.table)
        self.butt2 = QtWidgets.QPushButton(self)
        self.butt2.setGeometry(QtCore.QRect(700, 380, 81, 41))
        self.butt2.setText('Cancel')
        self.butt2.setFont(QtGui.QFont('Arial', 11))
        self.butt2.setStyleSheet("background-color: black;"
                                 "border :1px solid;"
                                 "border-color: black;"
                                 "border-radius: 10px;"
                                 "font-weight: bold;"
                                 "color: white")
        self.butt2.clicked.connect(self.add_home_screen)
        self.add_view(True)

    def delete(self):
        self.ligne = QtWidgets.QLineEdit(self)
        self.ligne.setGeometry(QtCore.QRect(260, 160, 371, 41))
        self.ligne.setFont(QtGui.QFont('Arial', 12))
        self.ligne.setStyleSheet("background-color: white;"
                                 "border :2px solid;"
                                 "border-top-color: white;"
                                 "border-right-color: white;"
                                 "border-bottom-color: black;"
                                 "border-left-color: white;"
                                 "font-weight: bold;")
        self.ligne.setPlaceholderText('Title')
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(QtCore.QRect(350, 240, 181, 41))
        self.button1.setText('Delete')
        self.button1.setFont(QtGui.QFont('Arial', 11))
        self.button1.setStyleSheet("background-color: black;"
                                   "border :1px solid;"
                                   "border-color: black;"
                                   "border-radius: 10px;"
                                   "font-weight: bold;"
                                   "color: white")
        self.button1.clicked.connect(self.delete_book)
        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setGeometry(QtCore.QRect(700, 410, 81, 41))
        self.button2.setText('Cancel')
        self.button2.setFont(QtGui.QFont('Arial', 11))
        self.button2.setStyleSheet("background-color: black;"
                                   "border :1px solid;"
                                   "border-color: black;"
                                   "border-radius: 10px;"
                                   "font-weight: bold;"
                                   "color: white")
        self.button2.clicked.connect(self.delete_home)
        self.delete_view(True)

    def search(self):
        self.lig = QtWidgets.QLineEdit(self)
        self.lig.setGeometry(QtCore.QRect(280, 140, 381, 41))
        self.lig.setFont(QtGui.QFont('Arial', 12))
        self.lig.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.lig.setPlaceholderText('Title Of The Book')
        self.butto1 = QtWidgets.QPushButton(self)
        self.butto1.setGeometry(QtCore.QRect(380, 230, 181, 41))
        self.butto1.setText('Search')
        self.butto1.setFont(QtGui.QFont('Arial', 11))
        self.butto1.setStyleSheet("background-color: black;"
                                  "border :1px solid;"
                                  "border-color: black;"
                                  "border-radius: 10px;"
                                  "font-weight: bold;"
                                  "color: white")
        self.butto1.clicked.connect(self.show_book)
        self.butto2 = QtWidgets.QPushButton(self)
        self.butto2.setGeometry(QtCore.QRect(430, 410, 81, 41))
        self.butto2.setText('Cancel')
        self.butto2.setFont(QtGui.QFont('Arial', 11))
        self.butto2.setStyleSheet("background-color: black;"
                                  "border :1px solid;"
                                  "border-color: black;"
                                  "border-radius: 10px;"
                                  "font-weight: bold;"
                                  "color: white")
        self.butto2.clicked.connect(self.search_home)

        self.search_view(True)

    def profile(self):
        self.bo1 = QtWidgets.QPushButton(self)
        self.bo1.setGeometry(QtCore.QRect(370, 300, 181, 41))
        self.bo1.setText('Edit')
        self.bo1.setFont(QtGui.QFont('Arial', 11))
        self.bo1.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: black;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bo1.clicked.connect(self.upadmin)

        self.bo2 = QtWidgets.QPushButton(self)
        self.bo2.setGeometry(QtCore.QRect(420, 410, 81, 41))
        self.bo2.setText('Cancel')
        self.bo2.setFont(QtGui.QFont('Arial', 11))
        self.bo2.setStyleSheet("background-color: black;"
                               "border :1px solid;"
                               "border-color: black;"
                               "border-radius: 10px;"
                               "font-weight: bold;"
                               "color: white")
        self.bo2.clicked.connect(self.profile_home)

        self.li1 = QtWidgets.QLineEdit(self)
        self.li1.setGeometry(QtCore.QRect(270, 90, 381, 41))
        self.li1.setFont(QtGui.QFont('Arial', 12))
        self.li1.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.li1.setPlaceholderText('Useraname')
        self.li2 = QtWidgets.QLineEdit(self)
        self.li2.setGeometry(QtCore.QRect(270, 160, 381, 41))
        self.li2.setFont(QtGui.QFont('Arial', 12))
        self.li2.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.li2.setPlaceholderText('New Password')
        self.li3 = QtWidgets.QLineEdit(self)
        self.li3.setGeometry(QtCore.QRect(270, 230, 381, 41))
        self.li3.setFont(QtGui.QFont('Arial', 12))
        self.li3.setStyleSheet("background-color: white;"
                               "border :2px solid;"
                               "border-top-color: white;"
                               "border-right-color: white;"
                               "border-bottom-color: black;"
                               "border-left-color: white;"
                               "font-weight: bold;")
        self.li3.setPlaceholderText('Password')
        self.li3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.profile_view(True)

    def all_books(self):
        self.tblTable = QtWidgets.QTableWidget(self)
        self.tblTable.setGeometry(QtCore.QRect(230, 11, 521, 331))
        self.tblTable.setRowCount(5)
        self.tblTable.setColumnCount(5)
        self.tblTable.setHorizontalHeaderLabels(['ID', 'Title', 'Author', 'Price', 'Qunatity'])
        self.tblTable.setFont(QtGui.QFont('Arial', 11))
        # self.setStyleSheet( "font-weight: bold;")
        self.boto1 = QtWidgets.QPushButton(self)
        self.boto1.setGeometry(QtCore.QRect(420, 360, 141, 41))
        self.boto1.setText('Load')
        self.boto1.setFont(QtGui.QFont('Arial', 11))
        self.boto1.setStyleSheet("background-color: black;"
                                 "border :1px solid;"
                                 "border-color: black;"
                                 "border-radius: 10px;"
                                 "font-weight: bold;"
                                 "color: white")
        self.boto1.clicked.connect(self.list_books)
        self.boto2 = QtWidgets.QPushButton(self)
        self.boto2.setGeometry(QtCore.QRect(460, 420, 71, 41))
        self.boto2.setText('Cancel')
        self.boto2.setFont(QtGui.QFont('Arial', 11))
        self.boto2.setStyleSheet("background-color: black;"
                                 "border :1px solid;"
                                 "border-color: black;"
                                 "border-radius: 10px;"
                                 "font-weight: bold;"
                                 "color: white")
        self.boto2.clicked.connect(self.allbooks_home)
        self.view_allbooks(True)

    def b_update(self):
        self.lignes = QtWidgets.QLineEdit(self)
        self.lignes.setGeometry(QtCore.QRect(260, 160, 371, 41))
        self.lignes.setFont(QtGui.QFont('Arial', 12))
        self.lignes.setStyleSheet("background-color: white;"
                                  "border :2px solid;"
                                  "border-top-color: white;"
                                  "border-right-color: white;"
                                  "border-bottom-color: black;"
                                  "border-left-color: white;"
                                  "font-weight: bold;")
        self.lignes.setPlaceholderText('Title')
        self.buttons1 = QtWidgets.QPushButton(self)
        self.buttons1.setGeometry(QtCore.QRect(350, 240, 181, 41))
        self.buttons1.setText('Continue')
        self.buttons1.setFont(QtGui.QFont('Arial', 11))
        self.buttons1.setStyleSheet("background-color: black;"
                                    "border :1px solid;"
                                    "border-color: black;"
                                    "border-radius: 10px;"
                                    "font-weight: bold;"
                                    "color: white")
        self.buttons1.clicked.connect(self.b_update_logic)
        self.buttons2 = QtWidgets.QPushButton(self)
        self.buttons2.setGeometry(QtCore.QRect(700, 410, 81, 41))
        self.buttons2.setText('Cancel')
        self.buttons2.setFont(QtGui.QFont('Arial', 11))
        self.buttons2.setStyleSheet("background-color: black;"
                                    "border :1px solid;"
                                    "border-color: black;"
                                    "border-radius: 10px;"
                                    "font-weight: bold;"
                                    "color: white")
        self.buttons2.clicked.connect(self.b_update_home)
        self.b_update_view(True)

    def Bupdate(self):
        self.liness1 = QtWidgets.QLineEdit(self)
        self.liness1.setGeometry(QtCore.QRect(270,160, 371, 41))
        self.liness1.setFont(QtGui.QFont('Arial', 12))
        self.liness1.setStyleSheet("background-color: white;"
                                   "border :2px solid;"
                                   "border-top-color: white;"
                                   "border-right-color: white;"
                                   "border-bottom-color: black;"
                                   "border-left-color: white;"
                                   "font-weight: bold;")
        self.liness1.setPlaceholderText('Price')
        self.liness2 = QtWidgets.QLineEdit(self)
        self.liness2.setGeometry(QtCore.QRect(270, 230, 371, 41))
        self.liness2.setFont(QtGui.QFont('Arial', 12))
        self.liness2.setStyleSheet("background-color: white;"
                                   "border :2px solid;"
                                   "border-top-color: white;"
                                   "border-right-color: white;"
                                   "border-bottom-color: black;"
                                   "border-left-color: white;"
                                   "font-weight: bold;")
        self.liness2.setPlaceholderText('Quantity')

        self.boto1 = QtWidgets.QPushButton(self)
        self.boto1.setGeometry(QtCore.QRect(370, 300, 181, 41))
        self.boto1.setText('Update')
        self.boto1.setFont(QtGui.QFont('Arial', 11))
        self.boto1.setStyleSheet("background-color: black;"
                                 "border :1px solid;"
                                 "border-color: black;"
                                 "border-radius: 10px;"
                                 "font-weight: bold;"
                                 "color: white")
        self.boto1.clicked.connect(self.bupdate_logic)
        self.boto2 = QtWidgets.QPushButton(self)
        self.boto2.setGeometry(QtCore.QRect(420, 410, 81, 41))
        self.boto2.setText('Cancel')
        self.boto2.setFont(QtGui.QFont('Arial', 11))
        self.boto2.setStyleSheet("background-color: black;"
                                 "border :1px solid;"
                                 "border-color: black;"
                                 "border-radius: 10px;"
                                 "font-weight: bold;"
                                 "color: white")
        self.boto2.clicked.connect(self.update_home)

        self.update_view(True)
    ###databse and logic ######

    def check_login(self):
        self.usr = self.box1.text()
        pss = self.box2.text()
        exit = sqlite3.connect('donnes.db')
        result = exit.execute("SELECT * FROM ADMIN WHERE username = ? AND passe = ?", (self.usr, pss))
        if (len(result.fetchall()) > 0):
            self.login_to_home()
            exit.close()
        else:
            mes = 'Username or Password incorrect'
            self.warning(mes)

    def table(self):
        id = self.bn1.text()
        titre = self.bn2.text()
        author = self.bn3.text()
        price = self.bn4.text()
        quant = self.bn5.text()
        exit = sqlite3.connect('donnes.db')
        exit.execute("INSERT INTO BOOKS VALUES(?,?,?,?,?)", (id, titre, author, price, quant))
        exit.commit()
        exit.close()
        txt = 'Done Successfully'
        self.information(txt)
        self.add_view(False)
        self.add()

    def show_book(self):
        nom = self.lig.text()
        conn = sqlite3.connect('donnes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from BOOKS WHERE Nom = ?", (nom,))
        result = cursor.fetchall()
        conn.commit()
        if (len(result) > 0):
            txt1 = ("Book ID :" + "  " + str(result[0][0]) + "\n"
                                                             "Title :" + "  " + str(result[0][1]) + "\n" +
                    "Author :" + "  " + str(result[0][2]) + "\n" +
                    "Price :" + "  " + str(result[0][3]) + "\n" +
                    "Quantity :" + "  " + str(result[0][4]))

            self.text(txt1)
            conn.close()



        else:
            txt = 'This Is Not Available'
            self.warning(txt)
        # self.search()

    def delete_book(self):
        titre = self.ligne.text()
        exit = sqlite3.connect('donnes.db')
        exit.execute("DELETE FROM BOOKS WHERE Nom = ?", (titre,))
        exit.commit()
        exit.close()
        txt = 'Done Successfully'
        self.information(txt)
        self.delete_view(False)
        self.delete()

    def upadmin(self):
        pss = self.li3.text()
        exit = sqlite3.connect('donnes.db')
        result = exit.execute("SELECT * FROM ADMIN WHERE passe = ?", (pss,))
        if (len(result.fetchall()) > 0):
            user = self.li1.text()
            ps = self.li2.text()
            exit.execute("UPDATE ADMIN SET username = ? ,passe = ? WHERE id = 1 ", (user, ps))
            exit.commit()
            txt = 'Upadted Successfully'
            self.information(txt)
            exit.close()
        else:
            msg = 'Password Incorrect'
            self.warning(msg)

    def list_books(self):
        exit = sqlite3.connect('donnes.db')
        query = "SELECT * FROM BOOKS"
        result = exit.execute(query)
        self.tblTable.setRowCount(0)
        for row, form in enumerate(result):
            self.tblTable.insertRow(row)
            for column, item in enumerate(form):
                self.tblTable.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
        exit.close()

    def b_update_logic(self):
        self.usr = self.lignes.text()
        exit = sqlite3.connect('donnes.db')
        result = exit.execute("SELECT * FROM BOOKS WHERE Nom = ?", (self.usr,))
        if (len(result.fetchall()) > 0):
            self.b_update_update()
            exit.close()
        else:
            mes = 'Book don\'t exist'
            self.warning(mes)
            exit.close()

    def bupdate_logic(self):
        exit = sqlite3.connect('donnes.db')
        cursor = exit.cursor()
        cursor.execute("SELECT * FROM BOOKS WHERE Nom = ?", (self.usr,))
        result = cursor.fetchall()
        exit.commit()
        if (len(result) > 0):
            print(result)
            if self.liness1.text():
                price = self.liness1.text()
            else:
                price = result[0][3]
            if self.liness2.text():
                quan = self.liness2.text()
            else:
                quan = result[0][4]
            exit.execute("UPDATE BOOKS SET Prix = ? ,Quantiter = ? WHERE Nom = ? ", (price, quan, self.usr))
            exit.commit()
            txt = 'Book Updated Successfully'
            self.information(txt)

        exit.close()


def main():
    app = QApplication(sys.argv)
    win = window()
    win.login_screen()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()