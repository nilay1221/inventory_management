# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_shade_delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.shade_new_delete_details_table = QtWidgets.QTableWidget(self.centralwidget)
        self.shade_new_delete_details_table.setGeometry(QtCore.QRect(180, 130, 421, 381))
        self.shade_new_delete_details_table.setRowCount(10)
        self.shade_new_delete_details_table.setObjectName("shade_new_delete_details_table")
        self.shade_new_delete_details_table.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_new_delete_details_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_new_delete_details_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_new_delete_details_table.setHorizontalHeaderItem(2, item)
        self.rm_new_delete_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.rm_new_delete_confirm.setGeometry(QtCore.QRect(340, 520, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_new_delete_confirm.setFont(font)
        self.rm_new_delete_confirm.setObjectName("rm_new_delete_confirm")
        self.back_add_rm = QtWidgets.QPushButton(self.centralwidget)
        self.back_add_rm.setGeometry(QtCore.QRect(20, 30, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_add_rm.setFont(font)
        self.back_add_rm.setObjectName("back_add_rm")
        self.shade_new__delete_number = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_new__delete_number.setGeometry(QtCore.QRect(430, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_new__delete_number.setFont(font)
        self.shade_new__delete_number.setObjectName("shade_new__delete_number")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 70, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back to Main Menu"))
        item = self.shade_new_delete_details_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Code"))
        item = self.shade_new_delete_details_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.shade_new_delete_details_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Percentage"))
        self.rm_new_delete_confirm.setText(_translate("MainWindow", "Delete"))
        self.back_add_rm.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Shade Number"))
        self.label_5.setText(_translate("MainWindow", "Enter Shade Number :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())