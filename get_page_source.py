from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Edge('msedgedriver.exe')

browser.get('http://www.youtube.com')
time.sleep(10)
# print(browser.page_source())
time.sleep(2)