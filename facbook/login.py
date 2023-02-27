from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# msedgedriver


url = 'https://www.facebook.com/login.php'
# driver = webdriver.Edge('msedgedriver.exe')
# driver.open(url)

class facebooklogin():
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()
        #________________________________
        self.driver.get(url)
        time.sleep(3)
    #_____________________________________________________________
    def login(self):
        email_element = self.driver.find_element(By.ID,'email')
        email_element.send_keys(self.email)

        password_element = self.driver.find_element(By.ID,'pass')
        password_element.send_keys(self.password)

        login_button = self.driver.find_element(By.NAME,'login')
        login_button.click()

        time.sleep(20)

if __name__ == '__main__':
    fb_login = facebooklogin(email='Your username',password='Your password')
    fb_login.login()

   