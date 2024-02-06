import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3


class CoffeeApp(QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Информация о кофе')

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM coffee')
        coffee_data = cursor.fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(coffee_data))
        self.tableWidget.setColumnCount(7)

        headers = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 'Описание вкуса', 'Цена', 'Объем упаковки']
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row_num, row_data in enumerate(coffee_data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
