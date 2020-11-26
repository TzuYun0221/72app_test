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


	def test_5_9_MyPage_android_我頁面_推薦有獎(self):
		print('==========test_5_9_MyPage_android_我頁面_推薦有獎==========')
		#登入
		Login(self)
		#點擊我的頁面
		press_my_button(self)
		#點擊活動中心
		self.driver.find_element_by_xpath("//*[@text='推荐有奖']").click()
		#檢查字段
		print('檢查是否跳轉至推薦有獎頁面')
		#截取標題做比對
		app_title_expect = '推荐有奖'
		app_title = self.driver.find_element_by_id(package_name+":id/app_title").text

		if(app_title == app_title_expect):
			print('正確!已跳轉至',app_title)
		else:
			print('錯誤!未跳轉至推薦有獎,目前跳轉至',app_title)
			self.assertEqual(app_title,app_title_expect)
		#QRCODE
		try:
			self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]")
			print('正確!二維碼有顯示')
		except NoSuchElementException:
			print('錯誤!二維碼沒有顯示')
			raise AssertionError('錯誤!二維碼沒有顯示')
		#客服
		print('\n檢查推薦有獎之客服按鈕')
		#點擊客服
		self.driver.find_element_by_accessibility_id("javascript:void(0)").click()
		#檢查客服中心標題
		title = self.driver.find_element_by_id(package_name+':id/app_title').text
		title_expect = '客服'
		if(title == title_expect):
			print('正確!客服中心標題顯示:',title)
		else:
			print('錯誤!客服中心標題顯示:',title)
			raise AssertionError('錯誤!客服中心標題顯示:',title)
		#檢查消息輸入欄"发送"按鈕有無顯示
		try:
			self.driver.find_element_by_xpath("//*[@text='发送']")
			print('正確!消息發送按鈕顯示顯示"发送"')
		except NoSuchElementException:
			print('錯誤!消息發送按鈕沒有顯示"发送"')
			raise AssertionError('錯誤!消息發送按鈕沒有顯示"发送"')
		#關閉H5
		close_html5(self)
		#分享
		print('\n檢查立即推薦好友')
		el5 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"立即推荐好友 一键分享，轻松领奖\"]/android.widget.TextView[1]")
		el5.click()
		#檢查分享彈窗
		share_element_texts = ['分享到','微信好友','微信朋友圈']
		for txt in share_element_texts:
			try:
				title_text = self.driver.find_element_by_xpath("//*[@text='"+txt+"']").text
				print('正確!'+txt+'標題顯示:',title_text)
			except NoSuchElementException:
				print('錯誤!'+txt+'標題沒有顯示')
				raise AssertionError('錯誤!'+txt+'標題沒有顯示')
		#關閉分享彈窗
		close_share_window(self)
		print('\n檢查活動條款')
		#活动条款和细则
		el7 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]")
		el7.click()
		try:
			title_text = self.driver.find_element_by_xpath("//*[@text='活动条款和细则']").text
			print('正確!活動條款標題顯示:',title_text)
		except NoSuchElementException:
			print('錯誤!活動條款標題沒有顯示')
			raise AssertionError('錯誤!活動條款標題沒有顯示')
		#關閉H5
		close_html5(self)
		#登出
		Logout(self)