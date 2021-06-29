'''@author
Rana Sarkar
'''

import time
import unittest
import smtplib
import keyboard
from openpyxl import Workbook
from selenium import  webdriver
from email.message import EmailMessage
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



class Tforcetesting_all(unittest.TestCase):
    current_url=""
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\\SeleniumTestCode\\driver\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login_form(self):
        driver=self.driver
        driver.get("http://teton.tforcehrms.com/admin/")
        driver.find_element(By.NAME,"iusername").send_keys("Sarkar")
        time.sleep(4)
        driver.find_element(By.NAME,"ipassword").send_keys("123456789")
        time.sleep(4)
        driver.find_element(By.XPATH,'//*[@id="hrm-form"]/div[3]/button').submit()

        time.sleep(10)
        current_url=driver.current_url
        current_title=driver.title
        print(current_title)
        real_current_url="http://teton.tforcehrms.com/admin/dashboard?module=dashboard"
        self.assertEqual(current_url,real_current_url)

        #now check the logout function works automatically

        hoverelement=driver.find_element(By.XPATH,'//*[@id="user_avatar"]')
        acttion=ActionChains(driver)
        acttion.move_to_element(hoverelement).perform()
        time.sleep(4)
        driver.find_element(By.XPATH,'//i[@class="ion ion-ios-log-out text-primary"]').click()
        afterlgouturl=driver.current_url
        print(afterlgouturl)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
