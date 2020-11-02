import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		#開啟app的參數
		self.driver = webdriver.Remote(Remote_url, desired_install)
		#設置隱性等待10秒
		self.driver.implicitly_wait(10)
		print(" -- set up finished -- ")

	def tearDown(self):
		#檢查app是否安裝,若沒安裝則會自行安裝(Parameter)
		check_app_installed()
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_1_3_uninstall_android_卸載(self):
		print('==========test_1_3_uninstall_android_卸載==========')
		#執行卸載app
		self.driver.remove_app(desired_caps['appPackage'])

		#檢查app是否卸載
		if(self.driver.is_app_installed(desired_caps['appPackage'])==False):
			print('正確!卸載正常完成，無異常')
		else:
			print('錯誤!卸載失敗')
			raise AssertionError('錯誤!卸載失敗')
