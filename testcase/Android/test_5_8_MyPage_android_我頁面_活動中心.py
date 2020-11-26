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


	def test_5_8_MyPage_android_我頁面_活動中心(self):
		print('==========test_5_8_MyPage_android_我頁面_活動中心==========')
		#點擊我的頁面
		press_my_button(self)
		#點擊活動中心
		self.driver.find_element_by_xpath("//*[@text='活动中心']").click()

		#截取標題做比對
		app_title_expect = '活动中心'
		app_title = self.driver.find_element_by_id(package_name+":id/app_title").text

		if(app_title == app_title_expect):
			print('正確!已跳轉至',app_title)
		else:
			print('錯誤!未跳轉至活動中心,目前跳轉至',app_title)
			self.assertEqual(app_title,app_title_expect)

		