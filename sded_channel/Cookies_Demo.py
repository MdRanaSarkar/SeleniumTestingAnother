from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.amazon.com/")
#find all cookies from browser of any websites
cookies=driver.get_cookies()
#showing the lenght of the cookies
print(len(cookies))

#showing the all cookies of the browser

print(cookies)

#adding new cookies into existing cookies

cookie={'name':'rana','value':'12323'}
cookies=driver.add_cookie(cookie)
#get all cookies after adding the cookies
cookies=driver.get_cookies()
#showing the lenght of the cookies
print(len(cookies))

#showing the all cookies of the browser

print(cookies)

#now delete cookies

driver.delete_cookie('rana')


#get all cookies after adding the cookies
cookies=driver.get_cookies()
#showing the lenght of the cookies
print(len(cookies))

#showing the all cookies of the browser

print(cookies)
