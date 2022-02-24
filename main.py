from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_2.setText(
            _translate("MainWindow", "Добавить/редактировать"))


class Ui_AddWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_id.setObjectName("line_id")
        self.verticalLayout.addWidget(self.line_id)
        self.line_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_name.setObjectName("line_name")
        self.verticalLayout.addWidget(self.line_name)
        self.line_roast = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_roast.setObjectName("line_roast")
        self.verticalLayout.addWidget(self.line_roast)
        self.line_type = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_type.setObjectName("line_type")
        self.verticalLayout.addWidget(self.line_type)
        self.line_taste = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_taste.setObjectName("line_taste")
        self.verticalLayout.addWidget(self.line_taste)
        self.line_cost = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_cost.setObjectName("line_cost")
        self.verticalLayout.addWidget(self.line_cost)
        self.line_size = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_size.setObjectName("line_size")
        self.verticalLayout.addWidget(self.line_size)
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 271, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_id.setPlaceholderText(
            _translate("MainWindow", "ID (При создании оставить пустым)"))
        self.line_name.setPlaceholderText(_translate("MainWindow", "Название"))
        self.line_roast.setPlaceholderText(
            _translate("MainWindow", "Степень обжарки"))
        self.line_type.setPlaceholderText(
            _translate("MainWindow", "Тип(молотый/в зернах)"))
        self.line_taste.setPlaceholderText(
            _translate("MainWindow", "Описание вкуса"))
        self.line_cost.setPlaceholderText(_translate("MainWindow", "Цена"))
        self.line_size.setPlaceholderText(
            _translate("MainWindow", "Объем упаковки"))
        self.button_add.setText(
            _translate("MainWindow", "Добавить/редактировать"))


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('data\coffee.sqlite')
        self.cur = self.con.cursor()

        self.pushButton.clicked.connect(self.update_base)
        self.pushButton_2.clicked.connect(self.add_item)
        self.drawing = True
        self.initUI()
        self.update_base()

    def initUI(self):
        self.setWindowTitle('Кофе')
        self.show()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            'ID',
            'Название',
            'Обжарка',
            'Тип',
            'Вкус',
            'Цена',
            'Объем'
        ])

    def update_base(self):
        self.info = self.cur.execute('SELECT * FROM coffee').fetchall()
        self.tableWidget.setRowCount(0)
        for i, lst in enumerate(self.info):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for s, item in enumerate(lst):
                self.tableWidget.setItem(i, s, QTableWidgetItem(str(item)))
        self.tableWidget.resizeColumnsToContents()

    def add_item(self):
        self.add_window = EditCoffee()
        self.add_window.show()


class EditCoffee(QMainWindow, Ui_AddWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('data\coffee.sqlite')
        self.cur = self.con.cursor()

        self.button_add.clicked.connect(self.add_item)

    def add_item(self):
        name = self.line_name.text()
        coffee_id = self.line_id.text()
        cost = self.line_cost.text()
        taste = self.line_taste.text()
        coffee_type = self.line_type.text()
        size = self.line_size.text()
        roast = self.line_roast.text()

        if coffee_id:
            lst = []
            lst_request = []
            if name:
                lst_request.append('name = ?')
                lst.append(name)
            if roast:
                lst_request.append('roast = ?')
                lst.append(roast)
            if coffee_type:
                lst_request.append('type = ?')
                lst.append(coffee_type)
            if taste:
                lst_request.append('taste = ?')
                lst.append(taste)
            if cost:
                lst_request.append('cost = ?')
                lst.append(cost)
            if size:
                lst_request.append('size = ?')
                lst.append(size)
            request = '''UPDATE coffee
                         SET {}
                         WHERE id = ?'''.format(', '.join(lst_request))
            self.cur.execute(request, (*lst, coffee_id))

        elif name and cost and taste and coffee_type and size and roast and not coffee_id:
            self.cur.execute(
                'INSERT INTO coffee(name, roast, type, taste, cost, size)'
                ' VALUES(?, ?, ?, ?, ?, ?)', (name, roast, coffee_type,
                                              taste, int(cost), int(size)))
        self.con.commit()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    sys.exit(app.exec_())
