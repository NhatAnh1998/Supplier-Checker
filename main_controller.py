import pandas as pd
import xlwt
from Model_Training import Model_Training
from UI_main import Ui_MainWindow
from UI_train import Ui_TrainWindow
from Web_HitHorizon import  Web_HitHorizon
from Web_GoogleSearch import Web_GoogleSearch
from Web_Sirene import Web_Sirene
from Vendor_Check import Vendor_Check
from PySide6.QtWidgets import QMainWindow , QTableWidgetItem, QFileDialog, QMessageBox
from PySide6 import QtCore


class Controlller(QMainWindow,Ui_MainWindow):

    def __init__(self, parent = None):
        super(Controlller, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)

        # click event
        
        self.pushButton_SelectFile.clicked.connect(self.browse_file)
        # self.pushButton_SelectFile.clicked.connect(self.message_box)

        self.pushButton_Import.clicked.connect(self.import_button_clicked)
        
        self.pushButton_HitHorizon.clicked.connect(self.hithorizon_button_clicked)

        self.pushButton_GoogleSearch.clicked.connect(self.google_button_clicked)

        self.pushButton_Sirene.clicked.connect(self.sirene_button_clicked)

        self.pushButton_VendorCheck.clicked.connect(self.vendorcheck_button_clicked)
        
        self.pushButton_Refresh.clicked.connect(self.refresh_table)
    
        self.pushButton_Export.clicked.connect(self.export_button_clicked)

        self.pushButton_OpenTrainWindow.clicked.connect(self.open_train_window)

  

    def open_train_window (self):
        self.trainwindow = TrainWindow()
        self.trainwindow.show()


    def import_button_clicked (self):

        try:
            self.load_excel_data(self.excel_file_path)

        except AttributeError:
            self.message_box1()

    
    def hithorizon_button_clicked (self):

        try:
            self.run_hithorizon(self.df_company)

        except AttributeError:
            self.message_box2()

    def google_button_clicked (self):

        try:
            self.run_googlesearch(self.df_company)

        except AttributeError:
            self.message_box2()

    def sirene_button_clicked (self):

        try:
            self.run_sirene(self.df_company)

        except AttributeError:
            self.message_box2()

    def vendorcheck_button_clicked (self):

        try:
           self.run_vendorcheck(self.df_company)

        except AttributeError:
            self.message_box2()



    def export_button_clicked (self):
        self.export_file()
        self.message_box3()
    
    # load train data vào trong Model_Training.py và chạy chương trình train model
  

    def load_excel_data (self, excel_file_dir):

        self.df_company = pd.read_excel(excel_file_dir, sheet_name=0, converters={'Supplier_number':str,'Tax_code':str},usecols={'Supplier_number','Supplier_name','Country','Tax_code','Country_code'})
        
        self.tableWidget.setRowCount(self.df_company.shape[0])
        self.tableWidget.setColumnCount(self.df_company.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(self.df_company.columns)

       
        for row in self.df_company.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.3f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)


    def run_hithorizon(self, df_company_input):

    
        self.web_horizon =  Web_HitHorizon()
        self.web_horizon.updateProgress.connect(self.setProgress)
        self.web_horizon.start()

        
        df_hithorizon_output = self.web_horizon.crawling_execution(df_company_input)

    
        self.tableWidget_result.setRowCount(df_hithorizon_output.shape[0])
        self.tableWidget_result.setColumnCount(df_hithorizon_output.shape[1])
        self.tableWidget_result.setHorizontalHeaderLabels(df_hithorizon_output.columns)

        for row in df_hithorizon_output.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.3f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget_result.setItem(row[0], col_index, tableItem)

        self.tableWidget_result.resizeColumnsToContents()
        self.tableWidget_result.resizeRowsToContents()

        self.web_horizon.quit()
        self.web_horizon.wait()


    def run_googlesearch(self, df_company_input):


        self.web_google = Web_GoogleSearch()
        self.web_google.updateProgress.connect(self.setProgress)
        self.web_google.start()

        df_google_output = self.web_google.crawling_execution(df_company_input)


        self.tableWidget_result.setRowCount(df_google_output.shape[0])
        self.tableWidget_result.setColumnCount(df_google_output.shape[1])
        self.tableWidget_result.setHorizontalHeaderLabels(df_google_output.columns)

        for row in df_google_output.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.3f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget_result.setItem(row[0], col_index, tableItem)

        self.tableWidget_result.resizeColumnsToContents()
        self.tableWidget_result.resizeRowsToContents()

        self.web_google.quit()
        self.web_google.wait()


        
    def run_sirene(self, df_company_input):

        self.web_sirene = Web_Sirene()
        self.web_sirene.updateProgress.connect(self.setProgress)
        self.web_sirene.start()

        df_sirene_output = self.web_sirene.crawling_execution(df_company_input)


        self.tableWidget_result.setRowCount(df_sirene_output.shape[0])
        self.tableWidget_result.setColumnCount(df_sirene_output.shape[1])
        self.tableWidget_result.setHorizontalHeaderLabels(df_sirene_output.columns)

        for row in df_sirene_output.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.3f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget_result.setItem(row[0], col_index, tableItem)

        self.tableWidget_result.resizeColumnsToContents()
        self.tableWidget_result.resizeRowsToContents()

        self.web_sirene.quit()
        self.web_sirene.wait()

    def run_vendorcheck(self, df_company_input):

        self.vendor = Vendor_Check()
        self.vendor.updateProgress.connect(self.setProgress)
        self.vendor.start()

        df_vendor_output = self.vendor.classify_execution(df_company_input)

        self.tableWidget_result.setRowCount(df_vendor_output.shape[0])
        self.tableWidget_result.setColumnCount(df_vendor_output.shape[1])
        self.tableWidget_result.setHorizontalHeaderLabels(df_vendor_output.columns)

        for row in df_vendor_output.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.3f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.tableWidget_result.setItem(row[0], col_index, tableItem)

        self.tableWidget_result.resizeColumnsToContents()
        self.tableWidget_result.resizeRowsToContents()

        self.vendor.quit()
        self.vendor.wait()

    def browse_file(self):

        file = str(QFileDialog.getOpenFileName(self, 'Select excel file to import',"","Excel (*.xls *.xlsx)"))
        
        start = "('"
        end = "',"
        self.excel_file_path = file[file.find(start)+len(start):file.rfind(end)]
        
        self.text_file.setText(file)

    

    def export_file(self):

        filename = QFileDialog.getSaveFileName(self, 'Save File', '', "Excel (*.xls)")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("Result", cell_overwrite_ok=True)     
        self.add_data(sheet)
        wbk.save(filename[0])
               
    # hàm add data vào trong workbook để export file
    def add_data (self, sheet):

        model = self.tableWidget_result.model()


        for column in range(model.columnCount()):
            text = model.headerData(column, QtCore.Qt.Horizontal)
            sheet.write(0, column+1, text)

        for row in range(model.rowCount()):
            text = model.headerData(row, QtCore.Qt.Vertical)
            sheet.write(row+1, 0, text)

        for column in range(model.columnCount()):
            for row in range(model.rowCount()):
                text = model.data(model.index(row, column))
                sheet.write(row+1, column+1, text)


    def setProgress(self, progress):

        self.progressBar.setValue(progress)

    def refresh_table(self):

        self.tableWidget_result.clearContents()
        self.progressBar.setValue(0)   

    def message_box1 (self):

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Error")
        dlg.setText("Please select a file first.")
        dlg.setStandardButtons(QMessageBox.StandardButton.Close)
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()

    def message_box2 (self):

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Error")
        dlg.setText("Please import data first.")
        dlg.setStandardButtons(QMessageBox.StandardButton.Close)
        dlg.setIcon(QMessageBox.Icon.Critical)
        dlg.exec()

    def message_box3 (self):

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Message")
        dlg.setText("Your data has been exported successfully.")
        dlg.setStandardButtons(QMessageBox.StandardButton.Close)
        dlg.setIcon(QMessageBox.Icon.NoIcon)
        dlg.exec()


class TrainWindow(QMainWindow, Ui_TrainWindow):
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.ui = Ui_TrainWindow()
        self.setupUi(self)

        self.pushButton_SelectTrainingFile.clicked.connect(self.browse_training_file)
        self.pushButton_TrainModel.clicked.connect(self.train_model_button_clicked)

    def train_model_button_clicked (self):
        try:
            self.run_model_training(self.train_file_path)
            self.message_box4()

        
        except AttributeError:
            self.controller = Controlller()
            self.controller.message_box1()

    def run_model_training (self, train_file_dir): 
        df_train_input = pd.read_excel(train_file_dir, sheet_name=0, converters={'Entity name':str,'Entity label':str},usecols={'Entity name','Trained','Entity label'})

        # tạo 1 instance từ class Model_Training
        self.model_training = Model_Training()

        # hàm chạy progress bar
        self.model_training.updateProgress.connect(self.setProgress)
        self.model_training.start()
        
        df_train_output = self.model_training.train_model(df_train_input)
        df_train_output.to_excel(train_file_dir, index = False)  # lưu lại file train đã đánh dấu X (đã train rồi)

        self.model_training.quit()
        self.model_training.wait()


    def browse_training_file(self):

         file = str(QFileDialog.getOpenFileName(self, 'Select excel file to train',"","Excel (*.xls *.xlsx)"))

         start = "('"
         end = "',"
         self.train_file_path = file[file.find(start)+len(start):file.rfind(end)]
         self.text_filetrain.setText(file)
        
    def message_box4 (self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Message")
        dlg.setText("Your model has been trained.")
        dlg.setStandardButtons(QMessageBox.StandardButton.Close)
        dlg.setIcon(QMessageBox.Icon.NoIcon)
        dlg.exec()

    def setProgress(self, progress):
        self.progressBar.setValue(progress)

    # def message_box(self):
    #     dlg = QMessageBox(self)
    #     dlg.setWindowTitle("Notifcation")
    #     dlg.setText("The data file to be imported must contain the following columns: <b>Supplier_number</b> ; <b>Supplier_name</b> ; <b>Country</b> ; <b>Tax_code</b> ; <b>Country_code</b>. <br><br> Country code must be a two letter ISO code for your country")
    #     dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    #     buttonYes = dlg.button(QMessageBox.Yes)
    #     buttonYes.setText('I understand')
    #     buttonNo = dlg.button(QMessageBox.No)
    #     buttonNo.setText('Cancel')

    #     dlg.setIcon(QMessageBox.Icon.Warning)
    #     button = dlg.exec()

    #     if button == QMessageBox.Yes:
    #         self.browse_file()


        
       
