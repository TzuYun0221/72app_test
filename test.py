# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time, os
from Parameter import *
import coverage
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

# source指定的是待測程式所在資料夾名稱
# cov = coverage.coverage(config_file=True)
cov = coverage.coverage()
cov.start()

#檢查app是否安裝,若沒安裝則會自行安裝(Parameter)
check_app_installed()


#讀取testcase路徑
if (desired_caps['platformName'] == 'Android'):
    testcase_path = ".//testcase/Android"
else:
    testcase_path = ".//testcase/ios"

def creat_suite():
    uit = unittest.TestSuite()
    #discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    #discover = unittest.defaultTestLoader.discover(specific_testcase_path, pattern="test_*.py")
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_3_5*.py")

    for test_suite in discover:
        print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())

if (desired_caps['platformName'] == 'Android'):
    if not os.path.exists('report/Android'):  os.makedirs('report/Android')
    reports_address = "report/Android/"
    report_path = "report/Android/" + now + ".html"
else:
    if not os.path.exists('report/ios'):  os.makedirs('report/ios')
    reports_address = "report/ios/"
    report_path = "report/ios/" + now + ".html"

suite = creat_suite()
file_results = open(report_path, "wb")
enviroments = u"  執行環境:"+OS+" "+"裝置:"+desired_caps['deviceName']+" "+"版本:"+desired_caps['platformName']+" "+desired_caps['platformVersion']
runner = HTMLTestRunner.HTMLTestRunner(stream=file_results, title=u"72app",description=enviroments, verbosity=2)
# verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。
runner.run(suite)
file_results.close()
