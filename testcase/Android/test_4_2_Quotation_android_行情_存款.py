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


	def test_4_2_Quotation_android_行情_存款(self):
		print('==========test_4_2_Quotation_android_行情_存款==========')
		#登入
		Login(self)
		#行情tab
		click_quotation(self)
		#點擊存款
		self.driver.find_element_by_xpath('//*[@text="存款"]').click()

		#檢查字段
		print('檢查存款頁面是否顯示')
		check_text_list = ['存款','支付方式','存款金额（美元）','确认存款']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('正確!點擊行情-存款可以正確跳至存款頁面')
		#關閉存款H5
		self.driver.find_element_by_id(package_name+":id/title_left_secondary_icon").click()
		#登出
		Logout(self)
