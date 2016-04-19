# coding=utf-8
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase



class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()




    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.browser.set_window_size(1024, 768)
        time.sleep(2)
        # 她看到输入框完美地居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        time.sleep(2)
        self.assertAlmostEqual(
                 inputbox.location['x'] + inputbox.size['width'] / 2,
                 512,
                 delta=5
        )


#if __name__ == '__main__':
#    unittest.main(warnings='ignore')
