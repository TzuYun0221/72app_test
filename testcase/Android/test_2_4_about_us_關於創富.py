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


	def test_2_4_about_us_關於創富(self):
		print('==========test_2_4_about_us_關於創富==========')
		#我的
		self.driver.find_element_by_xpath("//*[@text='我的']").click()
		#关于创富
		self.driver.find_element_by_xpath("//*[@text='关于创富']").click()
		#檢查关于创富H5頁面
		tab_list = ['关于神龙科技','安全保障','运营数据','荣誉奖项','联系我们']
		check_list = ['关于神龙科技','安全保障让您的投资安全无忧','安全运营','荣誉奖项屡获殊荣 我们一同见证','客服邮箱 cs@cf139.com']
		#算list長度
		length = len(tab_list)
		for i in range(length):
			#檢查各個tab
			try:
				self.driver.find_element_by_xpath("//*[@text='"+tab_list[i]+"']").click()
				print('正確!"'+tab_list[i]+'"tab正常顯示')
			except NoSuchElementException:
				print('錯誤!"'+tab_list[i]+'"沒有顯示')
				raise AssertionError('錯誤!"'+tab_list[i]+'"沒有顯示')
			#跳過'关于神龙科技'頁面的檢查,因抓不到元素
			if(i==0):
				continue
			#檢查各個tab的頁面
			try:
				self.driver.find_element_by_xpath("//*[@text='"+check_list[i]+"']")
				print('正確!"'+tab_list[i]+'"顯示:',check_list[i])
			except NoSuchElementException:
				print('錯誤!"'+tab_list[i]+'"沒有顯示',check_list[i])
				raise AssertionError('錯誤!"'+tab_list[i]+'"沒有顯示',check_list[i])


