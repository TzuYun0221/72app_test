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


	def test_1_1_install_android_安裝(self):
		print('==========test_1_1_install_android_安裝==========')
		app = self.driver
		#首次開啟app點擊允許通話權限
		while True:
			try:
				app.find_element_by_xpath("//*[@text='允許']").click()
				break
			except NoSuchElementException:
				continue
		time.sleep(10)
		#檢查app是否安裝(開戶引導頁是否正常顯示)
		try:
			app.find_element_by_id('com.szoc.zb.cs:id/imageview')
			print('正確!安裝正常完成，無異常')
		except NoSuchElementException:
			print('錯誤!安裝失敗,用戶引導頁沒有顯示')
			raise AssertionError('錯誤!安裝失敗,用戶引導頁沒有顯示')
