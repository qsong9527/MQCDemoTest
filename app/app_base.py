# -*- coding: utf-8 -*-

import time

WAIT_FOR = 5


class AppBase(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, target_id):
        time.sleep(WAIT_FOR)
        return self.driver.find_element_by_id(target_id)
