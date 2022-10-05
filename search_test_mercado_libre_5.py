from itertools import product
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.by import By

class SearchTestMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.mercadolibre.com.co/")
    
    def test_search_laptop(self):
        driver=self.driver
        search_field= driver.find_element(By.XPATH, '//input[@class="nav-search-input"]')
        search_field.clear()

        search_field.send_keys("laptop")
        search_field.submit()
        products=driver.find_elements(By.XPATH, '//ol[@class="ui-search-layout ui-search-layout--stack"]')
        #self.assertEqual(17, len(products))

    def test_search_salt_shaker(self):
        driver=self.driver
        search_field = driver.find_element(By.XPATH, '//input[@class="nav-search-input"]')
       # driver.find_element(By.LINK_TEXT, "Login")
        self.assertEqual("Mercado Libre", driver.title)
        search_field.clear()
        search_field.send_keys("Salt Shaker")
        search_field.submit()

        products=driver.find_elements(By.XPATH, '//ol[@class="ui-search-layout ui-search-layout--stack"]')
        #self.assertEqual(17, len(products))

    def tearDown(self):
        self.driver.quit()