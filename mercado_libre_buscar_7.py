from multiprocessing.connection import wait
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchMercadoLibreTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(executable_path='C:/Users/User/Desktop/CursosPlatzi/SeleniumPython/chromedriver.exe')
        driver = self.driver
        driver.get("https://www.mercadolibre.com.co/")
        driver.maximize_window()
        driver.implicitly_wait(50)

    def test_select_categories(self):
        driver=self.driver
        options=['Vehículos','Supermercado', 'Tecnología']
        act_options=[]
        driver.find_element(By.XPATH,'//button[@class="cookie-consent-banner-opt-out__action cookie-consent-banner-opt-out__action--primary cookie-consent-banner-opt-out__action--key-accept"]').click()
        select_category=driver.find_element(By.XPATH, '//a[@href="https://www.mercadolibre.com.co/categorias#nav-header"]').is_displayed()
        if(select_category):
            #Permite guardar el pantallazo de la página en ese estado.
            driver.get_screenshot_as_file("screenshot1.png")
        


    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

        
    #Definir los casoss de pruebas
''' def test_search_text_field(self):
        search_field=self.driver.find_element(By.XPATH,'//input[@class="nav-search-input"]')
        search_field.send_keys("nintendo switch")
        search_field.submit()
        btn_new_condition=self.driver.find_element(By.XPATH, '//div[@class="ui-search-filter-dl"]//span[contains(text(), "Nuevo")]')
        btn_new_condition.click()
        self.driver.find_element(By.XPATH,'//button[@class="cookie-consent-banner-opt-out__action cookie-consent-banner-opt-out__action--primary cookie-consent-banner-opt-out__action--key-accept"]').click()
        btn_ubication_bogota=self.driver.find_element(By.XPATH, '//a//span[contains(text(), "Bogot")]')
        btn_ubication_bogota.click()
'''
    #Definir un caso de pruebas para el Select Categorías>Tecnologías> Celulares y Smarthphones
    



