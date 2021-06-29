from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://selenium.dev")

cur_url=driver.current_url
print(cur_url)
driver.back()
print(driver.current_url)
driver.forward()
driver.switch_to.new_window('tab')
print(driver.current_url)

