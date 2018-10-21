
import sys
import os
from PyQt5 import QtWidgets 
import mf
###
class ExampleApp(QtWidgets.QMainWindow, mf.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.pushButton.clicked.connect(self.browse_sf)

    def browse_sf(self):
        #self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Select directory") 
        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
