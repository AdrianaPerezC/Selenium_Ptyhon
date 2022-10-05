import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(50)
        
    #Definir los casoss de pruebas
    def test_search_text_field(self):
        search_field=self.driver.find_element(By.ID,"search")

    def test_search_text_field_by_name(self):
        search_field=self.driver.find_element(By.NAME, "q")
    

    def text_search_text_field_class_name(self):
        search_field=self.driver.find_element(By.CLASS_NAME,"input-text")

    def test_search_button_enabled(self):
        button=self.driver.find_element(By.CLASS_NAME,"button")

    #Contar cuantas imágenes hasy de promoción en el banner

    def test_count_of_promo_banner_images(self):
        banner_list=self.driver.find_element(By.CLASS_NAME, "promos")
        banners=banner_list.find_elements(By.TAG_NAME, "img")
        self.assertEqual(3,len(banners))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

