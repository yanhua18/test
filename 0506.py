from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://baidu.com")
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.quit()