# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from random import Random
import unittest, time, re, os
import json
random = Random()
# 指定OS
OS = 'Windows'
#指定apk路徑
apk_url = 'C:/Users/Angela/72apptest/1027-uat-cs-1.8.3-release.apk'
#應用名稱&版本號(用於關於我們檢查)
app_name_expect = 'ISTONE'
app_version_expect = 'V_1.8.3'

check_status_json = 'check_status.json'
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
    'appPackage':'com.szoc.zb.cs',
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
	element_list = ['com.szoc.zb.cs:id/tv_skip','com.szoc.zb.cs:id/btn_cancel','com.szoc.zb.cs:id/close_btn']
	for element in element_list:
		try:
			self.driver.find_element_by_id(element).click()
		except NoSuchElementException:
			continue
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
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#點擊座標
	TouchAction(self.driver).tap(element=None, x=x*0.9, y=y-1, count=1).perform()

#點擊首頁輪播廣告
def click_home_banner(self):
	time.sleep(2)
	x=self.driver.get_window_size()['width']
	y=self.driver.get_window_size()['height']
	#點擊座標
	TouchAction(self.driver).tap(element=None, x=x/2 ,y=y/5, count=1).perform()


'''#更新driver狀態(已開啟True/已關閉False)(修改json)
def update_driver_status(status_bool):
	# 檢查check_status.json是否存在
    if os.path.isfile(check_status_json):
        #存在時
        #讀取check_status.json
        with open(check_status_json, 'r', encoding='utf-8') as json_file:  
            check_status_data = json.load(json_file)
            #修改driver狀態
            check_status_data['driver_status'] = status_bool
        #再將driver狀態存入check_status.json
        with open(check_status_json, 'w') as outfile:
            json.dump(check_status_data, outfile,indent=2)
    else:
        #不存在時
        #將driver狀態check_status.json
        with open(check_status_json, 'w') as outfile:
            json.dump({'driver_status':status_bool}, outfile,indent=2)
#檢查driver狀態(已開啟True/已關閉False)(修改json)
def check_driver_status(self):
	# 檢查check_status.json是否存在
	if os.path.isfile(check_status_json):
		#存在時
		#讀取check_status.json
		with open(check_status_json, 'r', encoding='utf-8') as json_file:  
			check_status_data = json.load(json_file)
		#確認driver狀態
		#driver關閉時則開啟driver
		if(check_status_data['driver_status'] == False):
			self.driver = webdriver.Remote(Remote_url, desired_caps_reset)
			#設置隱性等待10秒
			self.driver.implicitly_wait(10)
			#跳過廣告(Parameter)
			skip_ads(self)	        
	else:
		#不存在時
		#將driver狀態check_status.json
		with open(check_status_json, 'w') as outfile:
			json.dump({'driver_status':False}, outfile,indent=2)'''

		



