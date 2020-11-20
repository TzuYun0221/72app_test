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


	def test_5_7_MyPage_android_我頁面_資金明細(self):
		print('==========test_5_7_MyPage_android_我頁面_資金明細==========')
		#登入
		Login(self)
		#點擊我的頁面
		press_my_button(self)
		#點擊資金明細
		click_mypage_funding_details(self)
		#檢查字段
		print('檢查資金明細頁面字段是否正常顯示')
		check_text_list = ['资金明细','总收入','总支出','筛选']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('正確!資金明細頁面字段正常顯示')
		#關閉H5
		close_html5(self)
		#登出
		Logout(self)