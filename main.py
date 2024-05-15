# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QTableWidgetItem,QVBoxLayout,QHBoxLayout
import sys
from PyQt5.QtCore import QCoreApplication

import librosa
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QComboBox, QTableWidget, QTableWidgetItem, QLabel, QGraphicsView, QTableWidgetItem
import functions as func
import joblib
from PyQt5.QtGui import QIcon, QPainter
from PyQt5 import QtCore
import random
from PyQt5.QtWidgets import QTableWidgetItem,QVBoxLayout,QHBoxLayout, QApplication, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from functions import *
import wave
from pyqtgraph import PlotWidget
from PyQt5.QtGui import QPixmap, QImage  # Correct import statement
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice  # Import QByteArray and related classes
import functions
import pyqtgraph as pg

from matplotlib.figure import Figure
# from librosa import power_to_db , util
import matplotlib.pyplot as plt
# import librosa.display
import pyaudio
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1321, 783)
        MainWindow.setStyleSheet("background-color: #1b1d23;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #1b1d23;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFixedSize(800,400)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.line_11 = QtWidgets.QFrame(self.frame_3)
        self.line_11.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_9.addWidget(self.line_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")


        self.spectrogram = QtWidgets.QLabel(self.frame_3)
        self.spectrogram.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.spectrogram.setObjectName("spectrogram")



        self.verticalLayout_10.addWidget(self.spectrogram)
        self.verticalLayout_10.setStretch(0, 5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)



        self.verticalLayout_8.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.line_14 = QtWidgets.QFrame(self.frame_4)
        self.line_14.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_12.addWidget(self.line_14)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.person_1 = QtWidgets.QLabel(self.frame_4)
        self.person_1.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_1.setObjectName("person_1")
        self.verticalLayout_13.addWidget(self.person_1)
        self.person_2 = QtWidgets.QLabel(self.frame_4)
        self.person_2.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_2.setObjectName("person_2")
        self.verticalLayout_13.addWidget(self.person_2)
        self.person_3 = QtWidgets.QLabel(self.frame_4)
        self.person_3.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_3.setObjectName("person_3")
        self.verticalLayout_13.addWidget(self.person_3)
        self.person_4 = QtWidgets.QLabel(self.frame_4)
        self.person_4.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_4.setObjectName("person_4")
        self.verticalLayout_13.addWidget(self.person_4)
        self.person_5 = QtWidgets.QLabel(self.frame_4)
        self.person_5.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_5.setObjectName("person_5")
        self.verticalLayout_13.addWidget(self.person_5)
        self.person_6 = QtWidgets.QLabel(self.frame_4)
        self.person_6.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_6.setObjectName("person_6")
        self.verticalLayout_13.addWidget(self.person_6)
        self.person_7 = QtWidgets.QLabel(self.frame_4)
        self.person_7.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_7.setObjectName("person_7")
        self.verticalLayout_13.addWidget(self.person_7)
        self.person_8 = QtWidgets.QLabel(self.frame_4)
        self.person_8.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.person_8.setObjectName("person_8")
        self.verticalLayout_13.addWidget(self.person_8)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_1.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_14.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_2.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_14.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_3.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_14.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_4.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_14.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_5.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_14.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_6.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_14.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_7.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_14.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_8.setStyleSheet(" font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */")
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_14.addWidget(self.checkBox_8)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(39, 44, 54);\n"
"border: none;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_3.addWidget(self.line_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.table = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.table.setColumnCount(2)
        # Example data
        data = [
                ["Item1", "Value1"],
                ["Item2", "Value2"],
                ["Item3", "Value3"]

        ]

        # Set the number of rows
        self.table.setRowCount(len(data))

        # Populate the table with data
        for i, (item, value) in enumerate(data):
                self.table.setItem(i, 0, QTableWidgetItem(item))
                self.table.setItem(i, 1, QTableWidgetItem(value))

        font.setFamily("Robota")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.table.setFont(font)
        self.table.setStyleSheet("color: white;")



        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")


        self.status = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setObjectName("status")
        self.status.setColumnCount(0)
        self.status.setRowCount(0)
        self.verticalLayout_15.addWidget(self.status)
        self.horizontalLayout_2.addLayout(self.verticalLayout_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.status.setColumnCount(2)
        # Example data
        data = [
                ["Speaker", "Value1"],
                ["Speech", "Value2"],
                ["Access", "Value3"]

        ]

        # Set the number of rows
        self.status.setRowCount(len(data))

        # Populate the table with data
        for i, (item, value) in enumerate(data):
                self.status.setItem(i, 0, QTableWidgetItem(item))
                self.status.setItem(i, 1, QTableWidgetItem(value))

        font.setFamily("Robota")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("color: white;")

        header = self.table.horizontalHeader()
        header.setDefaultSectionSize(100)  # Adjust the cell width as needed
        self.table.verticalHeader().setDefaultSectionSize(70)  # Adjust the cell height as needed

        header = self.status.horizontalHeader()
        header.setDefaultSectionSize(100)  # Adjust the cell width as needed
        self.status.verticalHeader().setDefaultSectionSize(70)  # Adjust the cell height as needed

        # Populate the table with sample data
        # for i in range(3):
        #         for j in range(2):
        #                 item = QTableWidgetItem(f'Item {i}-{j}')
        #                 self.table.setItem(i, j, item)


        self.horizontalLayout_9=QHBoxLayout()
        
        self.record_button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.record_button.sizePolicy().hasHeightForWidth())
        self.record_button.setSizePolicy(sizePolicy)
        self.record_button.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;\n"
"background-color: #003366; \n"
"border: none;\n"
"color: #FFFFFF; \n"
"width:80px; \n"
"height: 30px; \n"
"border-radius: 10px;")
        self.record_button.setObjectName("record_button")
        self.horizontalLayout_9.addWidget(self.record_button)

        self.mode = QtWidgets.QComboBox(self.frame)
        self.mode.setStyleSheet("QComboBox {\n"
                                        "    font-family: \"Overpass\";\n"
                                        "    font-weight: 600; /* Semibold */\n"
                                        "    font-size: 10pt; /* Adjust the font size as needed */\n"
                                        "    color: white; /* Set the text color to white */\n"
                                        "    border: 1px solid white; /* Set the border to 1px solid white */\n"
                                        "background: rgba(74, 74, 74, 0);\n"
                                        "    border-radius: 5px;\n"
                                        "}")
        self.mode.setObjectName("mode")
        self.mode.addItem("mode1")
        self.mode.addItem("mode2")

        self.horizontalLayout_9.addWidget(self.mode)

        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        # self.gridLayout.addWidget(self.record_button, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line_12 = QtWidgets.QFrame(self.frame_2)
        self.line_12.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_4.addWidget(self.line_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.table2 = QtWidgets.QTableWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table2.sizePolicy().hasHeightForWidth())
        self.table2.setSizePolicy(sizePolicy)
        self.table2.setObjectName("tableWidget")
        self.table2.setColumnCount(0)
        self.table2.setRowCount(0)
        self.verticalLayout_5.addWidget(self.table2)

        self.table2.setColumnCount(2)


        # Example data
        data = [
            ["Item1", "Value1"],
            ["Item2", "Value2"],
            ["Item3", "Value3"],
            ["Item4", "Value4"],
            ["Item5", "Value5"],
            ["Item6", "Value6"],
            ["Item7", "Value7"],

        ]

        # Set the number of rows
        self.table2.setRowCount(len(data))

        # Populate the table with data
        for i, (item, value) in enumerate(data):
            self.table2.setItem(i, 0, QTableWidgetItem(item))
            self.table2.setItem(i, 1, QTableWidgetItem(value))

        font.setFamily("Robota")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.table2.setFont(font)
        self.table2.setStyleSheet("color: white;")

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.message=QMessageBox()

        self.state=''
        self.record_button.setText('Start Recording')
        self.record_button.clicked.connect(self.record_audio_test)
        self.allowed=[self.checkBox_1,self.checkBox_2,self.checkBox_3,self.checkBox_4,
                      self.checkBox_5,self.checkBox_6,self.checkBox_7,self.checkBox_8]
        for i in range (3):
                self.allowed[i].setChecked(True)


    def record_audio_test(self):
                FORMAT = pyaudio.paInt16
                CHANNELS = 1
                RATE = 44100
                CHUNK = 512
                RECORD_SECONDS = 2.5

                self.update_button(True)
                QCoreApplication.processEvents()
                audio = pyaudio.PyAudio()
                stream = audio.open(format=FORMAT, channels=CHANNELS,
                                    rate=RATE, input=True, input_device_index=1,
                                    frames_per_buffer=CHUNK)
                Recordframes = []
                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                        data = stream.read(CHUNK)
                        Recordframes.append(data)
                stream.stop_stream()
                stream.close()
                audio.terminate()

                OUTPUT_FILENAME = "output.wav"
                waveFile = wave.open(OUTPUT_FILENAME, 'wb')
                waveFile.setnchannels(CHANNELS)
                waveFile.setsampwidth(audio.get_sample_size(FORMAT))
                waveFile.setframerate(RATE)
                waveFile.writeframes(b''.join(Recordframes))
                waveFile.close()
                self.update_button(False)
                QCoreApplication.processEvents()
                self.test_model()

    def update_button(self,flag):

            style_template = ("color:white;\n"
                              "font-size:20px;\n"
                              "margin: 0 0 ;\n"
                              "background-color: {};\n"
                              "border: none;\n"
                              "color: #FFFFFF;\n"
                              "width:80px;\n"
                              "height: 30px;\n"
                              "border-radius: 10px;")

            if flag:
                    self.record_button.setStyleSheet(style_template.format("green"))
            else:
                    self.record_button.setStyleSheet(style_template.format("#003366"))

    def test_model(self):
                self.table.clearContents()
                audio, sr_freq = lr.load("output.wav")
                Draw_spectrogram(audio, sr_freq)

                # load the model of the persons
                gmm_files = [i + '.joblib' for i in ['fatim','mai', 'nora', 'sondos','manar','hesham','omar']]
                models = [joblib.load(fname) for fname in gmm_files]
                x = func.extract_features(audio, sr_freq)

                # load the model of the words
                gmm_files_word = [i + '.joblib' for i in
                                  ['grantmeaccess','openmiddledoor', 'unlockthegate']]
                models_word = [joblib.load(fname) for fname in gmm_files_word]
                x_word = func.extract_features(audio, sr_freq)

                # loop on the models of the persons to get the max score of the person to detect who
                log_likelihood = np.zeros(len(models))
                for j in range(len(models)):
                        gmm = models[j]
                        scores = np.array(gmm.score(x))
                        log_likelihood[j] = scores.sum()

                winner = np.argmax(log_likelihood)

                flag = False
                flagLst = log_likelihood - max(log_likelihood)
                for i in range(len(flagLst)):
                        if flagLst[i] == 0:
                                continue
                        if abs(flagLst[i]) < 0.2:
                                flag = True

                if flag:
                        winner = 7


                if winner ==0:
                        speaker = "Fatim"
                elif winner == 1:
                        speaker = "Mai"
                elif winner == 2:
                        speaker = "Noura"
                elif winner == 3:
                        speaker = "Sondos"
                elif winner == 4:
                        speaker = " Manar"

                elif winner == 5:
                        speaker = " Hesham"
                elif winner == 6:
                        speaker = " Omar"

                elif winner == 7:
                        speaker = " Unknown"
                ###########################################################################################

                log_likelihood_word = np.zeros(len(models_word))
                for j in range(len(models_word)):
                        gmm = models_word[j]
                        scores = np.array(gmm.score(x_word))
                        log_likelihood_word[j] = scores.sum()



                winner_word = np.argmax(log_likelihood_word)
                flagword = False
                wordflagLst = log_likelihood_word - max(log_likelihood_word)
                for i in range(len(wordflagLst)):
                        if wordflagLst[i] == 0:
                                continue
                        if abs(wordflagLst[i]) < 0.5:
                                flagword = True

                if flagword:
                        winner_word = 3

                if winner_word ==0:
                        word_rec='grantmeaccess'
                if winner_word ==1:
                        word_rec='openmiddledoor'
                if winner_word == 2:
                        word_rec = 'unlockthegate'
                if winner_word == 3:
                        word_rec = 'Wrong Password'
                #

                if self.mode.currentText()=="mode1":
                        if winner_word != 3:
                                self.state="Allowed to enter"

                        else:
                                self.state="Not Allowed to enter"

                else:

                        if self.allowed[winner].checkState() == 2 and winner_word != 3 and winner !=7:
                                self.state="Allowed to enter"

                        else:
                                self.state="Not Allowed to enter"



                self.status.setItem(0, 1, QTableWidgetItem(str(speaker)))
                self.status.setItem(1, 1, QTableWidgetItem(str(word_rec)))
                self.status.setItem(2, 1, QTableWidgetItem(self.state))

                speaker = [i  for i in ['fatim','mai', 'nora', 'sondos','manar','hesham','omar']]

                speech = [i  for i in['grant me access', 'open middle door', 'unlock the gate']]
                #
                # for i in range(len(speech)):
                #         self.table.setItem(i, 0, QTableWidgetItem(str(speech[i])))
                #         self.table.setItem(i, 1, QTableWidgetItem(str(np.round(100 - np.abs(log_likelihood_word[i]), 1)) + "%"))
                # for i in range(len(speaker)):
                #         self.table2.setItem(i, 0, QTableWidgetItem(str(speaker[i])))
                #         self.table2.setItem(i, 1, QTableWidgetItem(str(np.round(100 - np.abs(log_likelihood[i]), 1)) + "%"))
                #


                for i in range(len(speech)):
                        self.table.setItem(i, 0, QTableWidgetItem(str(speech[i])))
                        # print((2**(np.abs(log_likelihood_word[i]))/2**(np.abs(max(log_likelihood))))*100)

                        print((2**(100 - np.abs(log_likelihood_word[i]))/2**(100 - np.abs(max(log_likelihood_word))))*100)
                        self.table.setItem(i, 1, QTableWidgetItem(str((2**(100 - np.abs(log_likelihood_word[i]))/2**(100 - np.abs(max(log_likelihood_word))))*100)))
                for i in range(len(speaker)):
                        self.table2.setItem(i, 0, QTableWidgetItem(str(speaker[i])))
                        self.table2.setItem(i, 1, QTableWidgetItem(str((2**(100 - np.abs(log_likelihood[i]))/2**(100 - np.abs(max(log_likelihood))))*100)))




                pixmap = QPixmap('Spectrogram.png')
                self.spectrogram.setPixmap(pixmap)
                # Resize the QLabel to fit the image
                self.spectrogram.setScaledContents(True)


                print(speaker,word_rec)
                print(log_likelihood)
                print(log_likelihood_word)



    def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_7.setText(_translate("MainWindow", "Spectrogram"))
                self.label_10.setText(_translate("MainWindow", "Allowed"))
                self.person_1.setText(_translate("MainWindow", "Fatma"))
                self.person_2.setText(_translate("MainWindow", "Mai"))
                self.person_3.setText(_translate("MainWindow", "Noura"))
                self.person_4.setText(_translate("MainWindow", "Sondos"))
                self.person_5.setText(_translate("MainWindow", "Manar"))
                self.person_6.setText(_translate("MainWindow", "Hesham"))
                self.person_7.setText(_translate("MainWindow", "Omar"))
                # self.person_8.setText(_translate("MainWindow", "Omar"))
                self.checkBox_1.setText(_translate("MainWindow", "1"))
                self.checkBox_2.setText(_translate("MainWindow", "2"))
                self.checkBox_3.setText(_translate("MainWindow", "3"))
                self.checkBox_4.setText(_translate("MainWindow", "4"))
                self.checkBox_5.setText(_translate("MainWindow", "5"))
                self.checkBox_6.setText(_translate("MainWindow", "6"))
                self.checkBox_7.setText(_translate("MainWindow", "7"))
                self.checkBox_8.setText(_translate("MainWindow", "8"))
                self.label.setText(_translate("MainWindow", "Speech table                      Status table"))
                # self.record_button.setText(_translate("MainWindow", "Start Recording"))
                self.label_4.setText(_translate("MainWindow", "Speaker table"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())