from selenium import webdriver
import os,time

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('../html_file/modal.html')
driver.get(file_path)

driver.find_element_by_xpath('//*[@id="show_modal"]').click()
time.sleep(4)
link=driver.find_element_by_xpath('//*[@id="myModal"]/div[2]').find_element_by_xpath('//*[@id="click"]')
link.click()
time.sleep(3)
button=driver.find_element_by_class_name('modal-footer').find_element_by_xpath('//*[@id="myModal"]/div[3]/button[1]')
button.click()
time.sleep(3)
driver.quit()
