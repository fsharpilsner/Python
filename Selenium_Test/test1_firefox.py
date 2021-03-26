##!/usr/bin/python3.8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time


binary_location = "/usr/sbin/firefox"

cr_options = Options()
cr_options.binary_location=binary_location
cr_options.add_argument("--remote-debugging-port=4444")

driver_location = "/usr/bin/geckodriver"
cr_driver = webdriver.Firefox(executable_path=driver_location, \
    options=cr_options)

cr_driver.get('https://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


cr_driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2)")


w = WebDriverWait(cr_driver, 8)
EC.presence_of_element_located((By.XPATH, "//*[@id=\"name\"]"))


username = cr_driver.find_element_by_xpath("//*[@id=\"name\"]")
print(username)
username.send_keys("Kalle Persson")

NEXT_VALUE = '/html/body/div/div/div[3]/div[4]/div/a[1]/div[1]'
element = cr_driver.find_element_by_xpath(NEXT_VALUE)
element.click()


MODAL_VALUE= '/html/body/div/div/div[3]/div[4]/div[1]'
modal = cr_driver.find_element_by_xpath(MODAL_VALUE)
modal.screenshot("modal.png")


SIGN_VALUE= '/html/body/div/div/div[3]/div[4]/div[1]/a[1]/div'
signera = cr_driver.find_element_by_xpath(SIGN_VALUE)
signera.click()

time.sleep(10)

IS_SIGNED_VALUE = '/html/body/div/div/div[3]/div[2]/div[2]/div/div[1]/h1/span'

is_signed = cr_driver.find_element_by_xpath(IS_SIGNED_VALUE).text
print(is_signed)


#while(True):
#       pass

#cr_driver.close()







