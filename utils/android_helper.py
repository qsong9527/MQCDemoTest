# -*- coding: utf-8 -*-


class AndroidHelper(object):

    @classmethod
    def get_devices_log(cls, driver):
        return driver.get_log('logcat')
