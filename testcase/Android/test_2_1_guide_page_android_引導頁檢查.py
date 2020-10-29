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


	def test_2_1_guide_page_android_引導頁檢查(self):
		print('==========test_2_1_guide_page_android_引導頁檢查==========')
		app = self.driver
		#首次開啟app點擊允許通話權限
		while True:
			try:
				app.find_element_by_xpath("//*[@text='允許']").click()
				break
			except NoSuchElementException:
				continue
		x=app.get_window_size()['width']
		y=app.get_window_size()['height']
		x2=x*0.1
		y1=y*0.5
		x1=x*0.9
		time.sleep(10)
		for i in range(3):
			'''try:
				app.find_element_by_id('com.szoc.zb.cs:id/imageview')
			except NoSuchElementException:
				print('錯誤!引導頁未顯示')
				raise AssertionError('錯誤!引導頁未顯示')
			try:
				app.find_element_by_id('c4eef242-c138-4302-a540-0768ccb94479')
			except NoSuchElementException:
				print('錯誤!引導頁滾動圓點未顯示')
				raise AssertionError('錯誤!引導頁滾動圓點未顯示')'''
			TouchAction(app).press(x=x1,y=y1).move_to(x=x2,y=y1).release().perform()
			time.sleep(1)
		
		try:
			app.find_element_by_xpath("//*[@text='立即体验']").click()
			print('正確!立即体验按鈕正確顯示')
		except NoSuchElementException:
			print('錯誤!立即体验按鈕未顯示')
			raise AssertionError('錯誤!立即体验按鈕未顯示')
		time.sleep(3)
		try:
			app.find_element_by_id('com.szoc.zb.cs:id/iv_tutorial_map')
			print('正確!引導頁運作正常')
		except NoSuchElementException:
			print('錯誤!引導頁運作異常')
			raise AssertionError('錯誤!引導頁運作異常')
			
		
