# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from random import Random
import unittest, time, re, os
import json
import requests
import csv
random = Random()
#=========UAT/PRD切換測試需更改之參數========
# 指定OS
OS = 'Windows'
#UAT
#package_name = 'com.szoc.zb.cs'
#PRD
package_name = 'com.gwtsz.gts2.cf'
#包為PRD
if(package_name == 'com.gwtsz.gts2.cf'):
	#指定apk路徑
	apk_url = 'C:/Users/Angela/72apptest/20201111-prd-cf-1.8.3-release.apk'
	#應用名稱&版本號(用於關於我們檢查)
	app_name_version_expect = '创富CFD V_1.8.3'
	#關於創富(用於關於創富檢查)
	about_us_expect = '关于创富'
	#登入帳戶
	main_user_id = '81135805'
	main_user_demo_id = '11092003'
	main_user_password = 'abc123'
#包為UAT
else:
	#指定apk路徑
	apk_url = 'C:/Users/Angela/72apptest/1027-uat-cs-1.8.3-release.apk'
	#應用名稱&版本號(用於關於我們檢查)
	app_name_version_expect = 'ISTONE V_1.8.3'
	#關於創富(用於關於創富檢查)
	about_us_expect = '关于神龙科技'
	#登入帳戶
	main_user_id = '81018322'
	main_user_demo_id = '11002074'
	main_user_password = 'abc123'
#=========UAT/PRD切換測試需更改之參數========

account_csv = '帳號列表.csv'
#指定舊版本apk路徑(覆蓋安裝測試)
#old_apk_url = 'C:/Users/Angela/72apptest/20200812-uat-cs-1.8.2-release.apk'
#指定裝置、版本、安裝包
#每次開啟不重置app
desired_caps = {
    #'platformName':'Android',
    #'platformVersion':'5.1.1',
    #'deviceName':'Android Emulator',
    'platformName':'Android',
    'platformVersion':'10',
    'deviceName':'Mi 9t',
    'appPackage': package_name,
    'appActivity':'gw.com.android.ui.WelcomeActivity',
    'newCommandTimeout':6000,
    'noReset':True
}
#每次開啟重置app
desired_caps_reset = {
    'platformName':desired_caps['platformName'],
    'platformVersion':desired_caps['platformVersion'],
    'deviceName':desired_caps['deviceName'],
    'appPackage':desired_caps['appPackage'],
    'appActivity':desired_caps['appActivity'],
    'newCommandTimeout':desired_caps['newCommandTimeout'],
    'noReset':False
}
#不啟動app,開桌面
desired_install = {
    'platformName':desired_caps['platformName'],
    'platformVersion':desired_caps['platformVersion'],
    'deviceName':desired_caps['deviceName'],
}
Remote_url = 'http://localhost:4723/wd/hub'

#檢查app是否安裝,若沒安裝則自動安裝
def check_app_installed():
	driver_install = webdriver.Remote(Remote_url, desired_install)
	if(driver_install.is_app_installed(desired_caps['appPackage'])):
		print('APP已經安裝')
	else:
		driver_install.install_app(apk_url)
		print('APP安裝完畢')
	driver_install.quit()
#跳過廣告
def skip_ads(self):
	time.sleep(7)
	#1.跳過開屏廣告 2.關版本升級 3.關彈窗廣告
	#沒有彈出版本升級或廣告就跳過不執行
	element_list = [package_name+':id/tv_skip',package_name+':id/btn_cancel',package_name+':id/close_btn']
	for element in element_list:
		try:
			self.driver.find_element_by_id(element).click()
		except NoSuchElementException:
			continue

#跳過廣告(不等開屏七秒)
def skip_ads_no_wait(self):
	#設置隱性等待2秒
	self.driver.implicitly_wait(2)
	#1.跳過開屏廣告 2.關版本升級 3.關彈窗廣告
	#沒有彈出版本升級或廣告就跳過不執行
	element_list = [package_name+':id/tv_skip',package_name+':id/btn_cancel',package_name+':id/close_btn']
	for element in element_list:
		try:
			self.driver.find_element_by_id(element).click()
		except NoSuchElementException:
			continue
	self.driver.implicitly_wait(10)

#跳過文字彈窗
def skip_pop_ups_dialog(self):
	try:
		#點擊文字彈窗
		self.driver.find_element_by_xpath("//*[@text='立即前往']").click()
		time.sleep(2)
		#關閉文字彈窗H5
		self.driver.find_element_by_id(package_name+":id/title_left_secondary_icon").click()
	except NoSuchElementException:
		pass

#點允許(在app內時)
def click_allow(self):
	try:
		self.driver.find_element_by_xpath("//*[@text='允許']").click()
		print('點擊允許')
	except NoSuchElementException:
		print('允許未跳出')

#點允許(不在app內時)
def click_allow_outside_app():
	driver_allow = webdriver.Remote(Remote_url, desired_install)
	try:
		driver_allow.find_element_by_xpath("//*[@text='允許']").click()
		print('點擊允許')
	except NoSuchElementException:
		print('允許未跳出')
	driver_allow.quit()
#點擊我的頁面
def press_my_button(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#點擊座標
	TouchAction(self.driver).tap(element=None, x=x*0.9, y=y-1, count=1).perform()
#行情
def click_quotation(self):
	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView")
	element.click()
#取得真實帳號資訊
def get_account_information(self):
	#點我頁面TAB(Parameter)
	press_my_button(self)
	#點我頁面登入頭像
	self.driver.find_element_by_id(package_name+":id/iv_me_head_icon").click()
	#取得帳號
	account_num = self.driver.find_element_by_id(package_name+":id/dialog_content_text2").text
	#取得帳號級別
	account_lvl = self.driver.find_element_by_id(package_name+":id/dialog_content_text3").text
	self.driver.find_element_by_xpath("//*[@text='知道了']").click()
	return account_num,account_lvl
#取得模擬帳號資訊
def get_demo_account_information(self):
	#點我頁面TAB(Parameter)
	press_my_button(self)
	#點我頁面登入頭像
	self.driver.find_element_by_id(package_name+":id/iv_me_head_icon").click()
	#取得帳號
	account_num = self.driver.find_element_by_id(package_name+":id/dialog_content_text2").text
	self.driver.find_element_by_xpath("//*[@text='知道了']").click()
	return account_num
#點擊首頁消息中心
def click_home_message_center(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#點擊座標
	TouchAction(self.driver).tap(element=None, x=x*0.81 ,y=y/19, count=1).perform()
	#透過id
	#self.driver.find_element_by_id('com.szoc.zb.cs:id/message_btn2').click()
#點擊首頁客服中心
def click_home_customer_service(self):
	#透過id
	#self.driver.find_element_by_id(package_name+':id/contact_btn2').click()
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#點擊座標
	TouchAction(self.driver).tap(element=None, x=x*0.93 ,y=y/19, count=1).perform()

#點擊我頁面消息中心
def click_mypage_message_center(self):
	self.driver.find_element_by_id(package_name+":id/iv_user_center_message").click()
#點擊消息中心的返回
def click_message_center_return(self):
	el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.ImageView")
	el2.click()
#點擊我頁面在線客服
def click_mypage_customer_service(self):
	self.driver.find_element_by_id(package_name+":id/rl_user_center_live").click()

#點擊我頁面切換真實模擬
def click_mypage_switch_account(self):
	self.driver.find_element_by_id(package_name+":id/tv_real_demo_switch").click()

#點擊我頁面存款
def click_mypage_deposit(self):
	self.driver.find_element_by_id(package_name+":id/tv_me_main_deposit").click()

#點擊我頁面取款
def click_mypage_withdraw(self):
	self.driver.find_element_by_id(package_name+":id/tv_me_main_withdraw").click()

#點擊首頁輪播廣告
def click_home_banner(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	for i in range(3):
		#點擊座標
		TouchAction(self.driver).tap(element=None, x=x/2 ,y=y/5, count=1).perform()
#點擊首頁登入/註冊
def click_home_register_login(self):
	#做標定位只適用螢幕大小 2340*1080
	#TouchAction(self.driver).tap(x=931, y=2149).perform()
	#文字定位全部適用,但定位時間較久
	self.driver.find_element_by_xpath("//*[@text='登录/注册']").click()
#關閉H5
def close_html5(self):
	#關閉H5
	self.driver.find_element_by_id(package_name+":id/title_left_secondary_icon").click()

#往下滑
def scroll_down(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	x1=x/2
	y1=y*0.8
	y2=y*0.3
	#TouchAction(self.driver).press(x=x1, y=y1).move_to(x=x1, y=y2).release().perform()
	self.driver.swipe(x1,y1,x1,y2,1000)

#懂你所需左滑
def clever_need_swipe_left(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#懂你所需
	coordinates = self.driver.find_element_by_id(package_name+':id/home_clever_need').location
	y1 = coordinates['y'] + y/10
	x1 = x*0.72
	x2 = x*0.6
	self.driver.swipe(x1,y1,x2,y1,1000)

#懂你所需右滑
def clever_need_swipe_right(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#懂你所需
	coordinates = self.driver.find_element_by_id(package_name+':id/home_clever_need').location
	y1 = coordinates['y'] + y/10
	x2 = x*3/4
	x1 = x/4
	self.driver.swipe(x1,y1,x2,y1,1000)

#隨機產生密碼
def generate_random_password(self):
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqstuvwxyz0123456789'
	length = len(chars) - 1
	random_password = ''
	for i in range(random.randint(6,8)):
		random_password+=chars[random.randint(0,length)]
	random_password+=str(random.randint(0,9))
	return random_password

#隨機產生電話
def random_phone_number(self):
	area_list = ['130', '131', '132', '133', '134', '135', '136', '137',
	'138', '139', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159','188','189']
	numbers = '0123456789'
	random_phone = random.choice(area_list)
	for i in range(8):
		random_phone+=numbers[random.randint(0,9)]
	return random_phone
#隨機產生中文名
def random_chinese_name(self):
	#隨機中文名
	random_name = '測試'
	for i in range(2):
		random_name += chr(random.randint(0x4e00, 0x9fbf))
	return random_name
#產生身分證API
def user_id_card_api(self):
	request_url = "https://www.googlespeed.cn/idcard/ajax_get_idcard"
	years = str(random.randint(1940,2001))
	month = str(random.randint(1,12))
	days = str(random.randint(1,30))
	if(len(month)==1):
		month = '0'+month
	if(len(years)==1):
		years = '0'+years
	if(len(days)==1):
		days = '0'+days
	payload = {'sex': random.choice(['男','女']),
	'year': years,
	'month': month,
	'day': days}

	response = requests.request("POST", request_url, headers={}, data = payload)

	data = response.json()
	return data['id_list'][0]['id_card']


#獲取驗證碼API
def register_demo_account_api(self,random_phone):
	request_url = "http://mis.will68.com/ValidateCodeLog/createValidateNo"

	payload = random_phone
	headers = {
	  'Cookie': '_ga=GA1.1.280281216.1603264849; _ga_DR6HQD5SM3=GS1.1.1604370924.4.0.1604370929.0; JSESSIONID=6E3FAB6D7BD7F37DC94282001269EB03; lang_type=0; cf88_id="user:1:3dce2613-06a3-45b3-ad00-6ba6f75d79a3"',
	  'Content-Type': 'text/plain'
	}

	response = requests.request("POST", request_url, headers=headers, data = payload)
	data = response.json()
	#回傳驗證碼
	return data['data']

#添加白名單API
def White_List_API(self,random_phone):
	request_url = "http://mis.will68.com/whitelists/edit"
	payload = "{\"status\": 1, \"phone\": \""+random_phone+"\"}"
	headers = {
	  'Cookie': '_ga=GA1.1.280281216.1603264849; _ga_DR6HQD5SM3=GS1.1.1604370924.4.0.1604370929.0; lang_type=0; JSESSIONID=C3883C50852D325D183B1E41F2DC8EF3; cf88_id="user:1:e7b99c9d-3916-461a-8d2d-975f7eeb18d7"',
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", request_url, headers=headers, data = payload)
	data = response.json()
	print('添加白名單結果為:',data['msg'])
#登入
def Login(self):
	#點登錄註冊
	click_home_register_login(self)
	el1 = self.driver.find_element_by_id(package_name+":id/loginnameEditText")
	el1.clear()
	el1.send_keys(main_user_id)
	el2 = self.driver.find_element_by_id(package_name+":id/password")
	el2.clear()
	el2.send_keys(main_user_password)
	el3 = self.driver.find_element_by_id(package_name+":id/sign_in_button")
	el3.click()
	#跳廣告
	skip_ads_no_wait(self)
#登出
def Logout(self):
	#切至我的頁面
	press_my_button(self)
	#點擊設置
	el1 = self.driver.find_element_by_id(package_name+":id/iv_user_center_setting")
	el1.click()
	#退出登錄
	el2 = self.driver.find_element_by_xpath("//*[@text='退出登录']")
	el2.click()
	#確認
	el3 = self.driver.find_element_by_id(package_name+":id/action_btn_pos")
	el3.click()


def check_new_account_login(self,account_type,password):
	if(account_type=='真實'):
		try:
			#點立擊體驗
			self.driver.find_element_by_xpath("//*[@text='立即体验']").click()
			#跳過廣告(不等開屏七秒)
			skip_ads_no_wait(self)
			#抓取帳號資訊(Parameter)
			account_num,account_lvl = get_account_information(self)
			print('開戶成功!帳號為:'+account_num,'級別為:'+account_lvl)
		except NoSuchElementException:
			print('錯誤!開戶後無法正常進入登入後畫面')
			raise AssertionError('錯誤!開戶後無法正常進入登入後畫面')

		# 讀取預約表(方便寫入資料)
		with open(account_csv, newline='',encoding="utf-8") as csvfile:
			#讀取預約表內容並存入writed_csv
			rows = csv.reader(csvfile)
			writed_csv = list(rows)
		#寫入(新增帳號資訊)
		with open(account_csv, 'w', newline='',encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile)
			#寫入[帳號,密碼,真實/模擬,帳戶等級]
			account_information = [account_num,password,account_type,account_lvl]
			writed_csv.append(account_information)
			# 寫入CSV
			writer.writerows(writed_csv)
	else:
		try:
			#點立擊體驗
			self.driver.find_element_by_xpath("//*[@text='立即体验']").click()
			#跳過廣告(不等開屏七秒)
			skip_ads_no_wait(self)
			#抓取帳號資訊(Parameter)
			account_num = get_demo_account_information(self)
			print('開戶成功!帳號為:'+account_num)
		except NoSuchElementException:
			print('錯誤!開戶後無法正常進入登入後畫面')
			raise AssertionError('錯誤!開戶後無法正常進入登入後畫面')

		# 讀取預約表(方便寫入資料)
		with open(account_csv, newline='',encoding="utf-8") as csvfile:
			#讀取預約表內容並存入writed_csv
			rows = csv.reader(csvfile)
			writed_csv = list(rows)
		#寫入(新增帳號資訊)
		with open(account_csv, 'w', newline='',encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile)
			#寫入[帳號,密碼,真實/模擬,帳戶等級]
			account_information = [account_num,password,account_type,'']
			writed_csv.append(account_information)
			#寫入CSV
			writer.writerows(writed_csv)








		



