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


	def test_4_1_Quotation_android_行情_真實模擬切換(self):
		print('==========test_4_1_Quotation_android_行情_真實模擬切換==========')
		#登入
		Login(self)
		#行情tab
		click_quotation(self)
		#點擊真實
		el5 = self.driver.find_element_by_id(package_name+":id/arrow_up")
		el5.click()
		print('真實切換模擬')
		#切換模擬
		el6 = self.driver.find_element_by_id(package_name+":id/tv_up")
		el6.click()
		try:
			switch_button = self.driver.find_element_by_xpath('//*[@text="模拟"]').text
			print('正確!切換鍵切換後字段顯示:',switch_button)
		except NoSuchElementException:
			print('錯誤!切換鍵切換後字段沒有顯示')
			raise AssertionError('錯誤!切換鍵切換後字段沒有顯示')
		#取得模擬帳號資訊
		account_num = get_demo_account_information(self)
		if(account_num == main_user_demo_id):
			print('正確!已切換為模擬帳號,帳號顯示:',account_num)
		else:
			print('錯誤!未切換為模擬帳號,帳號顯示:',account_num)
			raise AssertionError('錯誤!未切換為模擬帳號,帳號顯示:',account_num)
		#行情tab
		click_quotation(self)
		#點擊模擬
		el7 = self.driver.find_element_by_id(package_name+":id/arrow_up")
		el7.click()
		print('模擬切換真實')
		#切換真實
		el8 = self.driver.find_element_by_id(package_name+":id/tv_up")
		el8.click()
		try:
			switch_button = self.driver.find_element_by_xpath('//*[@text="真实"]').text
			print('正確!切換鍵切換後字段顯示:',switch_button)
		except NoSuchElementException:
			print('錯誤!切換鍵切換後字段沒有顯示')
			raise AssertionError('錯誤!切換鍵切換後字段沒有顯示')
		#取得真實帳號資訊
		account_num,account_lvl = get_account_information(self)
		if(account_num == main_user_id):
			print('正確!已切換為真實帳號,帳號顯示:',account_num)
		else:
			print('錯誤!未切換為真實帳號,帳號顯示:',account_num)
			raise AssertionError('錯誤!未切換為真實帳號,帳號顯示:',account_num)
		#登出
		Logout(self)


