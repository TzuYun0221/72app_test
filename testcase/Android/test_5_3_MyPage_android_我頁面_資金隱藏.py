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


	def test_5_3_MyPage_android_我頁面_資金隱藏(self):
		print('==========test_5_3_MyPage_android_我頁面_資金隱藏==========')
		#隱藏資金時應顯示
		money_hide_expect = '* * * *'
		#登入
		Login(self)
		#點擊我的頁面
		press_my_button(self)
		#抓取資金文字
		money_hide = self.driver.find_element_by_id(package_name+":id/tv_me_head_amount").text
		#若資金為隱藏狀態則點兩次隱藏資金,否則只點一次
		if(money_hide==money_hide_expect):
			times=2
		else:
			times=1
		for i in range(times):
			#點擊隱藏資金
			self.driver.find_element_by_id(package_name+":id/iv_me_main_eye").click()
		#檢查資金是否顯示****
		money_hide = self.driver.find_element_by_id(package_name+":id/tv_me_head_amount").text
		if(money_hide == money_hide_expect):
			print('正確!資金顯示:',money_hide)
		else:
			print('錯誤!資金顯示:',money_hide)
			raise AssertionError('錯誤!資金顯示:',money_hide)
		#登出
		Logout(self)