from unittest import TestLoader, TestSuite
#from pyunitreport import HTMLTestRunner
from assertion_4 import AssertionsTest
from HtmlTestRunner import HTMLTestRunner
from search_test_mercado_libre_5 import SearchTestMercadoLibre

assertions_test=TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test=TestLoader().loadTestsFromTestCase(SearchTestMercadoLibre)

#Creación de suit de pruebas
smoke_test=TestSuite([assertions_test,search_test])

#para generar los reporters
kwargs={
    "output": "smoke_report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": True
}

#la variable runner almacena un reporte generado por HTMLTestRuner
#usa como argumento "kwarsp"
runner = HTMLTestRunner(**kwargs)
#runner = HTMLTestRunner(combine_reports=True,report_name="Reporte-combinado")

#corro el rurner con la suite de prueba
runner.run(smoke_test) 
#En Python, podemos pasar un número variable de argumentos a una función utilizando símbolos especiales. Hay dos símbolos especiales:
#*args (Argumentos sin keyword)
#**kwargs (Argumentos de keyword)
#Usamos *args y **kwargs cuando no estamos seguros del número de argumentos a pasar en las funciones.
