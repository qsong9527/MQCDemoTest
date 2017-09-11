# -*- coding: utf-8 -*-


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'PBV7N16925005082',
        'appPackage': 'com.thoughtworks.qsong.mqcdemo',
        'appActivity': 'com.thoughtworks.qsong.mqcdemo.LoginActivity',
        'appWaitPackage': 'com.example.host.demo',
        'newCommandTimeout': 30,
        'automationName': 'Appium'
    }

    return desired_caps


def get_uri():
    return "http://localhost:50000/wd/hub"


def get_username():
    return "admin"


def get_password():
    return "admin"
