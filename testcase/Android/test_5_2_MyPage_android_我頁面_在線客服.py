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


	def test_5_2_MyPage_android_我頁面_在線客服(self):
		print('==========test_5_2_MyPage_android_我頁面_在線客服==========')
		#點擊我的頁面
		press_my_button(self)
		#點擊我頁面在線客服
		click_mypage_customer_service(self)
		#檢查客服中心標題
		title = self.driver.find_element_by_id(package_name+':id/app_title').text
		title_expect = '客服'
		if(title == title_expect):
			print('正確!客服中心標題顯示:',title)
		else:
			print('錯誤!客服中心標題顯示:',title)
			raise AssertionError('錯誤!客服中心標題顯示:',title)
		#檢查消息輸入欄"发送"按鈕有無顯示
		try:
			self.driver.find_element_by_xpath("//*[@text='发送']")
			print('正確!消息發送按鈕顯示顯示"发送"')
		except NoSuchElementException:
			print('錯誤!消息發送按鈕沒有顯示"发送"')
			raise AssertionError('錯誤!消息發送按鈕沒有顯示"发送"')
