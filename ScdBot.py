from selenium import webdriver
from time import sleep

from secrets import username, password

class ScdBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://fb.com')

        sleep(3)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_btn.click()

        # switch to login popup
        

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pswd_btn = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pswd_btn.click()

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        #base_window = self.driver.window_handles[0]
        #self.driver.switch_to_window(self.driver.window_handles[1])
        #self.driver.switch_to_window(base_window)

        sleep(8)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="navItem_540532886458224"]/a/div[2]')
        popup_1.click()

       # popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        #popup_2.click()

bot = ScdBot()
bot.login()