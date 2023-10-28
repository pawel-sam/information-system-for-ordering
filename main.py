import sys
from functools import partial
from PyQt5.QtCore import QPropertyAnimation, QStringListModel
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_main import *

dictionary = {1: 'Сухой корм вкус курицы',
              2: 'Сухой корм вкус индейки',
              3: 'Жидкий корм вкус рыбы',
              4: 'Жидкий корм вкус томата',
              5: 'Игрушка с ароматизатором курицы',
              6: 'Игрушка с ароматизатором мяты',
              7: 'Игрушка в виде серой мыши',
              8: 'Игрушка в виде воробья',
              9: 'Крупный древесный наполнитель',
              10: 'Мелкий древесный наполнитель'}

dictionary_2 = {1: 'Корма',
                2: 'Игрушки',
                3: 'Наполнители',
                4: 'Лекарственные препараты',
                5: 'Средства гигиены',
                6: 'Одежда'}


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.animation = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.frame_left_menu.enterEvent = self.button_hovered
        self.ui.frame_left_menu.leaveEvent = self.button_left
        self.ui.catalog.clicked.connect(partial(self.ui.Widget_pages.setCurrentWidget, self.ui.page_catalog))
        self.ui.categories.clicked.connect(partial(self.ui.Widget_pages.setCurrentWidget, self.ui.page_categories))

        data_list = [f'{key}: {value}' for key, value in dictionary.items()]
        model = QStringListModel(data_list)
        self.ui.list_products.setModel(model)

        data_list = [f'{key}: {value}' for key, value in dictionary_2.items()]
        model = QStringListModel(data_list)
        self.ui.list_categories.setModel(model)

    def button_hovered(self, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = 250
            standard = 70
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def button_left(self, enable):
        width = self.ui.frame_left_menu.width()
        maxExtend = 250
        standard = 70
        if width == 70:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        if enable:
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(standard)
            self.animation.setEndValue(widthExtended)
            self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())
