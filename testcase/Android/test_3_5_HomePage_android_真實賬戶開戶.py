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
		#self.driver.quit()
		print('-- tear down finished -- ')


	def test_3_5_HomePage_android_真實賬戶開戶(self):
		print('==========test_3_5_HomePage_android_真實賬戶開戶==========')
		#若為PRD執行則跳過此測試
		if(package_name == 'com.gwtsz.gts2.cf'):
			raise AssertionError('錯誤!PRD目前無法自動化測試真實開戶')
		#隨機產生手機號碼
		random_phone = random_phone_number(self)
		#透過api將手機號碼驗証碼產生
		verification_code = register_demo_account_api(self,random_phone)
		#透過api將手機號碼加至白名單
		White_List_API(self,random_phone)
		#點擊首頁登入/註冊(Parameter)
		click_home_register_login(self)		
		#點擊開戶
		el1 = self.driver.find_element_by_id("com.szoc.zb.cs:id/open_account_button")
		el1.click()
		#檢查字段
		print('檢查真實開戶頁面是否正常')
		check_text_list = ['真实开户','真实姓名','手机号码','自设密码','手机验证码','获取验证码','完成开户']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('測試真實開戶...')
		#隨機中文名
		random_name = '測試'
		for i in range(2):
			random_name += chr(random.randint(0x4e00, 0x9fbf))
		#輸入姓名
		el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.EditText")
		el3.click()
		el3.send_keys(random_name)
		time.sleep(2)
		#輸入手機
		el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText")
		el4.click()
		el4.send_keys(random_phone)
		time.sleep(2)
		#自設密碼
		el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText")
		el5.click()
		el5.send_keys("abc123")
		time.sleep(2)
		#輸入驗證碼
		el7 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[4]/android.widget.EditText")
		el7.click()
		el7.send_keys(verification_code)
		time.sleep(2)
		#完成開戶
		el8 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]")
		el8.click()
		success_text_expect = random_phone + '模拟账号注册成功'
		try:
			success_text_result = self.driver.find_element_by_xpath("//*[@text='"+success_text_expect+"']").text
			print('正確!開戶成功後顯示:',success_text_result)
		except NoSuchElementException:
			print('錯誤!開戶成功後字段沒有顯示')
			raise AssertionError('錯誤!開戶成功後字段沒有顯示')