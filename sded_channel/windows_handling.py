import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
print(driver.current_window_handle)

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="SeleniumHQ Browser Automation":
        time.sleep(5)
        driver.close()
driver.quit()
