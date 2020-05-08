from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.set_window_size(600,800)
#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys("webdriver")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()





















# driver=webdriver.Firefox()
# driver.get("http://baidu.com")
# time.sleep(2)
# print(driver.title)
# print(driver.current_url)
# driver.quit()