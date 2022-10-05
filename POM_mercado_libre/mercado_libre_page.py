from operator import concat
from time import sleep
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MercadoLibrePage(object):
    def __init__(self,driver):
        self._driver = driver
        self._url = 'https://www.mercadolibre.com/'
        self.search_locator = '//input[@class="nav-search-input"]'

    @property #Propiedad para busqueda
    def is_loaded(self):
        WebDriverWait(self._driver , 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="nav-search-input"]')))
        return True
    
    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME,'as_word')
        return input_field.get_attribute('value')
    
    def open(self):
        self._driver.get(self._url)

    def type_search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.send_keys(keyword)
        input_field.send_keys(Keys.ENTER)

    def click_submit(self):
        button_submit = self._driver.find_element(By.XPATH, '//button[@class="nav-search-btn"]')
        button_submit.click()

    def search(self, keyword):
        self.type_search(keyword)
        #self.click_submit
    
    def select_country_colombia(self):
        country_item = self._driver.find_element(By.ID, "CO")
        country_item.click()
    
    def close_cookies(self):
        self._driver.find_element(By.XPATH,'//button[@class="cookie-consent-banner-opt-out__action cookie-consent-banner-opt-out__action--primary cookie-consent-banner-opt-out__action--key-accept"]').click()    

    def select_filter(self, filter_name):                
        txt_locator=concat('//li[@class="ui-search-filter-container shops__container-lists"]/a[@aria-label="',filter_name)     
        filter_item = self._driver.find_element(By.XPATH, concat(txt_locator,'"]'))
        filter_item.click()
    
    def select_order_by(self,option_slc):
        slc_order_by=self._driver.find_element(By.XPATH,'//button[@class="andes-dropdown__trigger"]')
        slc_order_by.click()

        options_order_by=self._driver.find_elements(By.XPATH,'//span[@class="andes-list__item-primary"]')
        for option in options_order_by:
            if str(option.text).lower() == option_slc.lower():
                option.click()   

    def first_elements(self, number):
        number=int(number)
        title_elements=self._driver.find_elements(By.XPATH,'//h2[@class="ui-search-item__title shops__item-title"]')
        titles_five=[]
        for x in range(number):
            titles_five.append(title_elements[x].text)
        return titles_five
'''
 def get_filters(self):
        filters = WebDriverWait(self._driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'ui-search-filter-name')))
        return self.order_data(filters)

    def choise_filter(self, keyword):
        self.get_filters()[keyword.lower()].click()

    def get_orders(self):
        list_buttom = WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'andes-dropdown__trigger')))
        list_buttom.click()
        orders = self._driver.find_elements_by_class_name('andes-list__item-primary')
        return self.order_data(orders)

    def choise_order_by(self, keyword):
        self.get_orders()[keyword.lower()].click()

    def get_top_5_elements_result(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-layout__item')))
        data = [[None, None]] * 5
        for i in range(5):
        data[i][0] = self._driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
        data[i][1] = self._driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
        return data
'''