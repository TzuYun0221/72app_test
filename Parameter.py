# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from random import Random
import unittest, time, re, os
random = Random()
# 指定OS
OS = 'Windows'
#指定apk路徑
apk_url = 'C:/Users/Angela/72apptest/1027-uat-cs-1.8.3-release.apk'
#應用名稱&版本號(用於關於我們檢查)
app_name_expect = 'ISTONE'
app_version_expect = 'V_1.8.3'

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
    #'newCommandTimeout':6000,
    'noReset':True
}
#每次開啟重置app
desired_caps_reset = {
    'platformName':desired_caps['platformName'],
    'platformVersion':desired_caps['platformVersion'],
    'deviceName':desired_caps['deviceName'],
    'appPackage':desired_caps['appPackage'],
    'appActivity':desired_caps['appActivity'],
    #'newCommandTimeout':desired_caps['newCommandTimeout'],
    'noReset':False
}
desired_install = {
    'platformName':desired_caps['platformName'],
    'platformVersion':desired_caps['platformVersion'],
    'deviceName':desired_caps['deviceName'],
}
Remote_url = 'http://localhost:4723/wd/hub'
#檢查app是否安裝,若沒安裝則自動安裝
def check_app_installed(self):
	driver_install = webdriver.Remote(Remote_url, desired_install)
	if(driver_install.is_app_installed(desired_caps['appPackage'])):
		print('APP已經安裝')
	else:
		driver_install.install_app(apk_url)
		print('APP安裝完畢')
	driver_install.quit()
#跳過廣告
def skip_ads(self):
	#1.跳過開屏廣告 2.關版本升級 3.關彈窗廣告
	#沒有彈出版本升級或廣告就跳過不執行
	element_list = ['com.szoc.zb.cs:id/tv_skip','com.szoc.zb.cs:id/btn_cancel','com.szoc.zb.cs:id/close_btn']
	for element in element_list:
		try:
			self.driver.find_element_by_id(element).click()
		except NoSuchElementException:
			continue



