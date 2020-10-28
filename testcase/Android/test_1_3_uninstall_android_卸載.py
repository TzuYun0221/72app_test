import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		#檢查app是否安裝,若沒安裝則會自行安裝(Parameter)
		check_app_installed(self)
		#開啟app的參數
		self.driver = webdriver.Remote(Remote_url, desired_caps)
		print(" -- set up finished -- ")

	def tearDown(self):
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_1_3_uninstall_android_卸載(self):
		print('==========test_1_3_uninstall_android_卸載==========')
		app = self.driver
		#首次開啟app點擊允許通話權限
		while True:
			try:
				app.find_element_by_xpath("//*[@text='允許']").click()
				break
			except NoSuchElementException:
				continue
		time.sleep(3)
		#執行卸載app
		app.remove_app(desired_caps['appPackage'])
		time.sleep(3)
		#檢查app是否卸載
		if(app.is_app_installed(desired_caps['appPackage'])==False):
			print('正確!卸載正常完成，無異常')
		else:
			print('錯誤!卸載失敗')
			raise AssertionError('錯誤!卸載失敗')
