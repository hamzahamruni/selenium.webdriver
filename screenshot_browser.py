from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Edge('msedgedriver.exe')

browser.get('http://www.youtube.com')
time.sleep(10)
browser.save_screenshot('C:\\Users\\21894\\Desktop\\test.png')
time.sleep(2)


