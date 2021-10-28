from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
import time
import os
import sys
import re

class Web_Sirene(QtCore.QThread):

    #This is the signal that will be emitted during the processing.
    #By including int as an argument, it lets the signal know to expect
    #an integer argument when emitting.
    updateProgress = QtCore.Signal(int)

    # function splits delimiters
    @staticmethod
    def rreplace(s, old, new, occurrence):
        li = s.rsplit(old, occurrence)  
        return new.join(li)

    def similar_check(self,company_name, search_result):

        company_name = self.rreplace(company_name, '.', '', company_name.count('.')) 

        company_name = company_name.lower().strip()

        # split string into an array
        lis_of_small = re.split('\W+',company_name)

        # khởi tạo mảng để chứa các cụm từ trong company name nếu có trùng với search result 
        list_item_match = []

        for item in lis_of_small:
            if re.search(r"\b{}\b".format(item), search_result.lower().strip()):
                list_item_match.append(item)


         # tính tỉ lệ match ratio
        match_ratio = round(len(list_item_match) / len(lis_of_small),2)

        return match_ratio


    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"intl.accept_languages": "en-US"})
        chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
        return webdriver.Chrome(executable_path=self.resource_path('ChromeDriver\chromedriver.exe'), options=chrome_options)
        # return webdriver.Chrome(executable_path=os.path.relpath('ChromeDriver\chromedriver.exe'), options=chrome_options)


    # df_company = pd.read_excel(r"C:\Users\ADMIN\Documents\Aufinia\Data_Test.xlsx",sheet_name='France', converters={'LFA1_LIFNR':str,'LFA1_STCD1':str},usecols={'LFA1_LIFNR','LFA1_NAME1','COUNTRY','LFA1_STCD1','LFA1_LAND1'})

    # df_company_isnull = df_company.loc[(df_company['LFA1_LAND1'] == 'FR') & (df_company['LFA1_STCD1'].isnull() == True)]
    # df_company_isnull.reset_index(drop=True, inplace = True) 
    # df_company_isnull.shape

    def crawling_execution(self, df_company):
        
        
        
        df_company_output = df_company[['Supplier_number','Supplier_name','Country','Tax_code','Country_code']]

        df_company_output['Country_code'] = df_company_output['Country_code'].str.lower()
        df_company_output = df_company_output.loc[(df_company_output['Country_code'] == 'fr')]
        df_company_output.reset_index(drop=True, inplace=True)

        driver = self.create_driver()
        driver.get('https://www.sirene.fr/sirene/public/recherche')
        driver.implicitly_wait(5)


        try:
            for idx in range(len(df_company_output)):

                time.sleep(3)
                tax_number = df_company_output.loc[idx,'Tax_code']
                company_name = df_company_output.loc[idx,'Supplier_name']

                search_result = {}

                if(tax_number):
                    print(tax_number)
                    try:
                        exclude_close_checkBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "excludeClosedCheckbox")))
                        if exclude_close_checkBox.is_selected():
                            exclude_close_checkBox.click()
                        
                        tax_number_input = driver.find_element(By.ID, "sirenSiretQuery")
                        tax_number_input.click()
                        tax_number_input.clear()
                        tax_number_input.send_keys(tax_number)

                    
                        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-search")))
                        driver.execute_script("arguments[0].click();", search_button)

                        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//div[@id='collapse-0']"))
                                )

                        search_result = {};

                        # Company_name
                        
                        search_result['company_name'] = driver.find_element(By.XPATH, "(//a[@class='accordion-toggle'])[1]/span[1]").text.strip()
                        print(search_result['company_name'])
                        # Entreprise status        
                        Ent_status_parent = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[1]")
                        Ent_status_child = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[1]/label")
                        
                        search_result['ENT-Status'] = Ent_status_parent.text.replace(Ent_status_child.text, '').strip()

                        # Legal category
                        ENT_leagal_cat_parent = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[2]")
                        ENT_legal_cat_child = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[2]/label")        
                        
                        search_result['Legal-CAT'] = ENT_leagal_cat_parent.text.replace(ENT_legal_cat_child.text, '').strip()

                        # Tax Code
                        # tax code gồm cả label đằng trước và tax
                        tax_code_parent = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[6]")
                        # tax code chỉ có label
                        tax_code_child = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[6]/label")

                        search_result['Tax_code'] = tax_code_parent.text.replace(tax_code_child.text, '').strip()


                        

                        # emit signal to main_GUI
                        QApplication.processEvents()
                        self.updateProgress.emit(((idx+1)  * 100)/len(df_company_output))
                        time.sleep(0.1)

                    except Exception:
                        search_result['company_name'] = "Nothing found"
                        search_result['ENT-Status'] = "Nothing found"
                        search_result['Legal-CAT'] = "Nothing found"
                        driver.get('https://www.sirene.fr/sirene/public/recherche')

                        # emit signal to main_GUI
                        QApplication.processEvents()
                        self.updateProgress.emit(((idx+1)  * 100)/len(df_company_output))
                        time.sleep(0.1)

                        continue
                    
                else:
                    try:
                        exclude_close_checkBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "excludeClosedCheckbox")))
                        if exclude_close_checkBox.is_selected():
                            exclude_close_checkBox.click()
                        
                        company_name_input = driver.find_element(By.ID, "rsQuery")
                        company_name_input.click()
                        company_name_input.clear()
                        company_name_input.send_keys(company_name)

                        driver.implicitly_wait(10)

                        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-search")))
                        driver.execute_script("arguments[0].click();", search_button)

                        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.XPATH, "//div[@id='collapse-0']"))
                                )

                        search_result = {};

                        # Company_name
                        
                        search_result['company_name'] = driver.find_element(By.XPATH, "(//a[@class='accordion-toggle'])[1]/span[1]").text.strip()
                        # Entreprise status        
                        Ent_status_parent = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[1]")
                        Ent_status_child = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[1]/label")
                        
                        search_result['ENT-Status'] = Ent_status_parent.text.replace(Ent_status_child.text, '').strip()

                        # Legal category
                        ENT_leagal_cat_parent = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[2]")
                        ENT_legal_cat_child = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[2]/label")        
                        
                        search_result['Legal-CAT'] = ENT_leagal_cat_parent.text.replace(ENT_legal_cat_child.text, '').strip()

                        # Tax Code
                        # tax code gồm cả label đằng trước và tax
                        tax_code_parent = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[6]")
                        # tax code chỉ có label
                        tax_code_child = driver.find_element(By.XPATH, "(//div[@id='collapse-0'])[1]/div/div[2]/p[6]/label")

                        search_result['Tax_code'] = tax_code_parent.text.replace(tax_code_child.text, '').strip()

                        

                        # emit signal to main_GUI
                        QApplication.processEvents()
                        self.updateProgress.emit(((idx+1)  * 100)/len(df_company_output))
                        time.sleep(0.1)

                    except Exception:
                        search_result['company_name'] = "Nothing found"
                        search_result['ENT-Status'] = "Nothing found"
                        search_result['Legal-CAT'] = "Nothing found"
                        driver.get('https://www.sirene.fr/sirene/public/recherche')


                        # emit signal to main_GUI
                        QApplication.processEvents()
                        self.updateProgress.emit(((idx+1)  * 100)/len(df_company_output))
                        time.sleep(0.1)
                        
                        continue

                
                df_company_output.loc[idx,'Name found in Sirene.FR'] = search_result['company_name'] 
                df_company_output.loc[idx,'Entity status found in SIRENE.FR'] = search_result['ENT-Status']
                df_company_output.loc[idx,'Legal category found in SIRENE.FR'] = search_result['Legal-CAT'] 
                df_company_output.loc[idx,'Tax_code found in SIRENE.FR'] = search_result['Tax_code'] 

                # Check whether or not this name search is similar to Supplier Name
                if(search_result['company_name'] != "Nothing found"):
                    similar_check_name = self.similar_check(company_name,search_result['company_name']) 

                    if similar_check_name >= 0.5:
                        df_company_output.loc[idx,'Name found in SIRENE.FR matches Supplier_name'] = "Yes"
                    else:
                        df_company_output.loc[idx,'Name found in SIRENE.FR matches Supplier_name'] = "No"
                else:
                    df_company_output.loc[idx,'Exists in name search'] = "Not Found"
            
            driver.close()

            df_company_output['Country_code'] = df_company_output['Country_code'].replace(['fr'],'FR')
            df_company_output = df_company_output.fillna('None')
            return df_company_output

        except WebDriverException:
            
            df_company_output['Country_code'] = df_company_output['Country_code'].replace(['fr'],'FR')
            df_company_output = df_company_output.fillna('None')
            return df_company_output
