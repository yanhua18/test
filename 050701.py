from selenium import webdriver
import os,time

driver=webdriver.Chrome()
driver.implicitly_wait(30)
file_path='file:///'+os.path.abspath('html_file/send.html')
driver.get(file_path)

driver.find_element_by_xpath('/html/body/input').click()
driver.switch_to.alert.send_keys('裴衍')
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()
