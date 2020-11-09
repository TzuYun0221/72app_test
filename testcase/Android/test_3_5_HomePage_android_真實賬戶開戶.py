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
		#登出(Parameter)
		Logout(self)
		#關閉app
		self.driver.quit()
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
		#隨機產生密碼
		random_password = generate_random_password(self)
		#透過api將手機號碼加至白名單
		White_List_API(self,random_phone)
		#點擊首頁登入/註冊(Parameter)
		click_home_register_login(self)		
		#點擊開戶
		el1 = self.driver.find_element_by_id("com.szoc.zb.cs:id/open_account_button")
		el1.click()
		#檢查字段
		print('檢查真實開戶頁面是否正常')
		check_text_list = ['真实开户','手机号码','自设密码','手机验证码','获取验证码','提交资料']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('測試真實開戶...')
		#輸入手機
		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.EditText")
		el1.click()
		el1.send_keys(random_phone)
		time.sleep(2)
		#自設密碼
		el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText")
		el2.click()
		el2.send_keys(random_password)
		time.sleep(2)
		#手機驗證碼
		el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText")
		el3.click()
		el3.send_keys(verification_code)
		time.sleep(2)
		#提交資料
		el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]")
		el4.click()

		#檢查字段
		print('檢查提交資料頁面是否正常')
		check_text_list = ['补充资料','迷你','标准','铂金','巴菲特级','真实姓名','身份证号','常用邮箱','完成开户',
		'* 为保障您的资金安全，真实交易前必须完善以下资料','用户协议']
		for check_text in check_text_list:
			try:
				text_result = self.driver.find_element_by_xpath("//*[@text='"+check_text+"']").text
				print('正確!'+check_text+'字段顯示:',text_result)
			except NoSuchElementException:
				print('錯誤!'+check_text+'字段沒有顯示')
				raise AssertionError('錯誤!'+check_text+'字段沒有顯示')
		print('測試真實開戶補充資料...')
		#隨機中文名(Parameter)
		random_name = random_chinese_name(self)
		#隨機產生身分證API(Parameter)
		random_id = user_id_card_api(self)
		#隨機6~8碼密碼
		#隨機選取級別
		random_level = random.choice(['迷你','标准','铂金','巴菲特级'])
		self.driver.find_element_by_xpath("//*[@text='"+random_level+"']").click()
		#填真實姓名
		el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View[1]/android.widget.EditText")
		el5.click()
		el5.send_keys(random_name)
		time.sleep(2)
		#填身分證號
		el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View[3]/android.widget.EditText")
		el6.click()
		el6.send_keys(random_id)
		time.sleep(2)
		#填常用郵箱
		el7 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View[4]/android.widget.EditText")
		el7.click()
		el7.send_keys('yoyo.ho@itnsl.net')
		time.sleep(2)
		#完成開戶
		el8 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="完成开户"]/android.widget.TextView')
		el8.click()

		success_text_expect = random_phone + '真实账号注册成功'
		try:
			success_text_result = self.driver.find_element_by_xpath("//*[@text='"+success_text_expect+"']").text
			print('正確!開戶成功後顯示:',success_text_result)
		except NoSuchElementException:
			print('錯誤!開戶成功後字段沒有顯示')
			raise AssertionError('錯誤!開戶成功後字段沒有顯示')
		
		#確認立記體驗是否會自動登入,並存取帳戶資訊至csv
		check_new_account_login(self,'真實',random_password)
		