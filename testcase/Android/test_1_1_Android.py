import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Remote(Remote_url, desired_caps)
		print(" -- set up finished -- ")

	def tearDown(self):
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_1_1_Android(self):
		print('==========test_1_1_Android==========')
		app = self.driver
		x=app.get_window_size()['width']
		y=app.get_window_size()['height']
		x2=x*0.1
		y1=y*0.5
		x1=x*0.9
		while True:
			try:
				app.find_element_by_id('com.szoc.zb.cs:id/userhelp_page')
				break
			except NoSuchElementException:
				continue
		#el01 = driver.find_element_by_id('com.szoc.zb.cs:id/userhelp_page')
		for i in range(3):
			TouchAction(app).press(x=x1,y=y1).move_to(x=x2,y=y1).release().perform()
			time.sleep(1)
		for i in range(3):
			TouchAction(app).press(x=x2,y=y1).move_to(x=x1,y=y1).release().perform()
			time.sleep(1)
