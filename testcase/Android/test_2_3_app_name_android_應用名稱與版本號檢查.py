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


	def test_2_3_app_name_android_應用名稱與版本號檢查(self):
		print('==========test_2_3_app_name_android_應用名稱與版本號檢查==========')
		#我的
		#self.driver.find_element_by_xpath("//*[@text='我的']").click()
		press_my_button(self)
		#設定
		self.driver.find_element_by_id(package_name+':id/iv_user_center_setting').click()
		#关于我们
		self.driver.find_element_by_xpath("//*[@text='关于我们']").click()
		#應用名稱版本檢查(取後7字)
		app_name_version = self.driver.find_element_by_id(package_name+':id/item_title').text
		if(app_name_version == app_name_version_expect):
			print('正確!應用名稱與版本號顯示:',app_name_version)
		else:
			print('錯誤!應用名稱與版本號顯示:',app_name_version)
			raise AssertionError('錯誤!應用名稱與版本號顯示:',app_name_version)
			
		
