# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from random import Random
from datetime import datetime
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
#package_name = 'com.gwtsz.gts2.cf'
#cf2
package_name = 'com.gwtsz.gts2.cf2'
#cf3
#package_name = 'com.gwtsz.gts2.cf3'
#專案目錄
dir_path = os.path.dirname(os.path.realpath(__file__))
#包為PRD
if(package_name == 'com.gwtsz.gts2.cf'):
	#指定apk路徑
	apk_url = dir_path + '/release-cf-1.8.5-release_185_jiagu_sign_zp.apk'
	#應用名稱&版本號(用於關於我們檢查)
	app_name_version_expect = '创富CFD V_1.8.5'
	#關於創富(用於關於創富檢查)
	about_us_expect = '关于创富'
	#登入帳戶
	main_user_id = '81135805'
	main_user_demo_id = '11092003'
	main_user_password = 'abc123'
#包為UAT
elif(package_name == 'com.szoc.zb.cs'):
	#指定apk路徑
	apk_url = dir_path + '/2021-02-17-uat-cs-1.8.6-release.apk'
	#應用名稱&版本號(用於關於我們檢查)
	app_name_version_expect = 'ISTONE V_1.8.3'
	#關於創富(用於關於創富檢查)
	about_us_expect = '关于神龙科技'
	#登入帳戶
	main_user_id = '81018322'
	main_user_demo_id = '11002074'
	main_user_password = 'abc123'
#包為CF2
elif(package_name == 'com.gwtsz.gts2.cf2'):
	#指定apk路徑
	apk_url = dir_path + '/20201120-prd-cf2-1.8.3-release.apk'
	#應用名稱&版本號(用於關於我們檢查)
	app_name_version_expect = '柯洛夫黃金平台 V_1.8.6'
	#關於創富(用於關於創富檢查)
	about_us_expect = '关于创富'
	#登入帳戶
	main_user_id = '81134740'
	main_user_demo_id = '11092003'
	main_user_password = 'abc123'
#包為CF3
else:
	# 指定apk路徑
	apk_url = dir_path + 'release-cf3-1.8.5-release_185_jiagu_sign_zp-update&utm_medium=bycfd.apk'
	# 應用名稱&版本號(用於關於我們檢查)
	app_name_version_expect = '白银交易平台 V_1.8.5'
	# 關於創富(用於關於創富檢查)
	about_us_expect = '关于创富'
	# 登入帳戶
	main_user_id = '81134740'
	main_user_demo_id = '11092003'
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
	time.sleep(12)
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
	#element = self.driver.find_element_by_id('com.gwtsz.gts2.cf:id/radio_button_text').find_element_by_xpath("//*[@text='我的']")
	#element.click()
#行情tab
def click_quotation(self):
	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView")
	element.click()
#交易tab
def click_transaction(self):
	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.ImageView")
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
#關閉分享彈窗
def close_share_window(self):
	self.driver.find_element_by_id(package_name+":id/btn_cancel").click()
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
#點擊我頁面設置
def click_mypage_setting(self):
	self.driver.find_element_by_id(package_name+":id/iv_user_center_setting").click()
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

#點擊我頁面資金明細
def click_mypage_funding_details(self):
	self.driver.find_element_by_xpath("//*[@text='资金明细']").click()
#點擊首頁
def press_home_tab(self):
	self.driver.find_element_by_xpath("//*[@text='首页']").click()
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
def click_home_real_account(self):
	#TouchAction(self.driver).tap(x=750, y=1300).perform()
	while True:
		try:
			#點擊首頁開立真實賬戶
			self.driver.find_element_by_id(package_name + ":id/tv_open_two").click()
			break
		except NoSuchElementException:
			#登出＋回到首頁
			Logout(self)
			press_home_tab(self)
			skip_ads(self)

def click_home_demo_account(self):
	#TouchAction(self.driver).tap(x=250, y=1300).perform()
	while True:
		try:
			#點擊首頁開立模擬賬戶
			self.driver.find_element_by_id(package_name + ":id/tv_open_one").click()
			break
		except NoSuchElementException:
			#登出＋回到首頁
			Logout(self)
			press_home_tab(self)
			skip_ads(self)
#點擊開戶
def click_login_create_account(self):
	self.driver.find_element_by_id(package_name+":id/open_account_button").click()
#點擊模擬開戶
def click_create_demo_account(self):
	self.driver.find_element_by_id(package_name+":id/main_top_right_tab").click()
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
'''def user_id_card_api(self):
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
	return data['id_list'][0]['id_card']'''
#獲取驗證碼API
def register_demo_account_api(self,random_phone):
	if(package_name == 'com.szoc.zb.cs'):
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
	else:
		request_url = "https://office.cf139.com/ValidateCodeLog/createValidateNo"

		payload = random_phone
		headers = {
		  'Connection': 'close',
		  'authority': 'office.cf139.com',
		  'accept': 'application/json, text/plain, */*',
		  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
		  'content-type': 'application/json;charset=UTF-8',
		  'origin': 'https://office.cf139.com',
		  'sec-fetch-site': 'same-origin',
		  'sec-fetch-mode': 'cors',
		  'sec-fetch-dest': 'empty',
		  'referer': 'https://office.cf139.com/home/validater/validateNo',
		  'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
		  'cookie': 'lang_type=0; JSESSIONID=84871DBC50AD6CCE38923B5F4F7FC5DF; cf88_id="user:763:869480c1-ce0e-4232-9a65-65b9336b2cec"'
		}

		response = requests.request("POST", request_url, headers=headers, data = payload,verify = False)
		#print(response.text.encode('utf8'))
		data = response.json()
		#回傳驗證碼
		return data['data']

#添加白名單API
def White_List_API(self,random_phone):
	if(package_name == 'com.szoc.zb.cs'):
		request_url = "http://mis.will68.com/whitelists/edit"
		payload = "{\"status\": 1, \"phone\": \""+random_phone+"\"}"
		headers = {
		  'Cookie': '_ga=GA1.1.280281216.1603264849; _ga_DR6HQD5SM3=GS1.1.1604370924.4.0.1604370929.0; lang_type=0; JSESSIONID=C3883C50852D325D183B1E41F2DC8EF3; cf88_id="user:1:e7b99c9d-3916-461a-8d2d-975f7eeb18d7"',
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", request_url, headers=headers, data = payload)
		data = response.json()
		print('添加白名單結果為:',data['msg'])
	else:
		request_url = "https://office.cf139.com/whitelists/edit"
		seconds = str(int(time.time()))
		#payload = "{\"status\":1,\"remark\":\"YoYo-自動測試\",\"phone\":\""+random_phone+"\"}"
		payload = "{\"phone\":\""+random_phone+"\",\"createTime\":1608542350760,\"ip\":\"\",\"updateTime\":"+seconds+",\"remark\":\"YoYo-自動測試\",\"id\":1593,\"idNumber\":\"\",\"email\":\"\",\"status\":1}"
		headers = {
		  'authority': 'office.cf139.com',
		  'accept': 'application/json, text/plain, */*',
		  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
		  'content-type': 'application/json;charset=UTF-8',
		  'origin': 'https://office.cf139.com',
		  'sec-fetch-site': 'same-origin',
		  'sec-fetch-mode': 'cors',
		  'sec-fetch-dest': 'empty',
		  'referer': 'https://office.cf139.com/home/whitelist/index',
		  'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
		  'cookie': 'JSESSIONID=B9F4F676CC7B8728FF5EB497C6CA6FF1; cf88_id="user:763:99919735-b166-41db-bc21-fdd84d0c6734"; lang_type=0'
		}

		response = requests.request("POST", request_url, headers=headers, data = payload.encode("utf-8").decode("latin1"),verify = False)
		#print(response.text.encode('utf8'))
		data = response.json()
		#回傳驗證碼
		return data['data']
#登入
def Login(self):
	try:
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
	except NoSuchElementException:
		print('已登入...\n')
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


def check_new_account_login(self,account_type,password,random_phone):
	#當前時間
	current_time = datetime.now().isoformat()
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
			#寫入[帳號,手機,密碼,真實/模擬,帳戶等級,當前時間,包名]
			account_information = [account_num,random_phone,password,account_type,account_lvl,current_time,package_name]
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
			#寫入[帳號,手機,密碼,真實/模擬,帳戶等級,當前時間,包名]
			account_information = [account_num,random_phone,password,account_type,'',current_time,package_name]
			writed_csv.append(account_information)
			#寫入CSV
			writer.writerows(writed_csv)


