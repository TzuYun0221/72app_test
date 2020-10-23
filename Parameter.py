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
desired_caps = {
    'platformName':'Android',
    #'platformVersion':'10',
    #'deviceName':'Mi 9T',
    'platformVersion':'5.1.1',
    'deviceName':'Android Emulator',
    'appPackage':'com.szoc.zb.cs',
    'appActivity':'gw.com.android.ui.WelcomeActivity'
}
Remote_url = 'http://localhost:4723/wd/hub'

