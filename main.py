# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase
from appium import webdriver

import desired_capabilities
# import app


class MqcTest(TestCase):

    global automationName

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        uri = desired_capabilities.get_uri()
        self.automationName = desired_caps.get('automationName')
        self.driver = webdriver.Remote(uri, desired_caps)

    def test_login(self):
        # login_act = app.LoginAct()
        # login_act.et_email.send_keys('qsong@thoughtworks.com')
        # login_act.et_password.send_keys('Qa123456')
        # login_act.bt_sign_in
        # log_records = login_act.devices_log

        et_email = self.driver.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/email')
        et_email.send_keys('qsong@thoughtworks.com')

        et_password = self.driver.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/password')
        et_password.send_keys('Qa123456')

        log_records = self.driver.get_log('logcat')
        print(log_records)
        print(len(log_records))
        assert len(log_records) > 0, \
            'Get log failed.'

    # def test_pass(self):
    #     assert 1 == 1, \
    #         'Test pass case failed.'
    #
    # def test_failed(self):
    #     assert 1 == 2, \
    #         'Test fail case failed.'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
