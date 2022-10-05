import unittest, csv
from ddt import ddt,data, unpack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner


def get_data(file_name):
    rows=[]
    #va a abrir el archivo en mode lectura r
    data_file=open(file_name,'r')
    reader=csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='C:/Users/User/Desktop/CursosPlatzi/SeleniumPython/chromedriver.exe')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(*get_data('C:/Users/User/Desktop/CursosPlatzi/SeleniumPython/DDT_PYTHON/testdata.csv'))
    @unpack
    def test_search_ddt(self,search_value,expected_count):
        driver=self.driver
        search_field=driver.find_element(By.NAME,'q')
        search_field.clear
        search_field.send_keys(search_value)
        search_field.send_keys(Keys.ENTER)
        products=driver.find_elements(By.XPATH,'//h2[@class="product-name"]/a')
        expected_count= int(expected_count)

        if expected_count>0:
            self.assertEqual(expected_count, len(products))
        else:
            message=driver.find_element(By.NAME,'note-msg')
            self.assertEqual('Your Search returns no results.',message)
        print(f'Found {len(products)} products')
        for product in products:
            print(product.text)
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'dtt_report'))


