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
		self.driver.implicitly_wait(20)
		print(" -- set up finished -- ")

	def tearDown(self):
		#關閉app
		self.driver.quit()
		print('-- tear down finished -- ')


	def test_5_7_MyPage_android_我頁面_資金明細(self):
		print('==========test_5_7_MyPage_android_我頁面_資金明細==========')
		#登入
		Login(self)
		#點擊交易tab
		click_transaction(self)
		#點擊更多
		self.driver.find_element_by_xpath("//*[@text='更多']").click()
		#查询历史盈亏
		self.driver.find_element_by_xpath("//*[@text='查询历史盈亏']").click()
		#抓取歷史盈虧第一筆記錄(後面與資金明細比較)
		try:
			record_expect = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View").text
		except NoSuchElementException:
			record_expect = ''
		#關閉H5
		close_html5(self)
		#點擊我的頁面
		press_my_button(self)
		#點擊資金明細
		click_mypage_funding_details(self)
		#檢查字段
		print('檢查資金明細頁面字段是否正常顯示')
		check_text_list = ['资金明细','总收入','总支出','筛选']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('正確!資金明細頁面字段正常顯示\n')
		#檢查資金明細記錄
		print('檢查資金明細記錄')
		try:
			record = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View").text
			if(record == record_expect):
				print('正確!資金明細記錄第一筆顯示:',record)
			else:
				print('錯誤!資金明細記錄第一筆顯示:',record)
				self.assertEqual(record_expect, record)
		except NoSuchElementException:
			if(record_expect == ''):
				print('正確!資金明細記錄正常顯示')
			else:
				print('錯誤!資金明細記錄沒有顯示')
				raise AssertionError('錯誤!資金明細記錄沒有顯示')

		#關閉H5
		close_html5(self)
		#登出
		Logout(self)