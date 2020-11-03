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


	def test_3_2_HomePage_android_首頁消息中心與我頁面消息中心(self):
		print('==========test_3_2_HomePage_android_首頁消息中心與我頁面消息中心==========')
		#點擊首頁消息中心
		click_home_message_center(self)
		print('首頁消息中心')
		#消息中心 重要公告 系统维护 交易安排 行情提醒
		check_titles = ['消息中心','重要公告','系统维护','交易安排','行情提醒']

		for title in check_titles:
			try:
				self.driver.find_element_by_xpath("//*[@text='"+title+"']")
				print('正確!"'+title+'"正常顯示')
			except NoSuchElementException:
				print('錯誤!"'+title+'"沒有顯示')
				raise AssertionError('錯誤!"'+title+'"沒有顯示')
		#點擊消息中心的返回
		click_message_center_return(self)
		#點擊我的頁面
		press_my_button(self)
		#點擊我頁面消息中心
		click_mypage_message_center(self)
		print('我頁面消息中心')
		#消息中心 重要公告 系统维护 交易安排 行情提醒
		check_titles = ['消息中心','重要公告','系统维护','交易安排','行情提醒']

		for title in check_titles:
			try:
				self.driver.find_element_by_xpath("//*[@text='"+title+"']")
				print('正確!"'+title+'"正常顯示')
			except NoSuchElementException:
				print('錯誤!"'+title+'"沒有顯示')
				raise AssertionError('錯誤!"'+title+'"沒有顯示')


