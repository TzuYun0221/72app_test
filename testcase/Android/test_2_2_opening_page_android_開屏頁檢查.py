import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		#檢查app是否安裝,若沒安裝則會自行安裝(Parameter)
		check_app_installed(self)
		#開啟app的參數
		self.driver = webdriver.Remote(Remote_url, desired_caps)
		#設置隱性等待10秒
		#self.driver.implicitly_wait(10)
		print(" -- set up finished -- ")

	def tearDown(self):
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_2_2_opening_page_android_開屏頁檢查(self):
		print('==========test_2_2_opening_page_android_開屏頁檢查==========')
		#開屏頁檢查
		try:
			self.driver.find_element_by_id('com.szoc.zb.cs:id/welacome_layout')
			print('正確!開屏頁正常顯示')
		except NoSuchElementException:
			print('錯誤!開屏頁沒有顯示')
			raise AssertionError('錯誤!開屏頁沒有顯示')
			
		
