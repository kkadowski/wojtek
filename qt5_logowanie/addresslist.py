# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addresslist.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from db_conn import dbConnection
from mess import messagebox

class Ui_FormAddressList(object):
    def setupUi(self, FormAddressList):
        FormAddressList.setObjectName("FormAddressList")
        FormAddressList.resize(377, 342)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormAddressList)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(FormAddressList)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
     
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButtonClose = QtWidgets.QPushButton(FormAddressList)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.verticalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(FormAddressList)
        QtCore.QMetaObject.connectSlotsByName(FormAddressList)
        self.pushButtonClose.clicked.connect(self.closewindow)
        
        query = """
                SELECT id_adres, ulica, kod, miejscowosc FROM adresy;
                """
            
        db = dbConnection()
        db.connect()
        rows = db.fetchall(query)
        db.close()
        
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.repaint()     

        
        
    def closewindow(self):
        FormAddressList.close()

    def retranslateUi(self, FormAddressList):
        _translate = QtCore.QCoreApplication.translate
        FormAddressList.setWindowTitle(_translate("FormAddressList", "Address list"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FormAddressList", "ID adres"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FormAddressList", "Ulica"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FormAddressList", "Kod pocztowy"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FormAddressList", "Miejscowość"))
        self.pushButtonClose.setText(_translate("FormAddressList", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormAddressList = QtWidgets.QWidget()
    ui = Ui_FormAddressList()
    ui.setupUi(FormAddressList)
    FormAddressList.show()
    sys.exit(app.exec_())