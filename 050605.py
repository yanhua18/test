from selenium import webdriver
import time,os
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('html_file/drop_down.html')
driver.get(file_path)
time.sleep(3)
m=driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("/html/body/select/option[3]").click()
time.sleep(3)
driver.quit()