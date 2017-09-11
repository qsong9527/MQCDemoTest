# -*- coding: utf-8 -*-


class AppBase(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def devices_log(self):
        return self.driver.get_log('logcat')


class LoginAct(AppBase):

    @property
    def et_email(self):
        return self.driver.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/email')

    @property
    def et_password(self):
        return self.driver.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/password')

    @property
    def bt_sign_in(self):
        return self.driver.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/email_sign_in_button')
