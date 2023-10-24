# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 572)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Bar = QtWidgets.QFrame(self.centralwidget)
        self.Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Bar.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bar.setObjectName("Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QtWidgets.QFrame(self.Bar)
        self.frame_menu.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_menu.setStyleSheet("background-color: rgb(194, 150, 95);")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_btn_menu = QtWidgets.QFrame(self.Bar)
        self.frame_btn_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn_menu.setObjectName("frame_btn_menu")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_btn_menu)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_btn_menu)
        self.label.setStyleSheet("font: 87 8pt \"Montserrat Black\";")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_btn_menu)
        self.verticalLayout.addWidget(self.Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_for_btn = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_for_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_for_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_btn.setObjectName("frame_for_btn")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_for_btn)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_categories = QtWidgets.QPushButton(self.frame_for_btn)
        self.btn_categories.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_categories.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_categories.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    background-color: rgb(255, 197, 125);\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}")
        self.btn_categories.setObjectName("btn_categories")
        self.verticalLayout_4.addWidget(self.btn_categories)
        self.btn_products = QtWidgets.QPushButton(self.frame_for_btn)
        self.btn_products.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_products.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    background-color: rgb(255, 197, 125);\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}")
        self.btn_products.setObjectName("btn_products")
        self.verticalLayout_4.addWidget(self.btn_products)
        self.btn_orders = QtWidgets.QPushButton(self.frame_for_btn)
        self.btn_orders.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_orders.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    background-color: rgb(255, 197, 125);\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}")
        self.btn_orders.setObjectName("btn_orders")
        self.verticalLayout_4.addWidget(self.btn_orders)
        self.btn_reports = QtWidgets.QPushButton(self.frame_for_btn)
        self.btn_reports.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_reports.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    background-color: rgb(255, 197, 125);\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}")
        self.btn_reports.setObjectName("btn_reports")
        self.verticalLayout_4.addWidget(self.btn_reports)
        self.btn_catalog = QtWidgets.QPushButton(self.frame_for_btn)
        self.btn_catalog.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_catalog.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    background-color: rgb(255, 197, 125);\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}")
        self.btn_catalog.setObjectName("btn_catalog")
        self.verticalLayout_4.addWidget(self.btn_catalog)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame_for_btn)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_object = QtWidgets.QFrame(self.Content)
        self.frame_object.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_object.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_object.setObjectName("frame_object")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_object)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Widget_pages = QtWidgets.QStackedWidget(self.frame_object)
        self.Widget_pages.setObjectName("Widget_pages")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_home)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listView_2 = QtWidgets.QListView(self.page_home)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_2.addWidget(self.listView_2, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.page_home)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 0, 1, 1, 1)
        self.btn_arrange = QtWidgets.QPushButton(self.page_home)
        self.btn_arrange.setMinimumSize(QtCore.QSize(150, 30))
        self.btn_arrange.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_arrange.setStyleSheet("QPushButton {\n"
"    font: 87 8pt \"Montserrat Black\";\n"
"    background-color: rgb(255, 197, 125);\n"
"    border: 0px solid;    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(195, 150, 95);\n"
"}")
        self.btn_arrange.setObjectName("btn_arrange")
        self.gridLayout_2.addWidget(self.btn_arrange, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.Widget_pages.addWidget(self.page_home)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listView_3 = QtWidgets.QListView(self.page_2)
        self.listView_3.setObjectName("listView_3")
        self.gridLayout_3.addWidget(self.listView_3, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.Widget_pages.addWidget(self.page_2)
        self.verticalLayout_8.addWidget(self.Widget_pages)
        self.horizontalLayout_2.addWidget(self.frame_object)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Информационная система для оформления заказа в зоомагазине"))
        self.btn_menu.setText(_translate("MainWindow", "меню"))
        self.label.setText(_translate("MainWindow", "Информационная система для оформления заказа в Зоомагазине"))
        self.btn_categories.setText(_translate("MainWindow", "Категории"))
        self.btn_products.setText(_translate("MainWindow", "Товары"))
        self.btn_orders.setText(_translate("MainWindow", "Заказы"))
        self.btn_reports.setText(_translate("MainWindow", "Отчеты"))
        self.btn_catalog.setText(_translate("MainWindow", "Каталог"))
        self.btn_arrange.setText(_translate("MainWindow", "оформить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
