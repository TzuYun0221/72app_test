import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		#檢查app是否安裝,若沒安裝則會自行安裝(Parameter)
		check_app_installed(self)
		#開啟app的參數
		self.driver = webdriver.Remote(Remote_url, desired_caps_reset)
		#設置隱性等待10秒
		self.driver.implicitly_wait(10)
		print(" -- set up finished -- ")

	def tearDown(self):
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_2_1_guide_page_android_引導頁檢查(self):
		print('==========test_2_1_guide_page_android_引導頁檢查==========')
		#首次開啟app點擊允許通話權限
		while True:
			try:
				self.driver.find_element_by_xpath("//*[@text='允許']").click()
				break
			except NoSuchElementException:
				continue
		#取得當前裝置螢幕大小(滑動引導頁使用)
		x=self.driver.get_window_size()['width']
		y=self.driver.get_window_size()['height']
		x2=x*0.1
		y1=y*0.5
		x1=x*0.9
		for i in range(3):
			#檢查引導頁
			try:
				self.driver.find_element_by_id('com.szoc.zb.cs:id/imageview')
			except NoSuchElementException:
				print('錯誤!引導頁未顯示')
				raise AssertionError('錯誤!引導頁未顯示')
			#同一Y軸由右向左滑
			TouchAction(self.driver).press(x=x1,y=y1).move_to(x=x2,y=y1).release().perform()
		
		try:
			self.driver.find_element_by_xpath("//*[@text='立即体验']").click()
			print('正確!立即体验按鈕正確顯示')
		except NoSuchElementException:
			print('錯誤!立即体验按鈕未顯示')
			raise AssertionError('錯誤!立即体验按鈕未顯示')

		#檢查按立即體驗後是否跳至小白老司機頁面
		try:
			self.driver.find_element_by_id('com.szoc.zb.cs:id/iv_tutorial_map')
			print('正確!引導頁運作正常')
		except NoSuchElementException:
			print('錯誤!引導頁運作異常')
			raise AssertionError('錯誤!引導頁運作異常')
			
		
