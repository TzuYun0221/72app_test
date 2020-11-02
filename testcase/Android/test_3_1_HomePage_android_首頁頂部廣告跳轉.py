import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		#開啟app的參數
		self.driver = webdriver.Remote(Remote_url, desired_caps)
		#跳過廣告(Parameter)
		skip_ads(self)
		#設置隱性等待10秒
		self.driver.implicitly_wait(10)
		print(" -- set up finished -- ")

	def tearDown(self):
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_3_1_HomePage_android_首頁頂部廣告跳轉(self):
		print('==========test_3_1_HomePage_android_首頁頂部廣告跳轉==========')
		#點擊首頁輪播廣告
		click_home_banner(self)

		try:
			#頂部叉叉
			self.driver.find_element_by_id('com.szoc.zb.cs:id/title_left_secondary_icon')
			#首頁標題
			title = self.driver.find_element_by_id('com.szoc.zb.cs:id/app_title').text
			print('正確!首頁頂部廣告跳轉至',title)
		except NoSuchElementException:
			print('錯誤!首頁頂部廣告無法跳轉')
			raise AssertionError('錯誤!首頁頂部廣告無法跳轉')


