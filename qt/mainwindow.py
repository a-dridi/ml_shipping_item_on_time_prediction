# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.apptitle = QtWidgets.QLabel(self.centralwidget)
        self.apptitle.setGeometry(QtCore.QRect(0, 0, 841, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.apptitle.setFont(font)
        self.apptitle.setAutoFillBackground(False)
        self.apptitle.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"color: white;\n"
"")
        self.apptitle.setAlignment(QtCore.Qt.AlignCenter)
        self.apptitle.setObjectName("apptitle")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 250, 120, 80))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.containerHeader = QtWidgets.QFrame(self.centralwidget)
        self.containerHeader.setGeometry(QtCore.QRect(20, 80, 791, 51))
        self.containerHeader.setStyleSheet("background-color:white;\n"
"border: 2px inset rgb(121, 0, 181);\n"
"border-radius: 5px;")
        self.containerHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.containerHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containerHeader.setObjectName("containerHeader")
        self.predictionTitle = QtWidgets.QLabel(self.containerHeader)
        self.predictionTitle.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predictionTitle.setFont(font)
        self.predictionTitle.setStyleSheet("background-color:white;\n"
"border: 2px none rgb(121, 0, 181);\n"
"border-radius: 0px;")
        self.predictionTitle.setObjectName("predictionTitle")
        self.predictionValue = QtWidgets.QLabel(self.containerHeader)
        self.predictionValue.setGeometry(QtCore.QRect(200, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predictionValue.setFont(font)
        self.predictionValue.setStyleSheet("background-color:white;\n"
"border: 2px none rgb(121, 0, 181);\n"
"border-radius: 0px;")
        self.predictionValue.setObjectName("predictionValue")
        self.accuracyValue = QtWidgets.QLabel(self.containerHeader)
        self.accuracyValue.setGeometry(QtCore.QRect(640, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accuracyValue.setFont(font)
        self.accuracyValue.setStyleSheet("background-color:white;\n"
"border: 2px none rgb(121, 0, 181);\n"
"border-radius: 0px;")
        self.accuracyValue.setText("")
        self.accuracyValue.setObjectName("accuracyValue")
        self.accuracyTitle = QtWidgets.QLabel(self.containerHeader)
        self.accuracyTitle.setGeometry(QtCore.QRect(710, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accuracyTitle.setFont(font)
        self.accuracyTitle.setStyleSheet("background-color:white;\n"
"border: 2px none rgb(121, 0, 181);\n"
"border-radius: 0px;")
        self.accuracyTitle.setObjectName("accuracyTitle")
        self.shippingDurationTable = QtWidgets.QTableWidget(self.centralwidget)
        self.shippingDurationTable.setGeometry(QtCore.QRect(20, 140, 791, 391))
        self.shippingDurationTable.setRowCount(1)
        self.shippingDurationTable.setColumnCount(5)
        self.shippingDurationTable.setObjectName("shippingDurationTable")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 590, 791, 161))
        self.frame_2.setStyleSheet("background-color: rgb(240, 255, 250);\n"
"border: 2px  solid black;\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.shippeditemNameValue = QtWidgets.QLineEdit(self.frame_2)
        self.shippeditemNameValue.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.shippeditemNameValue.setStyleSheet("background-color: white;\n"
"border: 1px  solid grey;\n"
"border-radius: 0px;")
        self.shippeditemNameValue.setObjectName("shippeditemNameValue")
        self.shippeditemNameTextview = QtWidgets.QLabel(self.frame_2)
        self.shippeditemNameTextview.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shippeditemNameTextview.setFont(font)
        self.shippeditemNameTextview.setStyleSheet("background-color: rgb(240, 255, 250);\n"
"border: 2px  none black;\n"
"border-radius: 0px;")
        self.shippeditemNameTextview.setObjectName("shippeditemNameTextview")
        self.addShippingDurationButton = QtWidgets.QPushButton(self.frame_2)
        self.addShippingDurationButton.setGeometry(QtCore.QRect(10, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addShippingDurationButton.setFont(font)
        self.addShippingDurationButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.addShippingDurationButton.setObjectName("addShippingDurationButton")
        self.shippedItemQuantityTextview = QtWidgets.QLabel(self.frame_2)
        self.shippedItemQuantityTextview.setGeometry(QtCore.QRect(230, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shippedItemQuantityTextview.setFont(font)
        self.shippedItemQuantityTextview.setStyleSheet("background-color: rgb(240, 255, 250);\n"
"border: 2px  none black;\n"
"border-radius: 0px;")
        self.shippedItemQuantityTextview.setObjectName("shippedItemQuantityTextview")
        self.shippedItemQuantityValue = QtWidgets.QSpinBox(self.frame_2)
        self.shippedItemQuantityValue.setGeometry(QtCore.QRect(230, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shippedItemQuantityValue.setFont(font)
        self.shippedItemQuantityValue.setStyleSheet("background-color: white;\n"
"border: 1px  solid grey;\n"
"border-radius: 0px;")
        self.shippedItemQuantityValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shippedItemQuantityValue.setMinimum(1)
        self.shippedItemQuantityValue.setMaximum(1000000)
        self.shippedItemQuantityValue.setProperty("value", 1)
        self.shippedItemQuantityValue.setObjectName("shippedItemQuantityValue")
        self.shippedItemOnTimeTextview = QtWidgets.QLabel(self.frame_2)
        self.shippedItemOnTimeTextview.setGeometry(QtCore.QRect(390, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shippedItemOnTimeTextview.setFont(font)
        self.shippedItemOnTimeTextview.setStyleSheet("background-color: rgb(240, 255, 250);\n"
"border: 2px  none black;\n"
"border-radius: 0px;")
        self.shippedItemOnTimeTextview.setObjectName("shippedItemOnTimeTextview")
        self.shippedItemDurationTextview = QtWidgets.QLabel(self.frame_2)
        self.shippedItemDurationTextview.setGeometry(QtCore.QRect(540, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shippedItemDurationTextview.setFont(font)
        self.shippedItemDurationTextview.setStyleSheet("background-color: rgb(240, 255, 250);\n"
"border: 2px  none black;\n"
"border-radius: 0px;")
        self.shippedItemDurationTextview.setObjectName("shippedItemDurationTextview")
        self.shippedItemDurationValue = QtWidgets.QSpinBox(self.frame_2)
        self.shippedItemDurationValue.setGeometry(QtCore.QRect(540, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shippedItemDurationValue.setFont(font)
        self.shippedItemDurationValue.setStyleSheet("background-color: white;\n"
"border: 1px  solid grey;\n"
"border-radius: 0px;")
        self.shippedItemDurationValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shippedItemDurationValue.setMinimum(1)
        self.shippedItemDurationValue.setMaximum(365)
        self.shippedItemDurationValue.setProperty("value", 1)
        self.shippedItemDurationValue.setObjectName("shippedItemDurationValue")
        self.shippedItemOnTime = QtWidgets.QCheckBox(self.frame_2)
        self.shippedItemOnTime.setGeometry(QtCore.QRect(390, 40, 121, 31))
        self.shippedItemOnTime.setStyleSheet("background-color: white;\n"
"border: 1px  solid grey;\n"
"border-radius: 0px;\n"
"padding: 4px;")
        self.shippedItemOnTime.setObjectName("shippedItemOnTime")
        self.tableInfo = QtWidgets.QFrame(self.centralwidget)
        self.tableInfo.setGeometry(QtCore.QRect(20, 540, 791, 41))
        self.tableInfo.setStyleSheet("background-color:white;\n"
"border: 2px inset rgb(121, 0, 181);\n"
"border-radius: 5px;")
        self.tableInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableInfo.setObjectName("tableInfo")
        self.tableInfoTextView = QtWidgets.QLabel(self.tableInfo)
        self.tableInfoTextView.setGeometry(QtCore.QRect(20, 10, 751, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableInfoTextView.sizePolicy().hasHeightForWidth())
        self.tableInfoTextView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableInfoTextView.setFont(font)
        self.tableInfoTextView.setStyleSheet("background-color:white;\n"
"border: 2px none rgb(121, 0, 181);\n"
"border-radius: 0px;")
        self.tableInfoTextView.setObjectName("tableInfoTextView")
        self.infoButtonMainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.infoButtonMainWindow.setGeometry(QtCore.QRect(670, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infoButtonMainWindow.setFont(font)
        self.infoButtonMainWindow.setObjectName("infoButtonMainWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apptitle.setText(_translate("MainWindow", "Prediction of Shipping Duration"))
        self.predictionTitle.setText(_translate("MainWindow", "Prediction of \"On Time\": "))
        self.predictionValue.setText(_translate("MainWindow", " "))
        self.accuracyTitle.setText(_translate("MainWindow", "Accuracy"))
        self.shippeditemNameTextview.setText(_translate("MainWindow", "Item Name:"))
        self.addShippingDurationButton.setText(_translate("MainWindow", "Add"))
        self.shippedItemQuantityTextview.setText(_translate("MainWindow", "Quantity:"))
        self.shippedItemOnTimeTextview.setText(_translate("MainWindow", "On Time:"))
        self.shippedItemDurationTextview.setText(_translate("MainWindow", "Duration:"))
        self.shippedItemOnTime.setText(_translate("MainWindow", "Delivered On Time"))
        self.tableInfoTextView.setText(_translate("MainWindow", "On Time: 0 = no | 1 = Yes"))
        self.infoButtonMainWindow.setText(_translate("MainWindow", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

