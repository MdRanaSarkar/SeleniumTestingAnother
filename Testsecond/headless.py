import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
opt=Options()
opt.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
driver.get("http//www.google.com")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Rana")


driver.close()
driver.quit()
