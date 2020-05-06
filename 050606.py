from selenium import webdriver
import time, os
from time import sleep

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('html_file/alert.html')
driver.get(file_path)
time.sleep(3)

driver.find_element_by_id('tooltip').click()
sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert = driver.switch_to.alert
alert.accept()
sleep(3)
driver.quit()
