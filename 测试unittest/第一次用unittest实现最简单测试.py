# -*- coding:utf-8 -*-
import unittest
import time
from appium import webdriver


class MyTest(unittest.TestCase):

    def setUp(self):
        """
            初始化，设置测试机,打开app
        :return:
        """
        print('----MyTest setUp----')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.ule.scan'
        desired_caps['appActivity'] = 'com.ule.scan.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        print('----MyTest tearDown----')

    def testMy(self):
        print('----MyTest testMy----')
        self.driver.quit()
        pass

    def test_webgum(self):
        print(self.driver.current_activity)
        print('----testWebgum start----')
        el = self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "webgum")]')
        el.click()
        self.driver.wait_activity()
        print(self.driver.current_activity)
        print('----testWebgum end----')
        pass


def f1():
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


def f2():
    help(webdriver)


def main():
    f1()
    # f2()
    pass


if __name__ == '__main__':
    main()
