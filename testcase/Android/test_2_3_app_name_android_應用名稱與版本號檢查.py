import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		#檢查app是否安裝,若沒安裝則會自行安裝(Parameter)
		check_app_installed(self)
		#開啟app的參數
		self.driver = webdriver.Remote(Remote_url, desired_caps)
		#設置隱性等待10秒
		self.driver.implicitly_wait(10)
		#跳過廣告(Parameter)
		skip_ads(self)
		print(" -- set up finished -- ")

	def tearDown(self):
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_2_3_app_name_android_應用名稱與版本號檢查(self):
		print('==========test_2_3_app_name_android_應用名稱與版本號檢查==========')
		#我的
		self.driver.find_element_by_xpath("//*[@text='我的']").click()
		#設定
		self.driver.find_element_by_id('com.szoc.zb.cs:id/iv_user_center_setting').click()
		#关于我们
		self.driver.find_element_by_xpath("//*[@text='关于我们']").click()
		#應用名稱檢查(取前6字)
		app_name = self.driver.find_element_by_id('com.szoc.zb.cs:id/item_title').text[:6]
		#應用版本檢查(取後7字)
		app_version = self.driver.find_element_by_id('com.szoc.zb.cs:id/item_title').text[7:]
		if(app_name == app_name_expect):
			print('正確!應用名稱顯示:',app_name)
		else:
			print('錯誤!應用名稱顯示:',app_name)
			raise AssertionError('錯誤!應用名稱顯示:',app_name)
		
		if(app_version == app_version_expect):
			print('正確!版本號顯示:',app_version)
		else:
			print('錯誤!版本號顯示:',app_version)
			raise AssertionError('錯誤!版本號顯示:',app_version)
			
		
