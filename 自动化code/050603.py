from selenium import webdriver
import time
import os
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('../html_file/frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("周时韫")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()
