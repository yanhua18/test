from selenium import webdriver
import time

from selenium.webdriver.firefox.webdriver import WebDriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='kw']").send_keys("抗击肺炎")
driver.find_element_by_xpath("//*[@id='su']").click()
# driver.find_element_by_class_name("s_ipt").send_keys("假偶天成")
# driver.find_element_by_class_name("btn self-btn bg s_btn btn_h btnhover").click()
# driver.find_element_by_name("wd").send_keys("大鱼海棠")
# driver.find_element_by_id("kw").send_keys("虞书欣")
# driver.find_element_by_id("su").click()

time.sleep(6)
driver.quit()