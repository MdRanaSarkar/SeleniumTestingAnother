from selenium import webdriver

from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../drivernext/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
pw=driver.current_window_handle
print("parrent window:",pw)
sleep(5)
driver.find_element_by_xpath("//img[@alt='LinkedIn OrangeHRM group']").click()
cw=driver.window_handles

for child in cw:
    if pw!=child:
        driver.switch_to.window(child)
        sleep(5)
        driver.find_element_by_id("email-address").send_keys("rana@gmail.com")
        print(driver.title)
        sleep(10)
        driver.close()
driver.switch_to.window(pw)
sleep(5)
driver.find_element_by_name("txtUsername").send_keys("Rana")
sleep(5)
print(driver.title)

driver.close()
driver

