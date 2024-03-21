# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from db_conn import dbConnection
from mess import messagebox




class Ui_FormMainWindow(object):
    def setupUi(self, FormMainWindow):
        FormMainWindow.setObjectName("FormMainWindow")
        FormMainWindow.resize(447, 315)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FormMainWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonCreate = QtWidgets.QPushButton(FormMainWindow)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.verticalLayout_2.addWidget(self.pushButtonCreate)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUlica = QtWidgets.QLabel(FormMainWindow)
        self.labelUlica.setObjectName("labelUlica")
        self.verticalLayout.addWidget(self.labelUlica)
        self.lineEditUlica = QtWidgets.QLineEdit(FormMainWindow)
        self.lineEditUlica.setObjectName("lineEditUlica")
        self.verticalLayout.addWidget(self.lineEditUlica)
        self.label = QtWidgets.QLabel(FormMainWindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditKod = QtWidgets.QLineEdit(FormMainWindow)
        self.lineEditKod.setObjectName("lineEditKod")
        self.verticalLayout.addWidget(self.lineEditKod)
        self.labeMiejscowosc = QtWidgets.QLabel(FormMainWindow)
        self.labeMiejscowosc.setObjectName("labeMiejscowosc")
        self.verticalLayout.addWidget(self.labeMiejscowosc)
        self.lineEditMiejscowosc = QtWidgets.QLineEdit(FormMainWindow)
        self.lineEditMiejscowosc.setObjectName("lineEditMiejscowosc")
        self.verticalLayout.addWidget(self.lineEditMiejscowosc)
        self.pushButtonInsertRecord = QtWidgets.QPushButton(FormMainWindow)
        self.pushButtonInsertRecord.setObjectName("pushButtonInsertRecord")
        self.verticalLayout.addWidget(self.pushButtonInsertRecord)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(FormMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FormMainWindow)
        self.pushButtonCreate.clicked.connect(self.createtable)
        self.pushButtonInsertRecord.clicked.connect(self.insertrecord)
        
        
    def insertrecord(self):
        ulica = self.lineEditUlica.text()
        kod = self.lineEditKod.text()
        miejscowosc = self.lineEditMiejscowosc.text()
        
        if ulica !='' and kod!='' and miejscowosc!='':
            params = (ulica, kod, miejscowosc)
            
            query = """
                    INSERT INTO adresy (ulica, kod, miejscowosc)
                    VALUES (%s, %s, %s);
                    """
            db = dbConnection()
            db.connect()
            curs = db.execute(query, params)
            db.close()
            if curs.statusmessage == 'INSERT 0 1':
                messagebox("New record", "New record has been added." , "Information", "Ok")
            else:
                messagebox("Error", "Record has not been added" , "Warning", "Cancel")
        else:
            messagebox("Error", "Insert correct data" , "Warning", "Cancel")
        

        
        
    def createtable(self):
        query = """
                CREATE TABLE IF NOT EXISTS adresy (
                  id_adres SERIAL PRIMARY KEY,
                  ulica VARCHAR(50) NOT NULL,
                  kod VARCHAR(6) NOT NULL,
                  miejscowosc VARCHAR(30) NOT NULL  
                );
                """
        db = dbConnection()
        db.connect()
        curs = db.execute(query)
        db.close()
        if curs.statusmessage ==  'CREATE TABLE':
            messagebox("New table", "New table has been added." , "Information", "Ok")
        else:
            messagebox("Error", "New table has NOT been added." , "Warning", "Cancel")
        

    def retranslateUi(self, FormMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FormMainWindow.setWindowTitle(_translate("FormMainWindow", "Main Window"))
        self.pushButtonCreate.setText(_translate("FormMainWindow", "Create table"))
        self.labelUlica.setText(_translate("FormMainWindow", "Ulica"))
        self.label.setText(_translate("FormMainWindow", "Kod pocztowy"))
        self.labeMiejscowosc.setText(_translate("FormMainWindow", "Miejscowość"))
        self.pushButtonInsertRecord.setText(_translate("FormMainWindow", "Insert record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMainWindow = QtWidgets.QWidget()
    ui = Ui_FormMainWindow()
    ui.setupUi(FormMainWindow)
    FormMainWindow.show()
    sys.exit(app.exec_())
