# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WebTool_GUI.ui'
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
        background-color: lightblue;
        width: 10px;
        margin: 1px;
    }
    """

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 898)
        icon = QIcon()
        icon.addFile(u":/images/sc_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 431, 411))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 130, 91, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.text_file = QTextEdit(self.groupBox)
        self.text_file.setObjectName(u"text_file")
        self.text_file.setGeometry(QRect(20, 160, 381, 31))
        self.pushButton_SelectFile = QPushButton(self.groupBox)
        self.pushButton_SelectFile.setObjectName(u"pushButton_SelectFile")
        self.pushButton_SelectFile.setGeometry(QRect(60, 200, 141, 31))
        self.pushButton_Import = QPushButton(self.groupBox)
        self.pushButton_Import.setObjectName(u"pushButton_Import")
        self.pushButton_Import.setGeometry(QRect(230, 200, 131, 31))
        self.pushButton_Export = QPushButton(self.groupBox)
        self.pushButton_Export.setObjectName(u"pushButton_Export")
        self.pushButton_Export.setGeometry(QRect(60, 240, 301, 31))
        self.pushButton_Export.setCheckable(False)
        self.pushButton_Export.setFlat(False)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 340, 501, 81))
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(-2)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 401, 101))
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(-2)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 280, 101, 16))
        self.label_4.setFont(font)
        self.pushButton_OpenTrainWindow = QPushButton(self.groupBox)
        self.pushButton_OpenTrainWindow.setObjectName(u"pushButton_OpenTrainWindow")
        self.pushButton_OpenTrainWindow.setGeometry(QRect(60, 310, 301, 31))
        self.pushButton_OpenTrainWindow.setCheckable(False)
        self.pushButton_OpenTrainWindow.setFlat(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(430, 0, 631, 411))
        self.tableWidget = QTableWidget(self.groupBox_2)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 20, 611, 381))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 420, 1061, 71))
        self.pushButton_HitHorizon = QPushButton(self.groupBox_3)
        self.pushButton_HitHorizon.setObjectName(u"pushButton_HitHorizon")
        self.pushButton_HitHorizon.setGeometry(QRect(10, 20, 101, 41))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_HitHorizon.setFont(font1)
        self.pushButton_GoogleSearch = QPushButton(self.groupBox_3)
        self.pushButton_GoogleSearch.setObjectName(u"pushButton_GoogleSearch")
        self.pushButton_GoogleSearch.setGeometry(QRect(120, 20, 111, 41))
        self.pushButton_GoogleSearch.setFont(font1)

        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(710, 30, 341, 21))
        self.progressBar.setStyleSheet(ProgressBar_Style)
        self.progressBar.setValue(0)

        self.pushButton_VendorCheck = QPushButton(self.groupBox_3)
        self.pushButton_VendorCheck.setObjectName(u"pushButton_VendorCheck")
        self.pushButton_VendorCheck.setGeometry(QRect(360, 20, 161, 41))
        self.pushButton_VendorCheck.setFont(font1)
        self.pushButton_Refresh = QPushButton(self.groupBox_3)
        self.pushButton_Refresh.setObjectName(u"pushButton_Refresh")
        self.pushButton_Refresh.setGeometry(QRect(610, 20, 81, 41))
        self.pushButton_Sirene = QPushButton(self.groupBox_3)
        self.pushButton_Sirene.setObjectName(u"pushButton_Sirene")
        self.pushButton_Sirene.setGeometry(QRect(240, 20, 111, 41))
        self.pushButton_Sirene.setFont(font1)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 500, 1061, 371))
        self.tableWidget_result = QTableWidget(self.groupBox_4)
        if (self.tableWidget_result.columnCount() < 10):
            self.tableWidget_result.setColumnCount(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_result.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(9, __qtablewidgetitem14)
        self.tableWidget_result.setObjectName(u"tableWidget_result")
        self.tableWidget_result.setGeometry(QRect(10, 20, 1041, 341))
        self.tableWidget_result.horizontalHeader().setDefaultSectionSize(102)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1071, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("Supplier Checker", u"Supplier Checker", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Import and Export Files", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.pushButton_SelectFile.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.pushButton_Import.setText(QCoreApplication.translate("MainWindow", u"Import ", None))
        self.pushButton_Export.setText(QCoreApplication.translate("MainWindow", u"Export File", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Requires Google Chrome version: 93.0.4577.63 or later.</span></p><p><span style=\" font-size:10pt;\">For HitHorizons, upgrade to test more than 100 records per hour.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">The data file to be imported must contain the following columns: </span></p><p><span style=\" font-weight:700;\">Supplier_number ; Supplier_name ; Country ; Tax_code ; Country_code.</span></p><p><span style=\" font-size:10pt;\">The country code must be the two letter ISO code.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Training Model", None))
        self.pushButton_OpenTrainWindow.setText(QCoreApplication.translate("MainWindow", u"Train Model", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Data Input", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Supplier_number", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Supplier_name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tax_code", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Country_code", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Execution and Progress", None))
        self.pushButton_HitHorizon.setText(QCoreApplication.translate("MainWindow", u"HitHorizons", None))
        self.pushButton_GoogleSearch.setText(QCoreApplication.translate("MainWindow", u"Google ", None))
        self.pushButton_VendorCheck.setText(QCoreApplication.translate("MainWindow", u"Vendor Is A Person", None))
        self.pushButton_Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_Sirene.setText(QCoreApplication.translate("MainWindow", u"Sirene ", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Result", None))
        ___qtablewidgetitem5 = self.tableWidget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Supplier_number", None));
        ___qtablewidgetitem6 = self.tableWidget_result.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Supplier_name", None));
        ___qtablewidgetitem7 = self.tableWidget_result.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Country", None));
        ___qtablewidgetitem8 = self.tableWidget_result.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Tax_code", None));
        ___qtablewidgetitem9 = self.tableWidget_result.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Country_code", None));
        ___qtablewidgetitem10 = self.tableWidget_result.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Name_Search", None));
        ___qtablewidgetitem11 = self.tableWidget_result.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Address_Search", None));
        ___qtablewidgetitem12 = self.tableWidget_result.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Tax_Code_Search", None));
        ___qtablewidgetitem13 = self.tableWidget_result.horizontalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Industry", None));
        ___qtablewidgetitem14 = self.tableWidget_result.horizontalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"URLs", None));
    # retranslateUi


