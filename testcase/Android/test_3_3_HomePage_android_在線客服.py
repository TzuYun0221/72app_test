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


	def test_3_3_HomePage_android_在線客服(self):
		print('==========test_3_3_HomePage_android_在線客服==========')
		#點擊首頁客服中心
		click_home_customer_service(self)
		#檢查客服中心標題
		title = self.driver.find_element_by_id(package_name+':id/app_title').text
		title_expect = '客服'
		if(title == title_expect):
			print('正確!客服中心標題顯示:',title)
		else:
			print('錯誤!客服中心標題顯示:',title)
			raise AssertionError('錯誤!客服中心標題顯示:',title)
		#檢查消息輸入欄(透過元素id檢查該元素有沒有跑出來)
		#'enter' 'inputbox' 'menubtn'
		id_check_list = ['enter','inputbox','menubtn']
		for current_id in id_check_list:
			try:
				self.driver.find_element_by_id(current_id)
			except NoSuchElementException:
				print('錯誤!消息輸入欄沒有顯示')
				raise AssertionError('錯誤!消息輸入欄沒有顯示')

		print('正確!消息輸入欄顯示正確')
		


