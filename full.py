# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QPushButton, QAction, QInputDialog, QLineEdit
from scipy.interpolate import interp1d
import numpy as np
import pandas as pd
import os
import re
import csv
import math
from functools import reduce
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import scipy.integrate
import inspect

savedName = 'Default'



"""First Window. Here the option to choose 'User' or 'Analyst' is given"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userBtn = QtWidgets.QPushButton(self.centralwidget)
        self.userBtn.setObjectName("userBtn")
        self.horizontalLayout.addWidget(self.userBtn)
        self.analystBtn = QtWidgets.QPushButton(self.centralwidget)
        self.analystBtn.setObjectName("analystBtn")
        self.horizontalLayout.addWidget(self.analystBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userBtn.setText(_translate("MainWindow", "User"))
        self.analystBtn.setText(_translate("MainWindow", "Analyst"))
        self.analystBtn.clicked.connect(self.analyst)
        self.userBtn.clicked.connect(self.user)
     
    
    def user(self):

        self.midWindowUi = Ui_midWindow()
        self.midWindowUi.setupUi(midWindow)
        midWindow.show()    
        MainWindow.close()
        

    def analyst(self):
        self.SecondWindowUi = Ui_SecondWindow()
        self.SecondWindowUi.setupUi(SecondWindow)
        SecondWindow.show()
        MainWindow.hide()
    
    def close_window3(self):
        self.window3.hide()



"""This is the second window. Here, the analyst get the option to browse and select which library to use.
Number of interpolation points and decay steps are mentioned. Folder name is mentioned. Radio button to set library
as default for user is also set here.

TO ADD:
    If folder name is left empty, then either name file as the time stamp, or display error message
    Make file location appear in the blank line when location chosen using 'Browse'"""


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(34, 130, 641, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filePath = QtWidgets.QLineEdit(self.layoutWidget)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout.addWidget(self.filePath)
        self.browseBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout.addWidget(self.browseBtn)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.interpVal = QtWidgets.QLineEdit(self.layoutWidget)
        self.interpVal.setObjectName("interpVal")
        self.horizontalLayout_2.addWidget(self.interpVal)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.timeVal = QtWidgets.QLineEdit(self.layoutWidget)
        self.timeVal.setObjectName("timeVal")
        self.horizontalLayout_3.addWidget(self.timeVal)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.saveName = QtWidgets.QLineEdit(self.layoutWidget)
        self.saveName.setObjectName("saveName")
        self.horizontalLayout_5.addWidget(self.saveName)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_4.addWidget(self.backBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_4.addWidget(self.cancelBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)
        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.browseBtn.setText(_translate("SecondWindow", "Browse"))
        self.radioButton.setText(_translate("SecondWindow", "Set as default for user"))
        self.label.setText(_translate("SecondWindow", "Number of interpolation points"))
        self.label_2.setText(_translate("SecondWindow", "Number of decay steps"))
        self.nextBtn.setText(_translate("SecondWindow", "Next"))
        self.label_3.setText(_translate("SecondWindow", "Folder Name"))
        self.backBtn.setText(_translate("SecondWindow", "Back"))
        self.cancelBtn.setText(_translate("SecondWindow", "Cancel"))
        self.browseBtn.clicked.connect(self.browse)
        self.nextBtn.clicked.connect(self.next)
        self.backBtn.clicked.connect(self.back)
        self.cancelBtn.clicked.connect(self.cancel)
        

    def back(self):
        SecondWindow.hide()
        MainWindow.show()
        print('hey')

    def cancel(self):
        sys.exit(0)
        

    filePath = ''
    def browse(self):           
        w = QWidget()
        w.resize(320, 240)
        temp = QFileDialog.getOpenFileName(w, 'Open File')
        self.filePath.setText(temp[0])
        global filePath
        filePath = temp[0]
        print(temp[0])
        
        
    def next(self):
        n_interp = int(self.interpVal.text())
        n_timesteps = int(self.timeVal.text())
        self.generate(n_interp, n_timesteps)
        print('hi')


    def exp_val(self, arg):
        return {
            '137Cs / 133Cs' : (0.693147/10982.77),
            '154Eu / 153Eu' : (0.693147/3138.5),
            '134Cs / 137Cs' : (0.693147/754.15)-(0.693147/10982.77),
            '135Cs / 137Cs' : -(0.693147/10982.77),
            '136Ba / 138Ba' : -1,
            '150Sm / 149Sm' : -1,
            '152Sm / 149Sm' : -1,
            '242Pu / 239Pu' : (0.693147/136344092)-(0.693147/8805936.4),
            '241Pu / 239Pu' : (0.693147/5241.194)-(0.693147/8805936.4),
            '240Pu / 239Pu' : (0.693147/2397435.36)-(0.693147/8805936.4)
            }[arg]
    
    def generate(self, inter, t):
        xl = pd.ExcelFile(filePath)
        list_sheets = xl.sheet_names
        print(inter)
        print(t)
        print(list_sheets)
        current_dir = os.getcwd()
        
        for sheet in list_sheets:
            df = pd.read_excel(xl, sheet)
            temp = []
            l = len(df['Burnup (GWd/MTU)'])
            for i in range(l):
                if isinstance(df.iloc[i]['Burnup (GWd/MTU)'], str) or pd.isna(df.iloc[i]['Burnup (GWd/MTU)']):
                    temp.append(i)
            df = df.drop(df.index[temp])
            r = np.linspace(min(df['Burnup (GWd/MTU)']), max(df['Burnup (GWd/MTU)']), inter)
            #print(inter)
            print('interpolation len ', len(r))
            time_range = np.linspace(1, t + 1, t)
            print('time len ', len(time_range))
            
            col_names = list(df)
            for p in range(1, len(col_names)):
                
                
                df1 = pd.DataFrame(columns = time_range, index = None)
                f = interp1d(df['Burnup (GWd/MTU)'], df[col_names[p]])
                k1 = f(r)
                counter = 0
                e_val = self.exp_val(col_names[p])
                for xx in k1:
                    op = []
                    if e_val == -1:
                        for yy in time_range:
                            op.append(xx)
                    else:
                        for yy in time_range:
                            
                            op.append(xx * np.exp(-e_val * (yy - 1)))
                    df1.loc[counter] = op
                    counter = counter + 1
                name = re.sub('/', '', col_names[p])

                if self.radioButton.isChecked():
                    if not os.path.exists(current_dir + '/' + 'Default'):
                        os.mkdir(current_dir + '/Default')
                    dir = current_dir + '/Default'
                    df1.to_csv(dir + '/' + sheet + name + '.csv')
                else:
                	global savedName
                	savedName = self.saveName.text()
                	if not os.path.exists(current_dir + '/' + self.saveName.text()):
                		os.mkdir(current_dir + '/' + self.saveName.text())
                	dir = current_dir + '/' + self.saveName.text()
                	df1.to_csv(dir + '/' + sheet + name + '.csv')

        temp_list_sheets = list_sheets
        temp_time_range = time_range
        temp_r = r

        with open(dir + '/sheet_names.csv', 'w') as file:
            wr = csv.writer(file)
            wr.writerow(list_sheets)
            wr.writerow(time_range)
            wr.writerow(r)
        SecondWindow.hide()
        #self.midWindow = QtWidgets.QMainWindow()
        self.midWindowUi = Ui_midWindow()
        self.midWindowUi.setupUi(midWindow)
        midWindow.show()
        #Ui_MainWindow.close_second(ui)


    def close_third(self):
        self.hide()
              




class Ui_midWindow(object):
    def setupUi(self, midWindow):
        midWindow.setObjectName("midWindow")
        midWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(midWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(202, 200, 411, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.singleVal = QtWidgets.QPushButton(self.layoutWidget)
        self.singleVal.setObjectName("singleVal")
        self.gridLayout.addWidget(self.singleVal, 0, 0, 1, 1)
        self.ratioVal = QtWidgets.QPushButton(self.layoutWidget)
        self.ratioVal.setObjectName("ratioVal")
        self.gridLayout.addWidget(self.ratioVal, 0, 1, 1, 1)
        midWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(midWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        midWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(midWindow)
        self.statusbar.setObjectName("statusbar")
        midWindow.setStatusBar(self.statusbar)

        self.retranslateUi(midWindow)
        QtCore.QMetaObject.connectSlotsByName(midWindow)

    def retranslateUi(self, midWindow):
        _translate = QtCore.QCoreApplication.translate
        midWindow.setWindowTitle(_translate("midWindow", "MainWindow"))
        self.singleVal.setText(_translate("midWindow", "Enter individual values"))
        self.ratioVal.setText(_translate("midWindow", "Enter ratios"))
        self.singleVal.clicked.connect(self.singleValfunc)
        self.ratioVal.clicked.connect(self.ratioValfunc)
        
        
    def singleValfunc(self):
        self.ThirdWindowUi = Ui_ThirdWindow()
        self.ThirdWindowUi.setupUi(ThirdWindow)
        ThirdWindow.show()   
        midWindow.hide()

        
        
        
    def ratioValfunc(self):
        self.ThirdWindow2 = QtWidgets.QMainWindow()
        self.ThirdWindow2Ui = Ui_ThirdWindow2()
        self.ThirdWindow2Ui.setupUi(ThirdWindow2)
        ThirdWindow2.show()
        midWindow.hide()



class Ui_ThirdWindow2(object):
    def setupUi(self, ThirdWindow2):
        ThirdWindow2.setObjectName("ThirdWindow2")
        ThirdWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 10, 491, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.cs137cs133 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs137cs133.setObjectName("cs137cs133")
        self.gridLayout.addWidget(self.cs137cs133, 1, 1, 1, 1)
        self.cs137cs133E = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs137cs133E.setObjectName("cs137cs133E")
        self.gridLayout.addWidget(self.cs137cs133E, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.cs134cs137 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs134cs137.setObjectName("cs134cs137")
        self.gridLayout.addWidget(self.cs134cs137, 2, 1, 1, 1)
        self.cs134cs137E = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs134cs137E.setObjectName("cs134cs137E")
        self.gridLayout.addWidget(self.cs134cs137E, 2, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.cs135cs137 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs135cs137.setObjectName("cs135cs137")
        self.gridLayout.addWidget(self.cs135cs137, 3, 1, 1, 1)
        self.cs135cs137E = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs135cs137E.setObjectName("cs135cs137E")
        self.gridLayout.addWidget(self.cs135cs137E, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.eu154eu153 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu154eu153.setObjectName("eu154eu153")
        self.gridLayout.addWidget(self.eu154eu153, 4, 1, 1, 1)
        self.eu154eu153E = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu154eu153E.setObjectName("eu154eu153E")
        self.gridLayout.addWidget(self.eu154eu153E, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 3, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.sm150sm149 = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm150sm149.setObjectName("sm150sm149")
        self.gridLayout.addWidget(self.sm150sm149, 5, 1, 1, 1)
        self.sm150sm149E = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm150sm149E.setObjectName("sm150sm149E")
        self.gridLayout.addWidget(self.sm150sm149E, 5, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.sm152sm149 = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm152sm149.setObjectName("sm152sm149")
        self.gridLayout.addWidget(self.sm152sm149, 6, 1, 1, 1)
        self.sm152sm149E = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm152sm149E.setObjectName("sm152sm149E")
        self.gridLayout.addWidget(self.sm152sm149E, 6, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 3, 2, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.pu240pu239 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu240pu239.setObjectName("pu240pu239")
        self.gridLayout.addWidget(self.pu240pu239, 7, 1, 1, 1)
        self.pu240pu239E = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu240pu239E.setObjectName("pu240pu239E")
        self.gridLayout.addWidget(self.pu240pu239E, 7, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.pu241pu239 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu241pu239.setObjectName("pu241pu239")
        self.gridLayout.addWidget(self.pu241pu239, 8, 1, 1, 1)
        self.pu241pu239E = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu241pu239E.setObjectName("pu241pu239E")
        self.gridLayout.addWidget(self.pu241pu239E, 8, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.pu242pu239 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu242pu239.setObjectName("pu242pu239")
        self.gridLayout.addWidget(self.pu242pu239, 9, 1, 1, 1)
        self.pu242pu239E = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu242pu239E.setObjectName("pu242pu239E")
        self.gridLayout.addWidget(self.pu242pu239E, 9, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.ba136ba138 = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba136ba138.setObjectName("ba136ba138")
        self.gridLayout.addWidget(self.ba136ba138, 10, 1, 1, 1)
        self.ba136ba138E = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba136ba138E.setObjectName("ba136ba138E")
        self.gridLayout.addWidget(self.ba136ba138E, 10, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 3, 3, 1, 1)
        ThirdWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ThirdWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow2)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow2.setStatusBar(self.statusbar)
        self.retranslateUi(ThirdWindow2)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow2)

    def retranslateUi(self, ThirdWindow2):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow2.setWindowTitle(_translate("ThirdWindow2", "MainWindow"))
        self.label_3.setText(_translate("ThirdWindow2", "Labels"))
        self.label.setText(_translate("ThirdWindow2", "Ratios"))
        self.label_2.setText(_translate("ThirdWindow2", "Error"))
        self.label_4.setText(_translate("ThirdWindow2", "137Cs/133Cs"))
        self.label_5.setText(_translate("ThirdWindow2", "134Cs/137Cs"))
        self.radioButton.setText(_translate("ThirdWindow2", "Set Same Error"))
        self.label_6.setText(_translate("ThirdWindow2", "135Cs/137Cs"))
        self.label_7.setText(_translate("ThirdWindow2", "154Eu/153Eu"))
        self.pushButton.setText(_translate("ThirdWindow2", "Next"))
        self.label_8.setText(_translate("ThirdWindow2", "150Sm/149Sm"))
        self.label_9.setText(_translate("ThirdWindow2", "152Sm/149Sm"))
        self.pushButton_2.setText(_translate("ThirdWindow2", "Cancel"))
        self.label_10.setText(_translate("ThirdWindow2", "240Pu/239Pu"))
        self.label_11.setText(_translate("ThirdWindow2", "241Pu/239Pu"))
        self.label_12.setText(_translate("ThirdWindow2", "242Pu/239Pu"))
        self.label_13.setText(_translate("ThirdWindow2", "136Ba/138Ba"))
        self.radioButton_2.setText(_translate("ThirdWindow2", "Error in %"))
        self.pushButton.clicked.connect(self.next_btn)
        self.pushButton_2.clicked.connect(self.cancel)
        
    def cancel(self):
        sys.exit(0)
        
    def next_btn(self):
        ratios = []
        cs137cs133 = float(self.cs137cs133.text())
        cs134cs137 = float(self.cs134cs137.text())
        cs135cs137 = float(self.cs135cs137.text())
        eu154eu153 = float(self.eu154eu153.text())
        sm150sm149 = float(self.sm150sm149.text())
        sm152sm149 = float(self.sm152sm149.text())
        pu240pu239 = float(self.pu240pu239.text())
        pu241pu239 = float(self.pu241pu239.text())
        pu242pu239 = float(self.pu242pu239.text())
        ba136ba138 = float(self.ba136ba138.text())


        if cs137cs133 == -1:
            ratios.append(-1)
        else:
            ratios.append(cs137cs133)

        if eu154eu153 == -1:
            ratios.append(-1)
        else:
            ratios.append(eu154eu153)

        if cs134cs137 == -1:
            ratios.append(-1)
        else:
            ratios.append(cs134cs137)

        if cs135cs137 == -1:
            ratios.append(-1)
        else:
            ratios.append(cs135cs137)

        if ba136ba138 == -1:
            ratios.append(-1)
        else:
            ratios.append(ba136ba138)

        if sm150sm149 == -1:
            ratios.append(-1)
        else:
            ratios.append(sm150sm149)

        if sm152sm149 == -1:
            ratios.append(-1)
        else:
            ratios.append(sm152sm149)

        if pu242pu239 == -1:
            ratios.append(-1)
        else:
            ratios.append(pu242pu239)

        if pu241pu239 == -1:
            ratios.append(-1)
        else:
            ratios.append(pu241pu239)
        
        if pu240pu239 == -1:
            ratios.append(-1)
        else:
            ratios.append(pu240pu239)

        if self.radioButton.isChecked():
            values = [self.cs137cs133E.text(), self.eu154eu153E.text(), self.cs134cs137E.text(), self.cs135cs137E.text(), self.ba136ba138E.text(), self.sm150sm149E.text(), self.sm152sm149E.text(), self.pu242pu239E.text(), self.pu241pu239E.text(), self.pu240pu239E.text()]
            for val in values:
                print(val)
                if len(val) != 0:
                    print('taking 23')
                    cs137cs133Ep = float(val)
                    eu154eu153Ep = float(val)
                    cs134cs137Ep = float(val)
                    cs135cs137Ep = float(val)
                    ba136ba138Ep = float(val)
                    sm150sm149Ep = float(val)
                    sm152sm149Ep = float(val)
                    pu242pu239Ep = float(val)
                    pu241pu239Ep = float(val)
                    pu240pu239Ep = float(val)
                
            
        else:
            cs137cs133Ep = float(self.cs137cs133E.text())
            eu154eu153Ep = float(self.eu154eu153E.text())
            cs134cs137Ep = float(self.cs134cs137E.text())
            cs135cs137Ep = float(self.cs135cs137E.text())
            ba136ba138Ep = float(self.ba136ba138E.text())
            sm150sm149Ep = float(self.sm150sm149E.text())
            sm152sm149Ep = float(self.sm152sm149E.text())
            pu242pu239Ep = float(self.pu242pu239E.text())
            pu241pu239Ep = float(self.pu241pu239E.text())
            pu240pu239Ep = float(self.pu240pu239E.text())
            
        if self.radioButton_2.isChecked():
            cs137cs133E = (cs137cs133Ep*cs137cs133)/100
            eu154eu153E = (eu154eu153Ep*eu154eu153)/100
            cs134cs137E = (cs134cs137*cs134cs137Ep)/100
            cs135cs137E = (cs135cs137Ep*cs135cs137)/100
            ba136ba138E = (ba136ba138Ep*ba136ba138)/100
            sm150sm149E = (sm150sm149Ep*sm150sm149)/100
            sm152sm149E = (sm152sm149Ep*sm152sm149)/100
            pu242pu239E = (pu242pu239Ep*pu242pu239)/100
            pu241pu239E = (pu241pu239Ep*pu241pu239)/100
            pu240pu239E = (pu240pu239Ep*pu240pu239)/100
        
        else:
            cs137cs133E = cs137cs133Ep
            eu154eu153E = eu154eu153Ep
            cs134cs137E = cs134cs137Ep
            cs135cs137E = cs135cs137Ep
            ba136ba138E = ba136ba138Ep
            sm150sm149E = sm150sm149Ep
            sm152sm149E = sm152sm149Ep
            pu242pu239E = pu242pu239Ep
            pu241pu239E = pu241pu239Ep
            pu240pu239E = pu240pu239Ep
            
            
        

        errors = []
        if ratios[0] == -1:
            errors.append(-1)
        else:
            errors.append(cs137cs133E)

        if ratios[1] == -1:
            errors.append(-1)
        else:
            errors.append(eu154eu153E)

        if ratios[2] == -1:
            errors.append(-1)
        else:
            errors.append(cs134cs137E)

        if ratios[3] == -1:
            errors.append(-1)
        else:
            errors.append(cs135cs137E)

        if ratios[4] == -1:
            errors.append(-1)
        else:
            errors.append(ba136ba138E)

        if ratios[5] == -1:
            errors.append(-1)
        else:
            errors.append(sm150sm149E)

        if ratios[6] == -1:
            errors.append(-1)
        else:
            errors.append(sm152sm149E)

        if ratios[7] == -1:
            errors.append(-1)
        else:
            errors.append(pu242pu239E)

        if ratios[8] == -1:
            errors.append(-1)
        else:
            errors.append(pu241pu239E)

        if ratios[9] == -1:
            errors.append(-1)
        else:
            errors.append(pu240pu239E)


        

        
            
            
        global savedName
        current_dir = os.getcwd()
        current_dir = current_dir + '/' + savedName
        with open(current_dir + '/sheet_names.csv', 'r') as f:
            reader = csv.reader(f)
            sheet_names = list(reader.__next__())
            time_range = [float(x) for x in reader.__next__()]
            r = [float(x) for x in reader.__next__()]
        #print(sheet_names)
        #print(time_range)
        #print(r)
        #d = pd.read_csv(current_dir + '/sheet_names.csv', header = None)
        
        file_names = ['137CS  133Cs', '154Eu  153Eu', '134Cs  137Cs',
                      '135Cs  137Cs', '136Ba  138Ba', '150Sm  149Sm', '152Sm  149Sm', '242Pu  239Pu',
                      '241Pu  239Pu', '240Pu  239Pu']
        #sheet_names = list(d.iloc[0])
        #time_range = list(d.iloc[1])
        #r = list(d.iloc[2])
        y = len(time_range)
        x = len(r)
        
        num_plots = len(sheet_names)
        if num_plots <= 5:
            row = 1
            col = num_plots

        else:
            col = 5
            row = math.ceil(num_plots/5)

        u = 1
        fig = plt.figure(figsize = plt.figaspect(0.5))
        
        count = 0
        maxVal_param = []
        maxVal = -1000000000000000000
        final_wind = []
        for sheet in sheet_names:
            dfs = []
            dfs_size = 0
            for name in file_names:
                #print(sheet)
                dfs.append(pd.read_csv(current_dir + '/' + sheet + name + '.csv', header = 0, index_col = 0))
                dfs_size = dfs_size + 1
            matrix_dfs = []
            for d in dfs:
                matrix_dfs.append(d.values)
                #print('d values ', d.values)
            temp_dfs = []
            temp1 = []
            temp2 = []
            temp_error = []
            for k in range(dfs_size):
                if ratios[k] != -1 and errors[k] != -1:
                #print(((matrix_dfs[k] - ratios[k])**2)/(errors[k]**2))
                #print(np.exp(((matrix_dfs[k] - ratios[k])**2)/(errors[k]**2)))
                    temp1.append((np.square(ratios[k] - matrix_dfs[k]))/(2*(np.square(0.14*matrix_dfs[k]))))
                    temp2.append(np.log(1/((0.14*matrix_dfs[k])*math.sqrt(2*math.pi))))
                    #Error Log L(M|Tmes) = Sum[ (Tmes - Tsim)/(error_sim^2))^2 * (error_mes^2 + error_sim^2)]
                    temp_error.append(np.square(np.divide((ratios[k] - matrix_dfs[k]),(np.square(0.14*matrix_dfs[k])), out = np.zeros_like(matrix_dfs[k]), where = matrix_dfs[k] != 0)) * (errors[k]**2 + np.square(0.14*matrix_dfs[k])))
            a = 0
            for i in range(0, len(temp2)):
                a = a + temp2[i]
            #a = reduce((lambda x, y: x + y), temp2)
            b = 0
            for i in range(0, len(temp1)):
                b = b + temp1[i]
            
            error_value = 0
            
            for i in range(0, len(temp_error)):
                error_value = error_value + temp_error[i]
            #temp1 = reduce((lambda x, y: x + y), temp1)
            #print('a ', a)
            ans = (a - b)
            print(a.shape)
            #print(error_value)
            #if 
            maxVal_param.append(ans.max())
            #print(ans)
            #print(ans.max())
            ans = ans[..., 1:]
            num_row, num_col = ans.shape
            maxVal = -1000000000000
            maxX = 0
            maxY = 0
            error = 0
            for i in range(0, num_row):
                for j in range(0, num_col):
                    if ans[i, j] > maxVal:
                        #print(maxVal)
                        maxVal = ans[i, j]
                        maxX = i
                        maxY = j
                        error = error_value[i, j]
                        
            rVals = []
            for k in range(dfs_size):
                rVals.append(matrix_dfs[k][maxX, maxY])
            temp_str = '137C/133Cs: {}, 154Eu/153Eu: {}, 134Cs/137Cs {}, 135Cs/137Cs {}, 136Ba/138Ba: {}, 150Sm/149Sm: {}, 152Sm/149Sm: {}, 242Pu/239Pu: {}, 241Pu/239Pu: {}, 240Pu/239Pu: {}'.format(np.round(rVals[0], 2),np.round(rVals[1], 2),np.round(rVals[2], 2),np.round(rVals[3], 2),np.round(rVals[4], 2),np.round(rVals[5], 2),np.round(rVals[6], 2),np.round(rVals[7], 2),np.round(rVals[8], 2),np.round(rVals[9], 2))
            final_wind.append(temp_str)
            #print(ans)
            print(maxVal, maxX, maxY)
            for i in range(len(matrix_dfs)):
                print(matrix_dfs[i][maxX, maxY])
            
            ak = pd.DataFrame(index = r, columns = time_range)
            ak = pd.DataFrame(ans)
            #ak = ak.drop(columns = [0], axis = 0)
            ak.to_csv(current_dir + '/' + sheet + '_out.csv')
            
            ax = fig.add_subplot(row, col, u, projection = '3d')
            s = r'Max Val: {:.2f} $\pm$ {:.2f} X: {:.1f}, Y: {:.1f}'.format(maxVal, error, maxX, maxY)
            #r"Max Val: " + str(maxVal) + r"$\pm$ " + str(error) + r' X: ' + str(maxX) + 'Y: ' + str(maxY)
            ax.set_title(s)
            u = u + 1
            x, y = ak.shape
            x = range(x)
            y = range(y)
            print(len(x), len(y), ans.shape)
            X, Y = np.meshgrid(x, y)
            ax.contourf(X, Y, np.transpose(ans))
            #print(ak)
        MainWindow.hide()
        midWindow.hide()
        SecondWindow.hide()
        #ThirdWindow.hide()
        ThirdWindow2.hide()
        
        self.finalWindowUi = Ui_FinalWindow()
        self.finalWindowUi.setupUi(FinalWindow)
        finText = ''
        for i in range(len(final_wind)):
            finText = finText + final_wind[i] + '\n'
        self.finalWindowUi.label.setText(finText)
        self.finalWindowUi.label_2.setText('')
        
        FinalWindow.show()
        plt.show()
        print(self)
        #print(max(maxVal))
        
        
        


"""THIRD WINDOW V1. THIS IS WHERE THE USER ENTERS THE INPUT INDIVIDUALLY. THE CALCULATIONS ARE MADE AND GRAPHS ARE PLOTTED.


TO DO: NEED TO MAKE THE PAGE CLOSE ONCE THE GRPAHS ARE PLOTTED.
       NEED TO IMPLEMENT V2 FOR PEOPLE TO ENTER VALUES AS RATIOS DIRECTLY."""


class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 10, 551, 499))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.cs137 = QtWidgets.QLabel(self.layoutWidget)
        self.cs137.setObjectName("cs137")
        self.gridLayout.addWidget(self.cs137, 1, 0, 1, 1)
        self.cs137Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs137Field.setObjectName("cs137Field")
        self.gridLayout.addWidget(self.cs137Field, 1, 1, 1, 2)
        self.cs137Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs137Error.setObjectName("cs137Error")
        self.gridLayout.addWidget(self.cs137Error, 1, 3, 1, 1)
        self.cs133 = QtWidgets.QLabel(self.layoutWidget)
        self.cs133.setObjectName("cs133")
        self.gridLayout.addWidget(self.cs133, 2, 0, 1, 1)
        self.cs133Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs133Field.setObjectName("cs133Field")
        self.gridLayout.addWidget(self.cs133Field, 2, 1, 1, 2)
        self.cs133Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs133Error.setObjectName("cs133Error")
        self.gridLayout.addWidget(self.cs133Error, 2, 3, 1, 1)
        self.cs134 = QtWidgets.QLabel(self.layoutWidget)
        self.cs134.setObjectName("cs134")
        self.gridLayout.addWidget(self.cs134, 3, 0, 1, 1)
        self.cs134Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs134Field.setObjectName("cs134Field")
        self.gridLayout.addWidget(self.cs134Field, 3, 1, 1, 2)
        self.cs134Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs134Error.setObjectName("cs134Error")
        self.gridLayout.addWidget(self.cs134Error, 3, 3, 1, 1)
        self.cs135 = QtWidgets.QLabel(self.layoutWidget)
        self.cs135.setObjectName("cs135")
        self.gridLayout.addWidget(self.cs135, 4, 0, 1, 1)
        self.cs135Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs135Field.setObjectName("cs135Field")
        self.gridLayout.addWidget(self.cs135Field, 4, 1, 1, 2)
        self.cs135Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs135Error.setObjectName("cs135Error")
        self.gridLayout.addWidget(self.cs135Error, 4, 3, 1, 1)
        self.ba136 = QtWidgets.QLabel(self.layoutWidget)
        self.ba136.setObjectName("ba136")
        self.gridLayout.addWidget(self.ba136, 5, 0, 1, 1)
        self.ba136Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba136Field.setObjectName("ba136Field")
        self.gridLayout.addWidget(self.ba136Field, 5, 1, 1, 2)
        self.ba136Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba136Error.setObjectName("ba136Error")
        self.gridLayout.addWidget(self.ba136Error, 5, 3, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 5, 4, 2, 1)
        self.ba138 = QtWidgets.QLabel(self.layoutWidget)
        self.ba138.setObjectName("ba138")
        self.gridLayout.addWidget(self.ba138, 6, 0, 1, 1)
        self.ba138Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba138Field.setObjectName("ba138Field")
        self.gridLayout.addWidget(self.ba138Field, 6, 2, 1, 1)
        self.ba138Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba138Error.setObjectName("ba138Error")
        self.gridLayout.addWidget(self.ba138Error, 6, 3, 1, 1)
        self.eu154 = QtWidgets.QLabel(self.layoutWidget)
        self.eu154.setObjectName("eu154")
        self.gridLayout.addWidget(self.eu154, 7, 0, 1, 1)
        self.eu154Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu154Field.setObjectName("eu154Field")
        self.gridLayout.addWidget(self.eu154Field, 7, 2, 1, 1)
        self.eu154Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu154Error.setObjectName("eu154Error")
        self.gridLayout.addWidget(self.eu154Error, 7, 3, 1, 1)
        self.eu153 = QtWidgets.QLabel(self.layoutWidget)
        self.eu153.setObjectName("eu153")
        self.gridLayout.addWidget(self.eu153, 8, 0, 1, 1)
        self.eu153Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu153Field.setObjectName("eu153Field")
        self.gridLayout.addWidget(self.eu153Field, 8, 1, 1, 2)
        self.eu153Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu153Error.setObjectName("eu153Error")
        self.gridLayout.addWidget(self.eu153Error, 8, 3, 1, 1)
        self.sm150 = QtWidgets.QLabel(self.layoutWidget)
        self.sm150.setObjectName("sm150")
        self.gridLayout.addWidget(self.sm150, 9, 0, 1, 1)
        self.sm150Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm150Field.setObjectName("sm150Field")
        self.gridLayout.addWidget(self.sm150Field, 9, 1, 1, 2)
        self.sm150Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm150Error.setObjectName("sm150Error")
        self.gridLayout.addWidget(self.sm150Error, 9, 3, 1, 1)
        self.sm149 = QtWidgets.QLabel(self.layoutWidget)
        self.sm149.setObjectName("sm149")
        self.gridLayout.addWidget(self.sm149, 10, 0, 1, 1)
        self.sm149Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm149Field.setObjectName("sm149Field")
        self.gridLayout.addWidget(self.sm149Field, 10, 1, 1, 2)
        self.sm149Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm149Error.setObjectName("sm149Error")
        self.gridLayout.addWidget(self.sm149Error, 10, 3, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 10, 4, 2, 1)
        self.sm152 = QtWidgets.QLabel(self.layoutWidget)
        self.sm152.setObjectName("sm152")
        self.gridLayout.addWidget(self.sm152, 11, 0, 1, 1)
        self.sm152Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm152Field.setObjectName("sm152Field")
        self.gridLayout.addWidget(self.sm152Field, 11, 1, 1, 2)
        self.sm152Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm152Error.setObjectName("sm152Error")
        self.gridLayout.addWidget(self.sm152Error, 11, 3, 1, 1)
        self.pu240 = QtWidgets.QLabel(self.layoutWidget)
        self.pu240.setObjectName("pu240")
        self.gridLayout.addWidget(self.pu240, 12, 0, 1, 1)
        self.pu240Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu240Field.setObjectName("pu240Field")
        self.gridLayout.addWidget(self.pu240Field, 12, 1, 1, 2)
        self.pu240Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu240Error.setObjectName("pu240Error")
        self.gridLayout.addWidget(self.pu240Error, 12, 3, 1, 1)
        self.pu239 = QtWidgets.QLabel(self.layoutWidget)
        self.pu239.setObjectName("pu239")
        self.gridLayout.addWidget(self.pu239, 13, 0, 1, 1)
        self.pu239Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu239Field.setObjectName("pu239Field")
        self.gridLayout.addWidget(self.pu239Field, 13, 1, 1, 2)
        self.pu239Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu239Error.setObjectName("pu239Error")
        self.gridLayout.addWidget(self.pu239Error, 13, 3, 1, 1)
        self.pu241 = QtWidgets.QLabel(self.layoutWidget)
        self.pu241.setObjectName("pu241")
        self.gridLayout.addWidget(self.pu241, 14, 0, 1, 1)
        self.pu241Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu241Field.setObjectName("pu241Field")
        self.gridLayout.addWidget(self.pu241Field, 14, 1, 1, 2)
        self.pu241Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu241Error.setObjectName("pu241Error")
        self.gridLayout.addWidget(self.pu241Error, 14, 3, 1, 1)
        self.pu242 = QtWidgets.QLabel(self.layoutWidget)
        self.pu242.setObjectName("pu242")
        self.gridLayout.addWidget(self.pu242, 15, 0, 1, 1)
        self.pu242Field = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu242Field.setObjectName("pu242Field")
        self.gridLayout.addWidget(self.pu242Field, 15, 1, 1, 2)
        self.pu242Error = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu242Error.setObjectName("pu242Error")
        self.gridLayout.addWidget(self.pu242Error, 15, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 3, 4, 1, 1)
        ThirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "ThirdWindow"))
        self.label_3.setText(_translate("ThirdWindow", "TextLabel"))
        self.label.setText(_translate("ThirdWindow", "Value"))
        self.label_2.setText(_translate("ThirdWindow", "Error (%)"))
        self.cs137.setText(_translate("ThirdWindow", "Cs 137"))
        self.cs133.setText(_translate("ThirdWindow", "Cs 133"))
        self.cs134.setText(_translate("ThirdWindow", "Cs 134"))
        self.cs135.setText(_translate("ThirdWindow", "Cs 135"))
        self.ba136.setText(_translate("ThirdWindow", "Ba 136"))
        self.nextBtn.setText(_translate("ThirdWindow", "Next"))
        self.ba138.setText(_translate("ThirdWindow", "Ba 138"))
        self.eu154.setText(_translate("ThirdWindow", "Eu 154"))
        self.eu153.setText(_translate("ThirdWindow", "Eu 153"))
        self.sm150.setText(_translate("ThirdWindow", "Sm 150"))
        self.sm149.setText(_translate("ThirdWindow", "Sm 149"))
        self.cancelBtn.setText(_translate("ThirdWindow", "Cancel"))
        self.sm152.setText(_translate("ThirdWindow", "Sm 152"))
        self.pu240.setText(_translate("ThirdWindow", "Pu 240"))
        self.pu239.setText(_translate("ThirdWindow", "Pu 239"))
        self.pu241.setText(_translate("ThirdWindow", "Pu 241"))
        self.pu242.setText(_translate("ThirdWindow", "Pu 242"))
        self.radioButton.setText(_translate("ThirdWindow", "Set Same Error"))
        self.nextBtn.clicked.connect(self.next_btn)
        self.cancelBtn.clicked.connect(self.cancel)
        
    def cancel(self):
        sys.exit(0)

    def next_btn(self):
        ratios = []
        cs137Val = float(self.cs137Field.text())
        cs133Val = float(self.cs133Field.text())
        cs134Val = float(self.cs134Field.text())
        cs135Val = float(self.cs135Field.text())
        ba136Val = float(self.ba136Field.text())
        ba138Val = float(self.ba138Field.text())
        eu154Val = float(self.eu154Field.text())
        eu153Val = float(self.eu153Field.text())
        sm150Val = float(self.sm150Field.text())
        sm149Val = float(self.sm149Field.text())
        sm152Val = float(self.sm152Field.text())
        pu240Val = float(self.pu240Field.text())
        pu241Val = float(self.pu241Field.text())
        pu242Val = float(self.pu242Field.text())
        pu239Val = float(self.pu239Field.text())

        if cs137Val == -1 or cs133Val == -1:
            ratios.append(-1)
        else:
            ratios.append(cs137Val / cs133Val)

        if eu154Val == -1 or eu153Val == -1:
            ratios.append(-1)
        else:
            ratios.append(eu154Val / eu153Val)

        if cs134Val == -1 or cs137Val == -1:
            ratios.append(-1)
        else:
            ratios.append(cs134Val / cs137Val)

        if cs135Val == -1 or cs137Val == -1:
            ratios.append(-1)
        else:
            ratios.append(cs135Val / cs137Val)

        if ba136Val == -1 or ba138Val == -1:
            ratios.append(-1)
        else:
            ratios.append(ba136Val / ba138Val)

        if sm150Val == -1 or sm149Val == -1:
            ratios.append(-1)
        else:
            ratios.append(sm150Val / sm149Val)

        if sm152Val == -1 or sm149Val == -1:
            ratios.append(-1)
        else:
            ratios.append(sm152Val / sm149Val)

        if pu242Val == -1 or pu239Val == -1:
            ratios.append(-1)
        else:
            ratios.append(pu242Val / pu239Val)

        if pu241Val == -1 or pu239Val == -1:
            ratios.append(-1)
        else:
            ratios.append(pu241Val / pu239Val)
        
        if pu240Val == -1 or pu239Val == -1:
            ratios.append(-1)
        else:
            ratios.append(pu240Val / pu239Val)


        

        
        

        if self.radioButton.isChecked():
            values = [self.cs137Error.text(), self.cs133Error.text(), self.cs134Error.text(),self.cs135Error.text(), self.ba136Error.text(), self.ba138Error.text(), self.eu154Error.text(), self.eu153Error.text(), self.sm150Error.text(), self.sm149Error.text(), self.sm152Error.text(), self.pu240Error.text(), self.pu241Error.text(), self.pu242Error.text(), self.pu239Error.text()]
            for val in values:
                print(val)
                if len(val) != 0:
                    print('taking 23')
                    cs137Errorp = float(val)
                    cs133Errorp = float(val)
                    cs134Errorp = float(val)
                    cs135Errorp = float(val)
                    ba136Errorp = float(val)
                    ba138Errorp = float(val)
                    eu154Errorp = float(val)
                    eu153Errorp = float(val)
                    sm150Errorp = float(val)
                    sm149Errorp = float(val)
                    sm152Errorp = float(val)
                    pu240Errorp = float(val)
                    pu241Errorp = float(val)
                    pu242Errorp = float(val)
                    pu239Errorp = float(val)
                
            
        else:
            cs137Errorp = float(self.cs137Error.text())
            cs133Errorp = float(self.cs133Error.text())
            cs134Errorp = float(self.cs134Error.text())
            cs135Errorp = float(self.cs135Error.text())
            ba136Errorp = float(self.ba136Error.text())
            ba138Errorp = float(self.ba138Error.text())
            eu154Errorp = float(self.eu154Error.text())
            eu153Errorp = float(self.eu153Error.text())
            sm150Errorp = float(self.sm150Error.text())
            sm149Errorp = float(self.sm149Error.text())
            sm152Errorp = float(self.sm152Error.text())
            pu240Errorp = float(self.pu240Error.text())
            pu241Errorp = float(self.pu241Error.text())
            pu242Errorp = float(self.pu242Error.text())
            pu239Errorp = float(self.pu239Error.text())

        cs137Error = (cs137Val*cs137Errorp)/100
        cs133Error = (cs133Val*cs133Errorp)/100
        cs134Error = (cs134Val*cs134Errorp)/100
        cs135Error = (cs135Val*cs135Errorp)/100
        ba136Error = (ba136Val*ba136Errorp)/100
        ba138Error = (ba138Val*ba138Errorp)/100
        eu154Error = (eu154Val*eu154Errorp)/100
        eu153Error = (eu153Val*eu153Errorp)/100
        sm150Error = (sm150Val*sm150Errorp)/100
        sm149Error = (sm149Val*sm149Errorp)/100
        sm152Error = (sm152Val*sm152Errorp)/100
        pu240Error = (pu240Val*pu240Errorp)/100
        pu241Error = (pu241Val*pu241Errorp)/100
        pu242Error = (pu242Val*pu242Errorp)/100
        pu239Error = (pu239Val*pu239Errorp)/100

        errors = []
        if ratios[0] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[0]*math.sqrt((float(cs137Error)/float(cs137Val))**2 + (float(cs133Error)/float(cs133Val))**2))

        if ratios[1] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[1]*math.sqrt((float(eu154Error)/float(eu154Val))**2 + (float(eu153Error)/float(eu153Val))**2))

        if ratios[2] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[2]*math.sqrt((float(cs134Error)/float(cs134Val))**2 + (float(cs137Error)/float(cs137Val))**2))

        if ratios[3] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[3]*math.sqrt((float(cs135Error)/float(cs135Val))**2 + (float(cs137Error)/float(cs137Val))**2))

        if ratios[4] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[4]*math.sqrt((float(ba136Error)/float(ba136Val))**2 + (float(ba138Error)/float(ba138Val))**2))

        if ratios[5] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[5]*math.sqrt((float(sm150Error)/float(sm150Val))**2 + (float(sm149Error)/float(sm149Val))**2))

        if ratios[6] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[6]*math.sqrt((float(sm152Error)/float(sm152Val))**2 + (float(sm149Error)/float(sm149Val))**2))

        if ratios[7] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[7]*math.sqrt((float(pu242Error)/float(pu242Val))**2 + (float(pu239Error)/float(pu239Val))**2))

        if ratios[8] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[8]*math.sqrt((float(pu241Error)/float(pu241Val))**2 + (float(pu239Error)/float(pu239Val))**2))

        if ratios[9] == -1:
            errors.append(-1)
        else:
            errors.append(ratios[9]*math.sqrt((float(pu240Error)/float(pu240Val))**2 + (float(pu239Error)/float(pu239Val))**2))


        

        
            
            
        global savedName
        current_dir = os.getcwd()
        current_dir = current_dir + '/' + savedName
        with open(current_dir + '/sheet_names.csv', 'r') as f:
            reader = csv.reader(f)
            sheet_names = list(reader.__next__())
            time_range = [float(x) for x in reader.__next__()]
            r = [float(x) for x in reader.__next__()]
        #print(sheet_names)
        #print(time_range)
        #print(r)
        #d = pd.read_csv(current_dir + '/sheet_names.csv', header = None)
        
        file_names = ['137CS  133Cs', '154Eu  153Eu', '134Cs  137Cs',
                      '135Cs  137Cs', '136Ba  138Ba', '150Sm  149Sm', '152Sm  149Sm', '242Pu  239Pu',
                      '241Pu  239Pu', '240Pu  239Pu']
        #sheet_names = list(d.iloc[0])
        #time_range = list(d.iloc[1])
        #r = list(d.iloc[2])
        y = len(time_range)
        x = len(r)
        
        num_plots = len(sheet_names)
        if num_plots <= 5:
            row = 1
            col = num_plots

        else:
            col = 5
            row = math.ceil(num_plots/5)

        u = 1
        fig = plt.figure(figsize = plt.figaspect(0.5))
        
        count = 0
        maxVal_param = []
        maxVal = -1000000000000000000
        for sheet in sheet_names:
            dfs = []
            dfs_size = 0
            for name in file_names:
                #print(sheet)
                dfs.append(pd.read_csv(current_dir + '/' + sheet + name + '.csv'))
                dfs_size = dfs_size + 1
            matrix_dfs = []
            for d in dfs:
                matrix_dfs.append(d.values)
            temp_dfs = []
            temp1 = []
            temp2 = []
            for k in range(dfs_size):
                if ratios[k] != -1 and errors[k] != -1:
                    
                    #print(((matrix_dfs[k] - ratios[k])**2)/(errors[k]**2))
                    #print(np.exp(((matrix_dfs[k] - ratios[k])**2)/(errors[k]**2)))
                    temp1.append(np.divide(np.square(matrix_dfs[k] - ratios[k]), 2*(errors[k]**2), out = np.zeros_like(matrix_dfs[k]), where = errors[k] != 0))
                    temp2.append(np.log(1/(errors[k]*math.sqrt(2*math.pi))))
            
            a = reduce((lambda x, y: x + y), temp2)
            temp1 = reduce((lambda x, y: x + y), temp1)
            #print('YO YO', type(temp1))
            ans = -(temp1 - a)
            #if 
            ans = ans[..., 1:]
            num_row, num_col = ans.shape
            maxVal = -1000000000000
            maxX = 0
            maxY = 0
            for i in num_row:
                for j in num_col:
                    if ans[i, j] > maxVal:
                        maxVal = ans[i, j]
                        maxX = i
                        maxY = j
                        
                    
            #print(ans)
            print(maxVal)
            ak = pd.DataFrame(index = r, columns = time_range)
            ak = pd.DataFrame(ans)
            #ak = ak.drop(columns = [0], axis = 0)
            ak.to_csv(current_dir + '/' + sheet + '_out.csv')
            
            
            ax = fig.add_subplot(row, col, u, projection = '3d')
            ax.set_title('Max Val: ', maxVal, 'X: ', maxX, 'Y: ', maxY)
            u = u + 1
            x, y = ak.shape
            x = range(x)
            y = range(y)
            print(len(x), len(y), ans.shape)
            X, Y = np.meshgrid(x, y)
            ax.contourf(X, Y, np.transpose(ans))
            #print(ak)
        MainWindow.hide()
        midWindow.hide()
        SecondWindow.hide()
        ThirdWindow.hide()
        ThirdWindow2.hide()
        plt.show()
        print(self)
        
        
        #print(max(maxVal))
        #global window2
        #window2.hide()
        
        
class Ui_FinalWindow(object):
    def setupUi(self, FinalWindow):
        FinalWindow.setObjectName("FinalWindow")
        FinalWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FinalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        FinalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FinalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        FinalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FinalWindow)
        self.statusbar.setObjectName("statusbar")
        FinalWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FinalWindow)
        QtCore.QMetaObject.connectSlotsByName(FinalWindow)

    def retranslateUi(self, FinalWindow):
        _translate = QtCore.QCoreApplication.translate
        FinalWindow.setWindowTitle(_translate("FinalWindow", "FinalWindow"))
        self.label.setText(_translate("FinalWindow", "TextLabel"))
        self.label_2.setText(_translate("FinalWindow", "TextLabel"))


class bhat1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 220, 461, 32))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.bhattacharya = QtWidgets.QPushButton(self.widget)
        self.bhattacharya.setObjectName("bhattacharya")
        self.gridLayout.addWidget(self.bhattacharya, 0, 0, 1, 1)
        self.maxlike = QtWidgets.QPushButton(self.widget)
        self.maxlike.setObjectName("maxlike")
        self.gridLayout.addWidget(self.maxlike, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bhattacharya.setText(_translate("MainWindow", "Bhattacharya"))
        self.maxlike.setText(_translate("MainWindow", "Maximum Likelihood"))
        self.bhattacharya.clicked.connect(self.bhatt)
        self.maxlike.clicked.connect(self.maxlikeBtn)
        

        
    def bhatt(self):
        bhat1Window.hide()
        self.bhatWindowUi = bhat2()
        self.bhatWindowUi.setupUi(bhat2Window)
        bhat2Window.show()
        
        

    def maxlikeBtn(self):
        bhat1Window.hide()
        self.MainWindowUi = Ui_MainWindow()
        self.MainWindowUi.setupUi(MainWindow)
        MainWindow.show()


        


class bhat2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 220, 451, 32))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.user = QtWidgets.QPushButton(self.widget)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 0, 0, 1, 1)
        self.analyst = QtWidgets.QPushButton(self.widget)
        self.analyst.setObjectName("analyst")
        self.gridLayout.addWidget(self.analyst, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user.setText(_translate("MainWindow", "User"))
        self.analyst.setText(_translate("MainWindow", "Analyst"))
        self.user.clicked.connect(self.userBtn)
        self.analyst.clicked.connect(self.analystBtn)

    def userBtn(self):
        bhat2Window.hide()
        self.MainWindowUi = bhat3()
        self.MainWindowUi.setupUi(bhat3Window)
        bhat3Window.show()

    def analystBtn(self):
        bhat2Window.hide()
        self.MainWindowUi = bhat4()
        self.MainWindowUi.setupUi(bhat3Window)
        bhat3Window.show()


class bhat3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 90, 511, 340))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mean = QtWidgets.QLabel(self.layoutWidget)
        self.mean.setObjectName("mean")
        self.gridLayout.addWidget(self.mean, 0, 1, 1, 1)
        self.standarddeviation = QtWidgets.QLabel(self.layoutWidget)
        self.standarddeviation.setObjectName("standarddeviation")
        self.gridLayout.addWidget(self.standarddeviation, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cs137cs133 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs137cs133.setObjectName("cs137cs133")
        self.gridLayout.addWidget(self.cs137cs133, 1, 1, 1, 1)
        self.cs137cs133E = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs137cs133E.setObjectName("cs137cs133E")
        self.gridLayout.addWidget(self.cs137cs133E, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.cs134cs137 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs134cs137.setObjectName("cs134cs137")
        self.gridLayout.addWidget(self.cs134cs137, 2, 1, 1, 1)
        self.cs134cs137E = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs134cs137E.setObjectName("cs134cs137E")
        self.gridLayout.addWidget(self.cs134cs137E, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.cs135cs137 = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs135cs137.setObjectName("cs135cs137")
        self.gridLayout.addWidget(self.cs135cs137, 3, 1, 1, 1)
        self.cs135cs137E = QtWidgets.QLineEdit(self.layoutWidget)
        self.cs135cs137E.setObjectName("cs135cs137E")
        self.gridLayout.addWidget(self.cs135cs137E, 3, 2, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 3, 3, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 2, 1)
        self.eu154eu153 = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu154eu153.setObjectName("eu154eu153")
        self.gridLayout.addWidget(self.eu154eu153, 4, 1, 2, 1)
        self.eu154eu153E = QtWidgets.QLineEdit(self.layoutWidget)
        self.eu154eu153E.setObjectName("eu154eu153E")
        self.gridLayout.addWidget(self.eu154eu153E, 4, 2, 2, 1)
        self.backBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 5, 3, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.sm150sm149 = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm150sm149.setObjectName("sm150sm149")
        self.gridLayout.addWidget(self.sm150sm149, 6, 1, 1, 1)
        self.sm150sm149E = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm150sm149E.setObjectName("sm150sm149E")
        self.gridLayout.addWidget(self.sm150sm149E, 6, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.sm152sm149 = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm152sm149.setObjectName("sm152sm149")
        self.gridLayout.addWidget(self.sm152sm149, 7, 1, 1, 1)
        self.sm152sm149E = QtWidgets.QLineEdit(self.layoutWidget)
        self.sm152sm149E.setObjectName("sm152sm149E")
        self.gridLayout.addWidget(self.sm152sm149E, 7, 2, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 7, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.pu240pu239 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu240pu239.setObjectName("pu240pu239")
        self.gridLayout.addWidget(self.pu240pu239, 8, 1, 1, 1)
        self.pu240pu239E = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu240pu239E.setObjectName("pu240pu239E")
        self.gridLayout.addWidget(self.pu240pu239E, 8, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.pu241pu239 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu241pu239.setObjectName("pu241pu239")
        self.gridLayout.addWidget(self.pu241pu239, 9, 1, 1, 1)
        self.pu241pu239E = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu241pu239E.setObjectName("pu241pu239E")
        self.gridLayout.addWidget(self.pu241pu239E, 9, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.pu242pu239 = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu242pu239.setObjectName("pu242pu239")
        self.gridLayout.addWidget(self.pu242pu239, 10, 1, 1, 1)
        self.pu242pu239E = QtWidgets.QLineEdit(self.layoutWidget)
        self.pu242pu239E.setObjectName("pu242pu239E")
        self.gridLayout.addWidget(self.pu242pu239E, 10, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.ba136ba138 = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba136ba138.setObjectName("ba136ba138")
        self.gridLayout.addWidget(self.ba136ba138, 11, 1, 1, 1)
        self.ba136ba138E = QtWidgets.QLineEdit(self.layoutWidget)
        self.ba136ba138E.setObjectName("ba136ba138E")
        self.gridLayout.addWidget(self.ba136ba138E, 11, 2, 1, 1)
        self.errorinp = QtWidgets.QRadioButton(self.layoutWidget)
        self.errorinp.setObjectName("errorinp")
        self.gridLayout.addWidget(self.errorinp, 2, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mean.setText(_translate("MainWindow", "Mean"))
        self.standarddeviation.setText(_translate("MainWindow", "Standard Deviation"))
        self.label_3.setText(_translate("MainWindow", "137Cs/133Cs"))
        self.label_4.setText(_translate("MainWindow", "134Cs/137Cs"))
        self.label_5.setText(_translate("MainWindow", "135Cs/137Cs"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))
        self.label_6.setText(_translate("MainWindow", "154Eu/153Eu"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.label_7.setText(_translate("MainWindow", "150Sm/149Sm"))
        self.label_8.setText(_translate("MainWindow", "152Sm/149Sm"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.label_9.setText(_translate("MainWindow", "240Pu/239Pu"))
        self.label_10.setText(_translate("MainWindow", "241Pu/239Pu"))
        self.label_11.setText(_translate("MainWindow", "242Pu/239Pu"))
        self.label_12.setText(_translate("MainWindow", "136Ba/138Ba"))
        self.errorinp.setText(_translate("MainWindow", "SD in %"))
        self.radioButton.setText(_translate("MainWindow", "Set same error"))
        self.nextBtn.clicked.connect(self.nextFunc)

    def nextFunc(self):
        ratios = []
        cs137cs133 = float(self.cs137cs133.text())
        cs134cs137 = float(self.cs134cs137.text())
        cs135cs137 = float(self.cs135cs137.text())
        eu154eu153 = float(self.eu154eu153.text())
        sm150sm149 = float(self.sm150sm149.text())
        sm152sm149 = float(self.sm152sm149.text())
        pu240pu239 = float(self.pu240pu239.text())
        pu241pu239 = float(self.pu241pu239.text())
        pu242pu239 = float(self.pu242pu239.text())
        ba136ba138 = float(self.ba136ba138.text())


        if cs137cs133 == -1:
            ratios.append(-1)
        else:
            ratios.append(cs137cs133)

        if eu154eu153 == -1:
            ratios.append(-1)
        else:
            ratios.append(eu154eu153)

        if cs134cs137 == -1:
            ratios.append(-1)
        else:
            ratios.append(cs134cs137)

        if cs135cs137 == -1:
            ratios.append(-1)
        else:
            ratios.append(cs135cs137)

        if ba136ba138 == -1:
            ratios.append(-1)
        else:
            ratios.append(ba136ba138)

        if sm150sm149 == -1:
            ratios.append(-1)
        else:
            ratios.append(sm150sm149)

        if sm152sm149 == -1:
            ratios.append(-1)
        else:
            ratios.append(sm152sm149)

        if pu242pu239 == -1:
            ratios.append(-1)
        else:
            ratios.append(pu242pu239)

        if pu241pu239 == -1:
            ratios.append(-1)
        else:
            ratios.append(pu241pu239)
        
        if pu240pu239 == -1:
            ratios.append(-1)
        else:
            ratios.append(pu240pu239)

        if self.radioButton.isChecked():
            values = [self.cs137cs133E.text(), self.eu154eu153E.text(), self.cs134cs137E.text(), self.cs135cs137E.text(), self.ba136ba138E.text(), self.sm150sm149E.text(), self.sm152sm149E.text(), self.pu242pu239E.text(), self.pu241pu239E.text(), self.pu240pu239E.text()]
            for val in values:
                print(val)
                if len(val) != 0:
                    print('taking 23')
                    cs137cs133Ep = float(val)
                    eu154eu153Ep = float(val)
                    cs134cs137Ep = float(val)
                    cs135cs137Ep = float(val)
                    ba136ba138Ep = float(val)
                    sm150sm149Ep = float(val)
                    sm152sm149Ep = float(val)
                    pu242pu239Ep = float(val)
                    pu241pu239Ep = float(val)
                    pu240pu239Ep = float(val)
                
            
        else:
            cs137cs133Ep = float(self.cs137cs133E.text())
            eu154eu153Ep = float(self.eu154eu153E.text())
            cs134cs137Ep = float(self.cs134cs137E.text())
            cs135cs137Ep = float(self.cs135cs137E.text())
            ba136ba138Ep = float(self.ba136ba138E.text())
            sm150sm149Ep = float(self.sm150sm149E.text())
            sm152sm149Ep = float(self.sm152sm149E.text())
            pu242pu239Ep = float(self.pu242pu239E.text())
            pu241pu239Ep = float(self.pu241pu239E.text())
            pu240pu239Ep = float(self.pu240pu239E.text())
            
        if self.radioButton_2.isChecked():
            cs137cs133E = (cs137cs133Ep*cs137cs133)/100
            eu154eu153E = (eu154eu153Ep*eu154eu153)/100
            cs134cs137E = (cs134cs137*cs134cs137Ep)/100
            cs135cs137E = (cs135cs137Ep*cs135cs137)/100
            ba136ba138E = (ba136ba138Ep*ba136ba138)/100
            sm150sm149E = (sm150sm149Ep*sm150sm149)/100
            sm152sm149E = (sm152sm149Ep*sm152sm149)/100
            pu242pu239E = (pu242pu239Ep*pu242pu239)/100
            pu241pu239E = (pu241pu239Ep*pu241pu239)/100
            pu240pu239E = (pu240pu239Ep*pu240pu239)/100
        
        else:
            cs137cs133E = cs137cs133Ep
            eu154eu153E = eu154eu153Ep
            cs134cs137E = cs134cs137Ep
            cs135cs137E = cs135cs137Ep
            ba136ba138E = ba136ba138Ep
            sm150sm149E = sm150sm149Ep
            sm152sm149E = sm152sm149Ep
            pu242pu239E = pu242pu239Ep
            pu241pu239E = pu241pu239Ep
            pu240pu239E = pu240pu239Ep
            
            
        

        errors = []
        if ratios[0] == -1:
            errors.append(-1)
        else:
            errors.append(cs137cs133E)

        if ratios[1] == -1:
            errors.append(-1)
        else:
            errors.append(eu154eu153E)

        if ratios[2] == -1:
            errors.append(-1)
        else:
            errors.append(cs134cs137E)

        if ratios[3] == -1:
            errors.append(-1)
        else:
            errors.append(cs135cs137E)

        if ratios[4] == -1:
            errors.append(-1)
        else:
            errors.append(ba136ba138E)

        if ratios[5] == -1:
            errors.append(-1)
        else:
            errors.append(sm150sm149E)

        if ratios[6] == -1:
            errors.append(-1)
        else:
            errors.append(sm152sm149E)

        if ratios[7] == -1:
            errors.append(-1)
        else:
            errors.append(pu242pu239E)

        if ratios[8] == -1:
            errors.append(-1)
        else:
            errors.append(pu241pu239E)

        if ratios[9] == -1:
            errors.append(-1)
        else:
            errors.append(pu240pu239E)


        global savedName
        current_dir = os.getcwd()
        current_dir = current_dir + '/' + savedName
        with open(current_dir + '/sheet_names.csv', 'r') as f:
            reader = csv.reader(f)
            sheet_names = list(reader.__next__())
            time_range = [float(x) for x in reader.__next__()]
            r = [float(x) for x in reader.__next__()]
        #print(sheet_names)
        #print(time_range)
        #print(r)
        #d = pd.read_csv(current_dir + '/sheet_names.csv', header = None)
        
        file_names = ['137CS  133Cs', '154Eu  153Eu', '134Cs  137Cs',
                      '135Cs  137Cs', '136Ba  138Ba', '150Sm  149Sm', '152Sm  149Sm', '242Pu  239Pu',
                      '241Pu  239Pu', '240Pu  239Pu']
        #sheet_names = list(d.iloc[0])
        #time_range = list(d.iloc[1])
        #r = list(d.iloc[2])
        y = len(time_range)
        x = len(r)
        
        num_plots = len(sheet_names)
        if num_plots <= 5:
            row = 1
            col = num_plots

        else:
            col = 5
            row = math.ceil(num_plots/5)

        u = 1
        fig = plt.figure(figsize = plt.figaspect(0.5))
        
        count = 0
        maxVal_param = []
        maxVal = -1000000000000000000
        final_wind = []
        for sheet in sheet_names:
            dfs = []
            dfs_size = 0
            for name in file_names:
                #print(sheet)
                dfs.append(pd.read_csv(current_dir + '/' + sheet + name + '.csv', header = 0, index_col = 0))
                dfs_size = dfs_size + 1
            matrix_dfs = []
            for d in dfs:
                matrix_dfs.append(d.values)
                #print('d values ', d.values)
            temp_dfs = []
            temp1 = []
            temp2 = []
            temp_error = []
            for k in range(dfs_size):
                if ratios[k] != -1 and errors[k] != -1:
                #print(((matrix_dfs[k] - ratios[k])**2)/(errors[k]**2))
                #print(np.exp(((matrix_dfs[k] - ratios[k])**2)/(errors[k]**2)))
                    temp1.append((np.square(ratios[k] - matrix_dfs[k]))/(2*(np.square(0.14*matrix_dfs[k]))))
                    temp2.append(np.log(1/((0.14*matrix_dfs[k])*math.sqrt(2*math.pi))))
                    #Error Log L(M|Tmes) = Sum[ (Tmes - Tsim)/(error_sim^2))^2 * (error_mes^2 + error_sim^2)]
                    temp_error.append(np.square(np.divide((ratios[k] - matrix_dfs[k]),(np.square(0.14*matrix_dfs[k])), out = np.zeros_like(matrix_dfs[k]), where = matrix_dfs[k] != 0)) * (errors[k]**2 + np.square(0.14*matrix_dfs[k])))
            a = 0
            for i in range(0, len(temp2)):
                a = a + temp2[i]
            #a = reduce((lambda x, y: x + y), temp2)
            b = 0
            for i in range(0, len(temp1)):
                b = b + temp1[i]
            
            error_value = 0
            
            for i in range(0, len(temp_error)):
                error_value = error_value + temp_error[i]
            #temp1 = reduce((lambda x, y: x + y), temp1)
            #print('a ', a)
            ans = (a - b)
            print(a.shape)
            #print(error_value)
            #if 
            maxVal_param.append(ans.max())
            #print(ans)
            #print(ans.max())
            ans = ans[..., 1:]
            num_row, num_col = ans.shape
            maxVal = -1000000000000
            maxX = 0
            maxY = 0
            error = 0
            for i in range(0, num_row):
                for j in range(0, num_col):
                    if ans[i, j] > maxVal:
                        #print(maxVal)
                        maxVal = ans[i, j]
                        maxX = i
                        maxY = j
                        error = error_value[i, j]
                        
            rVals = []
            for k in range(dfs_size):
                rVals.append(matrix_dfs[k][maxX, maxY])
            temp_str = '137C/133Cs: {}, 154Eu/153Eu: {}, 134Cs/137Cs {}, 135Cs/137Cs {}, 136Ba/138Ba: {}, 150Sm/149Sm: {}, 152Sm/149Sm: {}, 242Pu/239Pu: {}, 241Pu/239Pu: {}, 240Pu/239Pu: {}'.format(np.round(rVals[0], 2),np.round(rVals[1], 2),np.round(rVals[2], 2),np.round(rVals[3], 2),np.round(rVals[4], 2),np.round(rVals[5], 2),np.round(rVals[6], 2),np.round(rVals[7], 2),np.round(rVals[8], 2),np.round(rVals[9], 2))
            final_wind.append(temp_str)
            #print(ans)
            print(maxVal, maxX, maxY)
            for i in range(len(matrix_dfs)):
                print(matrix_dfs[i][maxX, maxY])
            

        

        
        


    
class bhat4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 130, 561, 201))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.meantext = QtWidgets.QLineEdit(self.widget)
        self.meantext.setObjectName("meantext")
        self.gridLayout.addWidget(self.meantext, 0, 0, 1, 2)
        self.meanbrowse = QtWidgets.QPushButton(self.widget)
        self.meanbrowse.setObjectName("meanbrowse")
        self.gridLayout.addWidget(self.meanbrowse, 0, 2, 1, 1)
        self.stdtext = QtWidgets.QLineEdit(self.widget)
        self.stdtext.setObjectName("stdtext")
        self.gridLayout.addWidget(self.stdtext, 1, 0, 1, 2)
        self.stdbrowse = QtWidgets.QPushButton(self.widget)
        self.stdbrowse.setObjectName("stdbrowse")
        self.gridLayout.addWidget(self.stdbrowse, 1, 2, 1, 1)
        self.defaultbtn = QtWidgets.QRadioButton(self.widget)
        self.defaultbtn.setObjectName("defaultbtn")
        self.gridLayout.addWidget(self.defaultbtn, 2, 2, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.widget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 3, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(self.widget)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 3, 1, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(self.widget)
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.meanbrowse.setText(_translate("MainWindow", "Browse"))
        self.stdbrowse.setText(_translate("MainWindow", "Browse"))
        self.defaultbtn.setText(_translate("MainWindow", "Set as Default"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trial = QtWidgets.QMainWindow()
    MainWindow = QtWidgets.QMainWindow()
    midWindow = QtWidgets.QMainWindow()
    SecondWindow = QtWidgets.QMainWindow()
    ThirdWindow = QtWidgets.QMainWindow()
    ThirdWindow2 = QtWidgets.QMainWindow()
    FinalWindow = QtWidgets.QMainWindow()
    bhat1Window = QtWidgets.QMainWindow()
    bhat2Window = QtWidgets.QMainWindow()
    bhat3Window = QtWidgets.QMainWindow()
    bhat4Window = QtWidgets.QMainWindow()
    
    ui = bhat1()
    ui.setupUi(bhat1Window)
    bhat1Window.show()
    sys.exit(app.exec_())

