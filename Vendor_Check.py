from __future__ import unicode_literals, print_function
import spacy
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
import time

class Vendor_Check(QtCore.QThread):

    #This is the signal that will be emitted during the processing.
    #By including int as an argument, it lets the signal know to expect
    #an integer argument when emitting.
    updateProgress = QtCore.Signal(int)

    # Train the spacy program
    # Getting the pipeline component

    def create_model(self):

        try:
            nlp = spacy.load("ner") # load folder ner trong thư mục chương trình (model)
            return nlp

        except:
            nlp = spacy.load("en_core_web_lg") # Load thư viện gốc
            return nlp
                    

    # initial_data = pd.read_excel(r"C:\Users\ADMIN\Documents\Aufinia\Data_Test.xlsx",sheet_name='Euro', converters={'LFA1_LIFNR':str,'LFA1_STCD1':str},usecols={'LFA1_LIFNR','LFA1_NAME1','COUNTRY','LFA1_STCD1','LFA1_LAND1'})


    def classify_execution(self, df_company):
        
        df_require_col = df_company[['Supplier_number','Supplier_name','Country','Tax_code','Country_code']]
        nlp = self.create_model() # tạo ra một nlp object từ hàm create model

        for idx in range(len(df_require_col)):
            label_EN = ''

            Supplier_name = df_require_col.loc[idx, "Supplier_name"]
    
            doc = nlp(Supplier_name)

            for ent in doc.ents:
                label_EN = label_EN + ent.label_ + '/'
                df_require_col.loc[idx, "Supplier label"] = label_EN
                df_require_col["Supplier label"] = df_require_col["Supplier label"].fillna('Not determined')

            # emit signal to main_GUI
            QApplication.processEvents()
            self.updateProgress.emit(((idx+1)  * 100)/len(df_require_col))
            time.sleep(0.1)

        return df_require_col