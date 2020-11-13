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


	def test_5_4_MyPage_android_我頁面_真實模擬切換(self):
		print('==========test_5_4_MyPage_android_我頁面_真實/模擬切換==========')
		#登入
		Login(self)
		#點擊我的頁面
		press_my_button(self)
		#檢查真實模擬
		print_list = ['切換模擬...','切換真實...']
		check_list = [main_user_demo_id,main_user_id]
		length = len(check_list) 
		for i in range(length):
			print(print_list[i])
			#點擊我頁面切換真實模擬
			click_mypage_switch_account(self)
			#取得帳號
			account_num = get_demo_account_information(self)
			#檢查帳號是否切換
			if(account_num == check_list[i]):
				print('正確!已切換為'+print_list[i][2:4]+'帳號,帳號顯示:',account_num)
			else:
				print('錯誤!未切換為'+print_list[i][2:4]+'帳號,帳號顯示:',account_num)
				raise AssertionError('錯誤!未切換為'+print_list[i][2:4]+'帳號,帳號顯示:',account_num)
		#登出
		Logout(self)