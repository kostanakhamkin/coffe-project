import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog
import sys


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("CoffeeInfo")
        self.show_table()
        self.pushButton.clicked.connect(self.add_info)

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

    def add_info(self):
        sn, b = QInputDialog.getText(self, 'Введите данные', 'Название сорта', False)
        roastid, b = QInputDialog.getInt(self, 'Введите данные', 'Id обжарки', 0, 0, 7, False)
        condition, b = QInputDialog.getInt(self, 'Введите данные', 'Id состояния', 0, 0, 1, False)
        description, b = QInputDialog.getText(self, 'Введите данные', 'Описание', False)
        price, b = QInputDialog.getInt(self, 'Введите данные', 'Цена', False)
        volume, b = QInputDialog.getInt(self, 'Введите данные', 'Размер упаковки', False)
        print([sn, roastid, condition, description, price, volume])
        con = sqlite3.connect("coffee.sqlite.db")
        cur = con.cursor()
        print(type(self.id))
        print(type(3))
        con.execute("INSERT INTO coffee_types(Сорт, Обжарка, Состояние, Описание, Цена, Объем)"
                    " VALUES (?,?,?,?,?,?)", (sn, roastid, condition, description, price, volume))
        print(4)
        self.id += 1
        print(1)
        con.commit()
        print(2)
        self.show_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CoffeeInfo()
    w.show()
    sys.exit(app.exec_())
