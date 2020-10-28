import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Remote(Remote_url, desired_caps)
		print(" -- set up finished -- ")

	def tearDown(self):
		#self.driver.quit()
		print('-- tear down finished -- ')


	def test_1_3_uninstall_android_卸載(self):
		print('==========test_1_3_uninstall_android_卸載==========')
		app = self.driver
		app.removeApp(desired_caps['appPackage'])
