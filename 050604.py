from selenium import webdriver
import time
import os

from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('html_file/level_locate.html')
driver.get(file_path)

driver.find_element_by_link_text('Link1').click()
WebDriverWait(driver,10).until(lambda the_driver:
                               the_driver.find_element_by_id('dropdown1').is_displayed)
menu=driver.find_element_by_id('dropdown1').find_element_by_link_text('Action')
webdriver.ActionChains(driver).move_to_element(menu).perform()
time.sleep(4)
driver.quit()