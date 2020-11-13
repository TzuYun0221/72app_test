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


	def test_5_5_MyPage_android_我頁面_取款(self):
		print('==========test_5_5_MyPage_android_我頁面_取款==========')
		#登入
		Login(self)
		#點擊我的頁面
		press_my_button(self)
		#點擊我頁面取款
		click_mypage_withdraw(self)
		#檢查字段
		print('檢查取款頁面是否顯示')
		check_text_list = ['取款','取款至','取款记录','取款金额（美元）','手续费']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('正確!點擊我頁面_取款可以正確跳至存款頁面')
		#關閉H5
		close_html5(self)
		#登出
		Logout(self)