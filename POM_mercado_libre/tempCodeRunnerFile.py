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
        title_elements=mercadolibre.first_elements()
        print('---------------------',title_elements[0].text)
        self.assertEquals(title_elements[0].text,"Sony Playstation 4 Pro 1 Tb Consola Negro Ps4 Pro")
        self.assertEquals(title_elements[1].text,"Sony PlayStation 4 Slim 1TB Standard color negro azabache")
        self.assertEquals(title_elements[2].text,"Sony PlayStation 4 Slim 500GB Standard color negro azabache")
        self.assertEquals(title_elements[3].text,"Kit Mantenimiento Ps4 Artic Mx-4 + Destornillador Torx T8")
        self.assertEquals(title_elements[4].text,"Sony Playstation 4 Slim 1tb Standard Negro Open Box Nueva")   
        sleep(20)        

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'pom_meli_report'))
#unittest.main(verbosity = 2)

