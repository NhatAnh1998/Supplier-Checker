# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Train_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resource_icons


ProgressBar_Style = """
    QProgressBar{
        border: 1px solid grey;
        border-radius: 5px;
        text-align: center;
    }

    QProgressBar::chunk {
        background-color: #98e698;
        width: 10px;
        margin: 1px;
    }
    """

class Ui_TrainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(446, 216)
        icon = QIcon()
        icon.addFile(u":/images/sc_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_filetrain = QTextEdit(self.centralwidget)
        self.text_filetrain.setObjectName(u"text_filetrain")
        self.text_filetrain.setGeometry(QRect(30, 20, 381, 31))
        self.pushButton_SelectTrainingFile = QPushButton(self.centralwidget)
        self.pushButton_SelectTrainingFile.setObjectName(u"pushButton_SelectTrainingFile")
        self.pushButton_SelectTrainingFile.setGeometry(QRect(50, 70, 151, 41))
        self.pushButton_TrainModel = QPushButton(self.centralwidget)
        self.pushButton_TrainModel.setObjectName(u"pushButton_TrainModel")
        self.pushButton_TrainModel.setGeometry(QRect(240, 70, 151, 41))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.pushButton_TrainModel.setFont(font)
        self.pushButton_TrainModel.setAutoRepeatDelay(299)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 140, 301, 16))
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setStyleSheet(ProgressBar_Style)
        self.progressBar.setValue(0)

        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 446, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Training Model", None))
        self.pushButton_SelectTrainingFile.setText(QCoreApplication.translate("MainWindow", u"Choose Training File", None))
        self.pushButton_TrainModel.setText(QCoreApplication.translate("MainWindow", u"Train", None))
    # retranslateUi

