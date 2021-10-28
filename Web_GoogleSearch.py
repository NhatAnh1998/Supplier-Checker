from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
import time
import os
import sys
import re

class Web_GoogleSearch(QtCore.QThread):

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

        company_name = self.rreplace(company_name, '.', ' ', company_name.count('.')) # replace dot(.) with space in string
        search_result = self.rreplace(search_result, '_', ' ', search_result.count('_')) # replace underscore(_) with space in string

        company_name = company_name.lower().strip()

        # split string into an array
        lis_of_small = re.split('\W+',company_name)

        # khởi tạo mảng để chứa các cụm từ trong company name nếu có trùng với search result 
        list_item_match = []

        for item in lis_of_small:
            if re.search(r"\b{}\b".format(item), search_result.lower().strip()) or re.search(r"\b{}\b".format("".join(lis_of_small)), search_result.lower().strip())  :
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


    # df_company = pd.read_excel(r"C:\Users\ADMIN\Documents\Aufinia\Algieria\Algieria_half1.xlsx", converters={'LFA1_LIFNR':str,'LFA1_STCD1':str},usecols={'LFA1_LIFNR','LFA1_NAME12','COUNTRY','LFA1_STCD1','LFA1_LAND1'})

    # df_company_isnull = df_company.loc[(df_company['LFA1_STCD1'].isnull() == True)]
    # df_company_isnull.reset_index(drop=True, inplace = True) 
    # df_company_isnull.shape


    def crawling_execution(self,df_company):

        df_company_output = df_company[['Supplier_number','Supplier_name','Country','Tax_code','Country_code']]

        df_company_output['Country'] = df_company_output['Country'].str.strip()
        df_company_output['Supplier_name'] = df_company_output['Supplier_name'].str.strip()
        # Create driver
        driver = self.create_driver()

    
        for idx in range(len(df_company_output)):

            try:
                # get company name
                search_name = (df_company_output.loc[idx,'Supplier_name'] + ' ' + df_company_output.loc[idx,'Country'] ).replace(' ','+').replace('&','%26') 
                print(str(idx) + ": " + search_name)  
                driver.get('https://www.google.com/search?q='+search_name)
                driver.implicitly_wait(10)

                # Search
                search_title = driver.find_element(By.XPATH, '(//div[@class="yuRUbf"])[1]/a/h3').text          
                search_url = driver.find_element(By.XPATH, '(//div[@class="yuRUbf"])[1]/a').get_attribute("href")
                search_summary =  driver.find_element_by_xpath('(//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"])[1]/span/em').text
                search_title2 = driver.find_element(By.XPATH, '(//div[@class="yuRUbf"])[2]/a/h3').text            
                search_url2 = driver.find_element(By.XPATH, '(//div[@class="yuRUbf"])[2]/a').get_attribute("href")
                search_summary2 =  driver.find_element_by_xpath('(//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"])[2]/span/em').text



                supplier_name = df_company_output.loc[idx,'Supplier_name']

                similar_check_name1 = self.similar_check(supplier_name,search_title)
                similar_check_name2 = self.similar_check(supplier_name,search_title2)
                similar_check_url1 = self.similar_check(supplier_name,search_url)
                similar_check_url2 = self.similar_check(supplier_name,search_url2)
                similar_check_summary1 = self.similar_check(supplier_name,search_summary)
                similar_check_summary2 = self.similar_check(supplier_name,search_summary2)


                df_company_output.loc[idx,'First google result'] = search_title
                df_company_output.loc[idx,'Second google result'] = search_title2
                df_company_output.loc[idx,'First URL'] = search_url
                df_company_output.loc[idx,'Second URL'] = search_url2


                if similar_check_url1 >= 0.5:
                    df_company_output.loc[idx,'Exists in first URL'] = "Yes"
                else:
                    df_company_output.loc[idx,'Exists in first URL'] = "No"


                if similar_check_name1 >= 0.5:
                    df_company_output.loc[idx,'Exists in first Google result'] = "Yes"
                else:
                    df_company_output.loc[idx,'Exists in first Google result'] = "No"

                if similar_check_summary1 >= 0.5:
                    df_company_output.loc[idx,'Exists in first Google result summary'] = "Yes"
                else:
                    df_company_output.loc[idx,'Exists in first Google result summary'] = "No"

                
                if similar_check_url2 >= 0.5:
                    df_company_output.loc[idx,'Exists in second URL'] = "Yes"
                else:
                    df_company_output.loc[idx,'Exists in second URL'] = "No"

                if similar_check_name2 >= 0.5:
                    df_company_output.loc[idx,'Exists in Second Google result'] = "Yes"
                else:
                    df_company_output.loc[idx,'Exists in Second Google result'] = "No"



                if similar_check_summary2 >= 0.5:
                    df_company_output.loc[idx,'Exists in second Google result summary'] = "Yes"
                else:
                    df_company_output.loc[idx,'Exists in second Google result summary'] = "No"

                

                time.sleep(3)



                # emit signal to main_GUI
                QApplication.processEvents()
                self.updateProgress.emit(((idx+1)  * 100)/len(df_company_output))
                time.sleep(0.1)

                # Get back to previous page
                driver.execute_script("window.history.go(-1)")


            except NoSuchElementException as exception:
                df_company_output.loc[idx,'Exception'] = "No information found"

                # emit signal to main_GUI
                QApplication.processEvents()
                self.updateProgress.emit(((idx+1)  * 100)/len(df_company_output))
                time.sleep(0.1)
                continue


        driver.quit()

        return df_company_output





