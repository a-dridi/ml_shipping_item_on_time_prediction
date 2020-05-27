#Shipping Duration Prediction - Machine Learning: Python Example Application

This is a Python desktop application coded with Qt framework which uses the packge Scikit-Learn. This is an machine learning example application in Python.
This application allows you to save information about shipped product items which are used to predict, if the next shipping will be delivered on time. 

![Screenshot of Application](https://raw.githubusercontent.com/a-dridi/ml_shipping_item_on_time_prediction/master/img/screenshot.PNG)

##Features
You can save the product item name, quantitiy, duration and if it did get on time. 
Creates prediction if the next shipping will be delivered on time. The accuracy improves through amount of available information about the shipped product items. 
Displays the accuracy of the prediction
Data is saved in a sqlite database file
Optional: Function to create large test data can also be used

## Run
You can run the app by executing the Python file "app.py".
This repository can also be opened in the IDE "PyCharm".


## Installation (Deployment)
You need Python 3.6+
You can find an example database file for this application in the folder "test_database".

## Configuration
If you want to test this application with large data, then uncomment the function "ui.load_test_data_into_database()" in the bottom of the file "app.py". This function allows you to test the app in an productive environment. The database loading could take some time with this function. 

## Authors

* **A. Dridi** - [a-dridi](https://github.com/a-dridi/)

