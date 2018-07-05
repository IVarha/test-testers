import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from pprint import pprint

class BikesPageTests(unittest.TestCase):

	data = []
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/igorvarga/Downloads/chromedriver')

		with open('../bikes.json') as f:
			self.data = json.load(f)

	def test_contains_all_element_sorted(self):
		driver = self.driver
		driver.get("http://localhost:8000")

		self.assertEqual('Bike Store' , driver.title)
		etlems = driver.find_elements_by_class_name('prod')

		self.assertEqual(len(etlems),len(self.data['items']),"did not equal")
		for i in range(len(etlems)):
			head = etlems[i].find_element_by_class_name("panel-heading")
			self.assertEqual(head.text,self.data['items'][i]['name'])

			desc = etlems[i].find_element_by_class_name("desc")
			self.assertEqual(desc.text,self.data['items'][i]['description'])

			classes = etlems[i].find_element_by_class_name("panel-footer").find_elements_by_class_name('capitalise')
			self.assertEqual(head.text,self.data['items'][i]['name'])
			self.assertEqual(len(classes), len(self.data['items'][i]['class']), "did not equal")

			for j in range(len(classes)):
				self.assertTrue(str(self.data['items'][i]['class'][j]).capitalize() in str(classes[j].text))


	def test_contains_all_element_sorted_refresh(self):
		driver = self.driver
		driver.get("http://localhost:8000")

		self.assertEqual('Bike Store' , driver.title)

		elem = driver.find_elements_by_class_name('prod')
		heads = [x.find_element_by_class_name("panel-heading").text for x in elem]
		driver.refresh()
		elem2 = driver.find_elements_by_class_name('prod')
		heads2 = [x.find_element_by_class_name("panel-heading").text for x in elem2]
		self.assertEqual(heads,heads2)


	def test_contains_all_element_sorted_refresh1(self):
		driver = self.driver
		driver.get("http://localhost:8000")




		elem = driver.find_element_by_class_name('col-md-2').find_element_by_class_name('panel-body').find_elements_by_class_name('ng-scope')
		el = []
		for a in elem:
			if (a.text == 'Endurance'):
				el = a

		driver.refresh()








	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()