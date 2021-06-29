#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8



from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import keyboard
class browsertesting:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def searchwithkeywords(self):
        time.sleep(5)
        self.driver.get("https://presearch.org")
        time.sleep(10)
        search_data=self.driver.find_element(By.XPATH, "//*[@id='search']")
        search_data.clear()
        time.sleep(5)
        search_data.send_keys("income")
        time.sleep(5)
        search_data.send_keys(Keys.ENTER)
        time.sleep(5)
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        action = ActionChains(self.driver)
        time.sleep(8)
        elem=self.driver.find_element_by_link_text('Income - Wikipedia')
        time.sleep(4)
        self.driver.execute_script("window")
        action \
            .move_to_element(elem) \
            .key_down(Keys.SHIFT) \
            .click(elem) \
            .key_up(Keys.SHIFT) \
            .perform()

        elem.send_keys(Keys.CONTROL+'w')
        print("close the tab")




if __name__ == '__main__':
    cob=browsertesting()
    cob.searchwithkeywords()