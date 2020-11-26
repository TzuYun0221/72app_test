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


	def test_5_11_MyPage_android_隱私條款_文本檢查(self):
		print('==========test_5_11_MyPage_android_隱私條款_文本檢查==========')
		#點擊我的頁面
		press_my_button(self)
		#點擊我頁面設置
		click_mypage_setting(self)

		self.driver.find_element_by_xpath("//*[@text='关于我们']").click()

		self.driver.find_element_by_xpath("//*[@text='隐私条款']").click()

		des_view = self.driver.find_element_by_id(package_name+':id/qpp_des_view').text

		if("创富CFD" in des_view):
			print('正確!產品介紹公司名顯示:创富CFD')
		elif("创富国际" in des_view):
			print('正確!產品介紹公司名顯示:创富国际')
		else:
			print('錯誤!產品介紹公司名未包含"创富CFD"或"创富国际"')
			raise AssertionError('錯誤!產品介紹公司名未包含"创富CFD"或"创富国际"')