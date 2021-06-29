from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.pavantestingtools.com/")

print("Main driver title",driver.title)

driver.back()
print("After back title of driver ",driver.title)

driver.forward()

print("After forward again check the title :",driver.title)