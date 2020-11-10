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


	def test_5_1_MyPage_android_我頁面_消息中心(self):
		print('==========test_5_1_MyPage_android_我頁面_消息中心==========')
		#點擊我的頁面
		press_my_button(self)
		#點擊我頁面在線客服
		click_mypage_customer_service(self)
		
