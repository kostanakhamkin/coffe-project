import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("CoffeeInfo")
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
                self.CoffeeTable.setItem(ri, ci, QTableWidgetItem(str(c)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CoffeeInfo()
    w.show()
    sys.exit(app.exec_())
