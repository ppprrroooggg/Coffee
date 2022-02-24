from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sys
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        self.pushButton.clicked.connect(self.update_base)
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


class EditCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.con = sqlite3.connect('coffee.sqlite')
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