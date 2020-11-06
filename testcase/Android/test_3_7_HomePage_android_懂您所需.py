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


	def test_3_7_HomePage_android_懂您所需(self):
		print('==========test_3_7_HomePage_android_懂您所需==========')
		clever_need_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout'
		#往下滑
		scroll_down(self)
		#懂你所需左滑至同時顯示第一與第四個元素
		clever_need_swipe_left(self)
		print('懂你所需左滑...')
		try:
			#檢查第一個元素是否存在
			self.driver.find_element_by_xpath(clever_need_picture_xpath+'[1]')
			print('正確!第一個圖片正確顯示')
		except NoSuchElementException:
			print('錯誤!第一個圖片沒有顯示')
			raise AssertionError('錯誤!第一個圖片沒有顯示')
		try:
			#檢查第四個元素是否存在
			self.driver.find_element_by_xpath(clever_need_picture_xpath+'[4]')
			print('正確!懂你所需左滑成功,第四個圖片正確顯示')
		except NoSuchElementException:
			print('錯誤!懂你所需左滑失敗,第四個圖片沒有顯示')
			raise AssertionError('錯誤!懂你所需左滑失敗,第四個圖片沒有顯示')
		#懂你所需右滑至看不到第四個元素
		clever_need_swipe_right(self)
		print('懂你所需右滑...')
		try:
			#檢查第四個元素是否存在
			self.driver.find_element_by_xpath(clever_need_picture_xpath+'[4]')
			print('錯誤!懂你所需右滑失敗,第四個圖片仍然顯示')
			raise AssertionError('錯誤!懂你所需右滑失敗,第四個圖片仍然顯示')
		except NoSuchElementException:
			print('正確!懂你所需右滑成功,第四個圖片沒有顯示')

		#懂你所需隨機點擊一張圖片
		picture_list = ['[1]','[2]','[3]']
		random_picture_xpath=clever_need_picture_xpath+random.choice(picture_list)
		self.driver.find_element_by_xpath(random_picture_xpath).click()
		#檢查是否有跳轉
		try:
			#頂部叉叉
			self.driver.find_element_by_id(package_name+':id/title_left_secondary_icon')
			#標題
			title = self.driver.find_element_by_id(package_name+':id/app_title').text
			print('正確!點擊懂你所需圖片跳轉至',title)
		except NoSuchElementException:
			print('錯誤!點擊懂你所需圖片無法跳轉')
			raise AssertionError('錯誤!點擊懂你所需圖片無法跳轉')
		print('點擊右上角分享...')
		#點擊右上角分享
		self.driver.find_element_by_id(package_name+':id/title_right_btn').click()
		#檢查分享彈窗
		share_element_texts = ['分享到','微信好友','微信朋友圈']
		for txt in share_element_texts:
			try:
				title_text = self.driver.find_element_by_xpath("//*[@text='"+txt+"']").text
				print('正確!'+txt+'標題顯示:',title_text)
			except NoSuchElementException:
				print('錯誤!'+txt+'標題沒有顯示')
				raise AssertionError('錯誤!'+txt+'標題沒有顯示')


