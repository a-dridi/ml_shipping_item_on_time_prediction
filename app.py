from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import sqlite3
import hashlib
import random


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
        self.predictionTitle.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predictionTitle.setFont(font)
        self.predictionTitle.setStyleSheet("background-color:white;\n"
                                           "border: 2px none rgb(121, 0, 181);\n"
                                           "border-radius: 0px;")
        self.predictionTitle.setObjectName("predictionTitle")

        self.predictionValue = QtWidgets.QLabel(self.containerHeader)
        self.predictionValue.setGeometry(QtCore.QRect(240, 10, 51, 31))
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

        # *** Add shipped item form ***

        self.shippeditemNameValue = QtWidgets.QLineEdit(self.frame_2)
        self.shippeditemNameValue.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.shippeditemNameValue.setStyleSheet("background-color: white;\n"
                                                "border: 1px  solid grey;\n"
                                                "border-radius: 0px;")
        self.shippeditemNameValue.setObjectName("shippeditemNameValue")

        self.shippeditemNameTextview = QtWidgets.QLabel(self.frame_2)
        self.shippeditemNameTextview.setGeometry(QtCore.QRect(10, 9, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
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
        self.shippedItemQuantityValue.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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
        self.shippedItemDurationTextview.setGeometry(QtCore.QRect(540, 10, 139, 31))
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
        self.shippedItemDurationValue.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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

        self.predictOntimeButton = QtWidgets.QPushButton(self.frame_2)
        self.predictOntimeButton.setGeometry(QtCore.QRect(180, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predictOntimeButton.setFont(font)
        self.predictOntimeButton.setStyleSheet("background-color: rgb(255, 226, 61);\n"
                                               "color: black")
        self.predictOntimeButton.setObjectName("predictOntimeButton")

        self.createPredictionDisplay = QtWidgets.QLabel(self.frame_2)
        self.createPredictionDisplay.setGeometry(QtCore.QRect(320, 100, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createPredictionDisplay.setFont(font)
        self.createPredictionDisplay.setStyleSheet("background-color:white;\n"
                                                   "border: 2px none rgb(121, 0, 181);\n"
                                                   "border-radius: 0px;\n"
                                                   "padding-left: 5px;")
        self.createPredictionDisplay.setObjectName("createPredictionDisplay")

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
        self.infoButtonMainWindow.clicked.connect(self.open_info_window)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        Ui_MainWindow.load_data_from_database(self)

        # Functions
        self.addShippingDurationButton.clicked.connect(self.save_shippeditem)
        self.predictOntimeButton.clicked.connect(self.create_prediction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shipping Duration"))
        self.apptitle.setText(_translate("MainWindow", "Prediction of Shipping Duration"))
        self.predictionTitle.setText(_translate("MainWindow", "Prediction of latest \"On Time\": "))
        self.predictionValue.setText(_translate("MainWindow", " "))
        self.accuracyTitle.setText(_translate("MainWindow", "Accuracy"))
        self.shippeditemNameTextview.setText(_translate("MainWindow", "Item Name:"))
        self.addShippingDurationButton.setText(_translate("MainWindow", "Add"))
        self.shippedItemQuantityTextview.setText(_translate("MainWindow", "Quantity:"))
        self.shippedItemOnTimeTextview.setText(_translate("MainWindow", "On Time:"))
        self.shippedItemDurationTextview.setText(_translate("MainWindow", "Duration (in Days):"))
        self.shippedItemOnTime.setText(_translate("MainWindow", "Delivered On Time"))
        self.tableInfoTextView.setText(_translate("MainWindow", "On Time: 0 = no | 1 = Yes"))
        self.infoButtonMainWindow.setText(_translate("MainWindow", "Info"))
        self.shippingDurationTable.setHorizontalHeaderLabels(
            ['ID', 'Item name', 'Quantity', 'Duration (days)', 'On Time'])
        self.predictOntimeButton.setText(_translate("MainWindow", "Predict"))

    def load_Database(self):
        # Try to load data from database for checking purposes. If database was not created, then create database.
        try:
            self.sqliteConn = sqlite3.connect('shipped_items_prediction.db')
            cursor = self.sqliteConn.cursor()
            query_select_dishes = "select * from shippeditems"
            cursor.execute(query_select_dishes)

        except sqlite3.Error as error:
            print("Error sqlite db: ", error)
            sqliteConn = self.sqliteConn
            # Create new database and tables - duration in days -
            # ontime: if shipping is on time (yes: 1, no: 0)
            query_create_table = ''' CREATE TABLE shippeditems (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                quantity INTEGER,
                                durationdays INTEGER,
                                ontime INTEGER
                                );
                                ''';

            cursor = sqliteConn.cursor();
            cursor.execute(query_create_table)
            sqliteConn.commit()
            print("New Database created")
            cursor.close()

        finally:
            if (self.sqliteConn):
                self.sqliteConn.close()

    def load_data_from_database(self):
        self.sqliteConn = sqlite3.connect('shipped_items_prediction.db')
        cursor = self.sqliteConn.cursor()

        query_select_dishes = "select * from shippeditems"
        cursor.execute(query_select_dishes)
        self.shippeditemsRecords = cursor.fetchall()

        cursor.close()
        self.sqliteConn.close()

        # Load table with shipped items data
        rowIndex = 0
        self.shippingDurationTable.setRowCount(0)
        # Features - Data that is needed to create prediction (item name, quantity, duration)
        self.X_coordinate = []
        # Labels - Prediction data (on time values of all shipped items)
        self.y_coordinate = []
        self.shippingDurationTable.editTriggers()
        self.quantitityShippingItemsArray = []
        self.durationShippingItemsArray = []

        if (self.shippeditemsRecords):
            rowIndex = 1
            for shippingItemEntry in self.shippeditemsRecords:
                self.shippingDurationTable.insertRow(rowIndex - 1)
                self.shippingDurationTable.setItem(rowIndex - 1, 0,
                                                   QtWidgets.QTableWidgetItem(str(shippingItemEntry[0])))
                self.shippingDurationTable.setItem(rowIndex - 1, 1,
                                                   QtWidgets.QTableWidgetItem(str(shippingItemEntry[1])))
                self.shippingDurationTable.setItem(rowIndex - 1, 2,
                                                   QtWidgets.QTableWidgetItem(str(shippingItemEntry[2])))
                self.shippingDurationTable.setItem(rowIndex - 1, 3,
                                                   QtWidgets.QTableWidgetItem(str(shippingItemEntry[3])))
                self.shippingDurationTable.setItem(rowIndex - 1, 4,
                                                   QtWidgets.QTableWidgetItem(str(shippingItemEntry[4])))

                self.X_coordinate.append([])
                #itemnameHash = int(hashlib.sha256("Hallo".encode("utf-8")).hexdigest(), 16) % 10 ** 10
                #self.X_coordinate[rowIndex - 1].append(itemnameHash)
                self.X_coordinate[rowIndex - 1].append(shippingItemEntry[2])
                self.X_coordinate[rowIndex - 1].append(shippingItemEntry[3])
                self.y_coordinate.append(shippingItemEntry[4])

                self.quantitityShippingItemsArray.append(shippingItemEntry[2])
                self.durationShippingItemsArray.append(shippingItemEntry[3])
                rowIndex += 1

        self.shippingDurationTable.setRowCount(rowIndex - 1)
        # No Edit available for now - Future feature
        self.shippingDurationTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.shippingDurationTable.show()
        self.quantitityShippingItemsAverage = sum(self.quantitityShippingItemsArray) / len(
            self.quantitityShippingItemsArray)
        self.durationShippingItemsAverage = sum(self.durationShippingItemsArray) / len(self.durationShippingItemsArray)
        # Add additional shipping item for prediction of future shipping item "on item" value - X_Coordinate uses average value
        self.X_coordinate.append([])
        #self.X_coordinate[rowIndex - 1].append(0)
        self.X_coordinate[rowIndex - 1].append(self.quantitityShippingItemsAverage)
        self.X_coordinate[rowIndex - 1].append(self.durationShippingItemsAverage)
        self.y_coordinate.append(round((sum(self.y_coordinate)/len(self.y_coordinate)),0))
        # DEBUG
        # print(self.X_coordinate)
        # print(self.y_coordinate)

    def load_prediction(self):
        if (len(self.shippeditemsRecords) > 0):
            # Most middle index of the database list
            center_index = int(len(self.shippeditemsRecords) / 2)
            # Features
            # The first half of available data is used for training - The second is used to test the prediction (accuracy)
            self.X_coordinate_train = self.X_coordinate[:-center_index]
            self.X_coordinate_real = self.X_coordinate[-center_index:]
            # Scaling to optimize data against biases
            #standardScalerObj = StandardScaler()
            #self.X_coordinate_train = standardScalerObj.fit_transform(self.X_coordinate_train)
            #self.X_coordinate_real = standardScalerObj.transform(self.X_coordinate_real)

            # Labels - The data that should be predicted
            self.y_coordinate_train = self.y_coordinate[:-center_index]
            self.y_coordinate_real = self.y_coordinate[-center_index:]
            # Train through created shipping item data - Create prection
            shippingitem_classification = RandomForestClassifier(n_estimators=300)
            shippingitem_classification.fit(self.X_coordinate_train, self.y_coordinate_train)
            prediction_ontime_shippingitem = shippingitem_classification.predict(self.X_coordinate_real)

            # OLD prediction method
            #shippingitem_classification = tree.DecisionTreeClassifier()
            #shippingitem_classification.fit(self.X_coordinate_train, self.y_coordinate_train)
            #prediction_ontime_shippingitem = shippingitem_classification.predict(self.X_coordinate_real)

            if (prediction_ontime_shippingitem[len(prediction_ontime_shippingitem) - 1]):
                self.predictionValue.setText("Yes")
            else:
                self.predictionValue.setText("no")
            self.accuracyValue.setText(
                "%.2f%%" % (accuracy_score(prediction_ontime_shippingitem, self.y_coordinate_real) * 100))

            # DEBUG
            # print("real **")
            # print(self.y_coordinate_real)
            # print("prediction **")
            # print(prediction_ontime_shippingitem)
            # print("score **")
            # print("%.2f" %(accuracy_score(prediction_ontime_shippingitem, self.y_coordinate_real) * 100))

    def save_shippeditem(self):
        shippeditemName = self.shippeditemNameValue.text().title()
        shippeditemQuantity = int(self.shippedItemQuantityValue.text().title())
        shippeditemDuration = int(self.shippedItemDurationValue.text().title())
        if (self.shippedItemOnTime.isChecked()):
            shippeditemOnTime = 1
        else:
            shippeditemOnTime = 0

        # Insert new dish
        sqliteConn = sqlite3.connect('shipped_items_prediction.db')
        cursor = sqliteConn.cursor()
        query_select_shippeditems = "select * from shippeditems"
        cursor.execute(query_select_shippeditems)
        shippeditemRecords = cursor.fetchall()

        if (len(shippeditemRecords) > 0):
            query_insert_shippeditem = "INSERT INTO shippeditems ('id', 'name', 'quantity', 'durationdays', 'ontime') VALUES (?,?,?,?,?)"
            print((len(shippeditemRecords) + 1))
            cursor.execute(query_insert_shippeditem,
                           [(len(shippeditemRecords) + 1), shippeditemName, shippeditemQuantity, shippeditemDuration,
                            shippeditemOnTime])
        else:
            print("App database started for the First Time")
            query_insert_shippeditem = "INSERT INTO shippeditems ('id', 'name', 'quantity', 'durationdays', 'ontime') VALUES (1,'"
            query_insert_shippeditem += shippeditemName
            query_insert_shippeditem += "','"
            query_insert_shippeditem += shippeditemQuantity
            query_insert_shippeditem += "','"
            query_insert_shippeditem += shippeditemDuration
            query_insert_shippeditem += "','"
            query_insert_shippeditem += str(shippeditemOnTime)
            query_insert_shippeditem += "')"
            cursor.execute(query_insert_shippeditem)

        sqliteConn.commit()
        print("New shipped item was added")
        cursor.close()
        sqliteConn.close()

        Ui_MainWindow.load_data_from_database(self)

    def open_info_window(self):
        infoWindowDialog = QtWidgets.QDialog()
        infowWindowUi = Ui_infoWindowDialog()
        infowWindowUi.setupUi(infoWindowDialog)
        infoWindowDialog.show()

    # OPTIONAL - For productive test: Load only test data into database - DELETES ALL EXISTING DATA!!!
    def load_test_data_into_database(self):
        sqliteConn = sqlite3.connect('shipped_items_prediction.db')
        cursor = sqliteConn.cursor()
        query_delete_all_shippeditems = "delete from shippeditems"
        query_select_shippeditems = "select * from shippeditems"
        cursor.execute(query_delete_all_shippeditems)
        cursor.execute(query_select_shippeditems)
        shippeditemRecords = cursor.fetchall()

        shippingitemCurrentId = len(shippeditemRecords)
        if (shippingitemCurrentId == 0):
            shippingitemCurrentId = 1
        for i in range(100000):
            query_insert_shippeditem = "INSERT INTO shippeditems ('id', 'name', 'quantity', 'durationdays', 'ontime') VALUES ("
            query_insert_shippeditem += str(shippingitemCurrentId)
            query_insert_shippeditem += ",'Product " + str(random.randint(1, 50))
            query_insert_shippeditem += "','"
            query_insert_shippeditem += str(random.randint(1, 100))
            query_insert_shippeditem += "','"
            query_insert_shippeditem += str(random.randint(1, 30))
            query_insert_shippeditem += "','"
            query_insert_shippeditem += str(random.randint(0, 1))
            query_insert_shippeditem += "')"
            cursor.execute(query_insert_shippeditem)
            shippingitemCurrentId += 1
        sqliteConn.commit()
        print("TEST DATA shipped item was added")
        cursor.close()
        sqliteConn.close()

    #Create prediction with new shipped item. Display the prediction value (on time) for the new shipped item.
    def create_prediction(self):
        shippeditemQuantity = int(self.shippedItemQuantityValue.text().title())
        shippeditemDuration = int(self.shippedItemDurationValue.text().title())
        self.X_coordinate.pop()
        self.X_coordinate.append([shippeditemQuantity, shippeditemDuration])

        train_index = int(len(self.shippeditemsRecords) * 0.70)
        rest_index = len(self.shippeditemsRecords) - train_index

        # The last 70 percent of available data is used for training - The first 30 is used to test the prediction (accuracy)
        self.X_coordinate_train = self.X_coordinate[:train_index]
        self.X_coordinate_real = self.X_coordinate[train_index:]

        # The data that should be predicted
        self.y_coordinate_train = self.y_coordinate[:train_index]
        self.y_coordinate_real = self.y_coordinate[train_index:]
        # Train through created shipping item data - Create prection
        shippingitem_classification = RandomForestClassifier(n_estimators=300)
        shippingitem_classification.fit(self.X_coordinate_train, self.y_coordinate_train)
        prediction_ontime_shippingitem = shippingitem_classification.predict(self.X_coordinate_real)

        #New prediction value is in the last array item
        newPredictionValue = ""
        if (prediction_ontime_shippingitem[-1]):
            newPredictionValue="Yes"
        else:
            newPredictionValue="no"
        newPredictionAccuracy = accuracy_score(prediction_ontime_shippingitem, self.y_coordinate_real) * 100
        self.createPredictionDisplay.setText("-> On Time: " + newPredictionValue + " - " + "{:.2f}".format(newPredictionAccuracy) + "% Accuracy")

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
        self.okButtonInfoWindow.clicked.connect(infoWindowDialog.done)
        self.infoWindowMainText = QtWidgets.QLabel(infoWindowDialog)
        self.infoWindowMainText.setGeometry(QtCore.QRect(30, 130, 731, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infoWindowMainText.setFont(font)
        self.infoWindowMainText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
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
        infoWindowDialog.setWindowTitle(_translate("infoWindowDialog", "Info about this application"))
        self.okButtonInfoWindow.setText(_translate("infoWindowDialog", "OK"))
        self.infoWindowMainText.setText(_translate("infoWindowDialog",
                                                   "<html><head/><body><p>This app allows you to save information about shipped items. </p><p>This app then creates a prediction, if the next (future) shipped item gets on time.<br>You also get an accuracy of the prediction. <br> You can show the prediction for a new shipping item, when you click on the button predicate. <br> More shipped items data equal to more accuracy in the prediction. <br>You can also use the function <span style=\" font-family:\'Courier New\'; color:#000000; background-color:#e4e4ff;\">load_test_data_into_database()</span> in the python file &quot;app.py&quot; <br>to add large test data for productive testing purposes. </p></body></html>"))
        self.infoWindowTitle.setText(_translate("infoWindowDialog", "Info"))
        self.infoWindowHeaderText.setText(
            _translate("infoWindowDialog", "Developed by: A.Dridi  - https://github.com/a-dridi"))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.load_Database()
    # TEST: Uncomment the following only for one run time
    ui.load_test_data_into_database()
    ui.setupUi(MainWindow)
    ui.load_prediction()
    MainWindow.show()
    sys.exit(app.exec_())
