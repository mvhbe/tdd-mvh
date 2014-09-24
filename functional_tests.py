from selenium import webdriver
import unittest

class BezoekerTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def testWebsiteVisclub(self):
		# Joske heeft gehoord over de nieuwe site van de visclub.
		# Hij opent de browser en gaat naar de de site.
		self.browser.get("http://localhost:8001")

		# De naam van de visclub wordt in de browser titel getoond.
		self.assertIn('Visclub Moed & Volharding',  self.browser.title)

		# De pagina heeft een titel "Wedstrijden deze maand"
		self.fail('Finish the test !')

if __name__ == '__main__':
	unittest.main()
