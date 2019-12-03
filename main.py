import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog, QWidget
import sys


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("CoffeeInfo")
        self.show_table()
        self.pushButton.clicked.connect(self.open_form)

    def show_table(self):
        self.CoffeeTable.setRowCount(0)
        con = sqlite3.connect("coffee.sqlite.db")
        cur = con.cursor()
        headers = con.execute("""PRAGMA table_info(coffee_types)""")
        headers = [i[1] for i in headers]
        self.CoffeeTable.setColumnCount(len(headers))
        self.CoffeeTable.setHorizontalHeaderLabels(headers)
        info = cur.execute("SELECT * FROM coffee_types").fetchall()
        for ri, r in enumerate(info):
            self.CoffeeTable.setRowCount(self.CoffeeTable.rowCount() + 1)
            for ci, c in enumerate(r):
                if ci == 2:
                    c = cur.execute("""SELECT name FROM roast_table
                                WHERE id = ?""", (c,)).fetchone()[0]
                elif ci == 3:
                    c = cur.execute("""SELECT condition FROM coffee_condition
                                    WHERE id = ?""", (c,)).fetchone()[0]
                elif ci == 0:
                    self.id = c
                self.CoffeeTable.setItem(ri, ci, QTableWidgetItem(str(c)))

    def open_form(self):
        self.aw = AddInfoForm(self)
        self.aw.show()


class AddInfoForm(QWidget):
    def __init__(self, sender):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle("AddInfo")
        self.sender = sender
        self.pushButton.clicked.connect(self.add_info)

    def add_info(self):
        sort = self.isort.text()
        roast = self.iroast.currentText()
        cond = self.icond.currentText()
        desc = self.idesc.toPlainText()
        price = self.iprice.value()
        vol = self.ivol.value()
        con = sqlite3.connect("coffee.sqlite.db")
        cur = con.cursor()
        roastid = cur.execute("SELECT id From roast_table WHERE name = ?", (roast, )).fetchone()[0]
        condid = cur.execute("SELECT id From coffee_condition WHERE condition = ?", (cond, )).fetchone()[0]
        con.execute("INSERT INTO coffee_types(Сорт, Обжарка, Состояние, Описание, Цена, Объем)"
                    " VALUES (?,?,?,?,?,?)", (sort, roastid, condid, desc, price, vol))
        con.commit()
        self.sender.show_table()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CoffeeInfo()
    w.show()
    sys.exit(app.exec_())
