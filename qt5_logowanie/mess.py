from PyQt5 import QtCore, QtGui, QtWidgets


def messagebox(title, message, icon, StandardButtons):
    mess = QtWidgets.QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    if icon == "Information":
        mess.setIcon(QtWidgets.QMessageBox.Information)
    elif icon == "Critical":
        mess.setIcon(QtWidgets.QMessageBox.Critical)
    elif icon == "Question":
        mess.setIcon(QtWidgets.QMessageBox.Question)
    elif icon == "Warning":
        mess.setIcon(QtWidgets.QMessageBox.Warning)
    else:
        mess.setIcon(QtWidgets.QMessageBox.NoIcon)
    
    if StandardButtons == "Ok":
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif StandardButtons == "Cancel":
        mess.setStandardButtons(QtWidgets.QMessageBox.Cancel)
    mess.exec_()   