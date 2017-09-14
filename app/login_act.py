# -*- coding: utf-8 -*-

from app.app_base import AppBase

from utils.log_helper import Logger


class LoginAct(AppBase):

    @property
    def et_email(self):
        return self.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/email')

    @property
    def et_password(self):
        return self.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/password')

    @property
    def bt_sign_in(self):
        return self.find_element_by_id('com.thoughtworks.qsong.mqcdemo:id/email_sign_in_button')

    def enter_email(self, email):
        Logger.d("Enter email with text => %s" % email)
        self.et_email.send_keys(email)

    def enter_password(self, password):
        Logger.d("Enter password with text => %s" % password)
        self.et_password.send_keys(password)

    def click_sign_in(self):
        Logger.d("Click button sign in")
        self.bt_sign_in.click()

    def sign_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()
