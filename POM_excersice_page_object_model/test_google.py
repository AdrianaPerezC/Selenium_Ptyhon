import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from google_page import GooglePage

class GooogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='C:/Users/User/Desktop/CursosPlatzi/SeleniumPython/chromedriver.exe')

    def test_search(self):
        google=GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'pom_report'))
#unittest.main(verbosity = 2)

