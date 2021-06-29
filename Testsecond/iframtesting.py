import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../drivernext/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.redbus.in/")
time.sleep(5)
driver.find_element(By.XPATH,"//i[contains(@id,'profile')]").click()

driver.find_element(By.XPATH,"//li[contains(@id,'signInLink')]").click()

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
time.sleep(10)
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
driver.switch_to.parent_frame()