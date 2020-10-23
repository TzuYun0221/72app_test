import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None
    
    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'c6eaadad'
        self.dc['appPackage'] = 'com.szoc.zb.cs'
        self.dc['appActivity'] = 'gw.com.android.ui.WelcomeActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def testUntitled(self):
        // self.driver.swipe(767, 1721, 0, 1810, 336)
        // self.driver.swipe(967, 1524, 0, 1589, 272)
        // self.driver.swipe(853, 1446, 242, 1417, 255)
        // self.driver.find_element_by_xpath("xpath=//*[@text='立即体验']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='iv_tutorial_map']").click()
        // WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='问答教学']')))
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='问答教学']')))
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='问答教学']')))
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='教学视频']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='问答教学']").click()
        // WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@text='跳过']')))
        // self.driver.find_element_by_xpath("xpath=//*[@text='跳过']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='btn_cancel']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='以后再说']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='radio_button' and (./preceding-sibling::* | ./following-sibling::*)[@text='我的']]").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='更多功能尽在登录后']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='loginnameEditText']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='8']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='1']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='key_pos_number_line4_2']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='1']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='key_pos_number_line3_2']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='key_pos_number_line1_3']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='key_pos_number_line1_2']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='key_pos_number_line1_2']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='password']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='label' and ./parent::*[@id='host' and ./parent::*[./parent::*[@id='key_pos_1_0']]]]").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='label' and ./parent::*[@id='key_pos_2_5']]").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='label' and ./parent::*[@id='key_pos_2_3']]").click()
        // self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.FrameLayout' and ./*[@text='1']]").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='2']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='3']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='登　录']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@id='btn_cancel']").click()
        // self.driver.find_element_by_xpath("xpath=//*[@text='以后再说']").click()

    def tearDown(self):
        self.driver.quit()
        
    if __name__ == '__main__':
        unittest.main()
