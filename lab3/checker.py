from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, string, os
def rs(N):
    return ''.join(random.choise(string.ascii_uppercase + string.digits) for _ in range(N))
driver = webdriver.GoogleChrome()
driver.get('http://localhost:5555')
elem = driver.find_element_by_id('Register_ref')
elem.click()
u, p = rs(10), rs(10)
driver.find_element_by_id('usr').send_keys(u)
driver.find_element_by_id('pwd').send_keys(u)
driver.find_element_by_id('submit_login').click()
driver.find_element_by_id('Login_ref').click()
driver.find_element_by_id('submit_login').click()
driver.find_element_by_id('userfile').send_keys(os.getcwd() + '/../Vietnam.mp4')
driver.find_element_by_id('userstart').send_keys(10)
driver.find_element_by_id('userdur').send_keys(10)
driver.find_element_by_id('sendfile').click()
time.sleep(10)
a = driver.find_element_by_css_selector('#result a')
a.click()
time.sleep(30)
driver.close()