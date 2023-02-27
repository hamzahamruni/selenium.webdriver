from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://selenium.dev/')
time.sleep(10)

# msedgedriver
# driver = webdriver.Edge('msedgedriver.exe')
# # for this to work you must have a gekodriver.exe in the same folder 
# #where the main python file is located by doing this there is no need 
# #to specify the path
# driver.open('https://www.youtube.com/')
    

