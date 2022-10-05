from time import sleep
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from mercado_libre_page import MercadoLibrePage

class MercadoLibreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='C:/Users/User/Desktop/CursosPlatzi/SeleniumPython/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(50)

    def test_search(self):
        mercadolibre=MercadoLibrePage(self.driver)
        mercadolibre.open()
        mercadolibre.select_country_colombia()
        mercadolibre.search('Playstation 4')
        mercadolibre.close_cookies()
        mercadolibre.select_filter('Nuevo')
        mercadolibre.select_filter('Bogotá D.C.')
        mercadolibre.select_order_by('Mayor precio')
        title_elements=mercadolibre.first_elements(5)
        first_five_elements_expected=["Sony Playstation 4 Pro 1 Tb Consola Negro Ps4 Pro","Consola Ps4 Slim De 1tb Color Negro","Consola Ps4 Slim De 1tb Color Negro + Spiderman De Sony","Consola Playstation 4 Delgado, De 500 Gb, Color Negro","Consola Ps4 Slim De 1tb"]   
        self.assertEquals(title_elements, first_five_elements_expected)
        sleep(20)        

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    #unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'pom_meli_report'))
    unittest.main(verbosity = 2)

