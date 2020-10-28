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


	def test_1_1_install_android_安裝(self):
		print('==========test_1_1_install_android_安裝==========')
		app = self.driver
		while True:
			try:
				app.find_element_by_xpath("//*[@text='允許']").click()
				break
			except NoSuchElementException:
				continue
		time.sleep(3)
		try:
			app.find_element_by_id('com.szoc.zb.cs:id/imageview')
			print('正確!安裝正常完成，無異常')
		except NoSuchElementException:
			print('錯誤!安裝失敗,用戶引導頁沒有顯示')
			raise AssertionError('錯誤!安裝失敗,用戶引導頁沒有顯示')
