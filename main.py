# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase
from appium import webdriver

import desired_capabilities

from app.login_act import LoginAct

from utils.android_helper import AndroidHelper
from utils.log_helper import Logger


class MQCDemoTester(TestCase):

    global automationName

    def setUp(self):

        desired_caps = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        self.automationName = desired_caps.get('automationName')
        self.driver = webdriver.Remote(uri, desired_caps)

    def test_login(self):

        email = 'qsong@thoughtworks.com'
        password = 'Qa123456'

        LoginAct(self.driver).sign_in(email, password)
        device_log = AndroidHelper.get_devices_log(self.driver)
        Logger.d("Device Log => %s " % device_log)

        assert len(device_log) > 0, \
            'Found device log error!'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
