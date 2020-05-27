# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infoWindowDialog(object):
    def setupUi(self, infoWindowDialog):
        infoWindowDialog.setObjectName("infoWindowDialog")
        infoWindowDialog.resize(803, 389)
        self.okButtonInfoWindow = QtWidgets.QPushButton(infoWindowDialog)
        self.okButtonInfoWindow.setGeometry(QtCore.QRect(340, 330, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okButtonInfoWindow.setFont(font)
        self.okButtonInfoWindow.setObjectName("okButtonInfoWindow")
        self.infoWindowMainText = QtWidgets.QLabel(infoWindowDialog)
        self.infoWindowMainText.setGeometry(QtCore.QRect(30, 130, 731, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infoWindowMainText.setFont(font)
        self.infoWindowMainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.infoWindowMainText.setObjectName("infoWindowMainText")
        self.line = QtWidgets.QFrame(infoWindowDialog)
        self.line.setGeometry(QtCore.QRect(30, 110, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.infoWindowTitle = QtWidgets.QLabel(infoWindowDialog)
        self.infoWindowTitle.setGeometry(QtCore.QRect(250, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.infoWindowTitle.setFont(font)
        self.infoWindowTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.infoWindowTitle.setObjectName("infoWindowTitle")
        self.infoWindowHeaderText = QtWidgets.QLabel(infoWindowDialog)
        self.infoWindowHeaderText.setGeometry(QtCore.QRect(30, 80, 721, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infoWindowHeaderText.setFont(font)
        self.infoWindowHeaderText.setObjectName("infoWindowHeaderText")

        self.retranslateUi(infoWindowDialog)
        QtCore.QMetaObject.connectSlotsByName(infoWindowDialog)

    def retranslateUi(self, infoWindowDialog):
        _translate = QtCore.QCoreApplication.translate
        infoWindowDialog.setWindowTitle(_translate("infoWindowDialog", "Dialog"))
        self.okButtonInfoWindow.setText(_translate("infoWindowDialog", "OK"))
        self.infoWindowMainText.setText(_translate("infoWindowDialog", "<html><head/><body><p>This app allows you to save information about shipped items. </p><p>This app then creates a prediction, if the latest shipped item gets on time.<br>You also get an accuracy of the prediction. <br> More shipped items data equal to more accuracy in the prediction.<br>You can also use the function <span style=\" font-family:\'Courier New\'; color:#000000; background-color:#e4e4ff;\">load_test_data_into_database()</span> in the python file &quot;app.py&quot; <br>to add large test data for productive testing purposes. </p></body></html>"))
        self.infoWindowTitle.setText(_translate("infoWindowDialog", "Info"))
        self.infoWindowHeaderText.setText(_translate("infoWindowDialog", "Developed by: A.Dridi  - https://github.com/a-dridi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    infoWindowDialog = QtWidgets.QDialog()
    ui = Ui_infoWindowDialog()
    ui.setupUi(infoWindowDialog)
    infoWindowDialog.show()
    sys.exit(app.exec_())

