from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.get("http://baidu.com")
driver.set_window_size(600,800)
driver.find_element_by_id("kw").send_keys("姬越")
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys("周时韫")
qqq=driver.find_element_by_id("su")
ActionChains(driver).context_click(qqq).perform() #右键
# ActionChains(driver).double_click(qqq).perform() #双击
driver.find_element_by_id("su").click()
driver.maximize_window()
time.sleep(3)
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
#将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
driver.quit()
