from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://baidu.com")
driver.find_element_by_id("kw").send_keys("顾昀")
driver.find_element_by_id("su").click()
time.sleep(3)

js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

driver.quit()












# driver=webdriver.Firefox()
# first_url='http://www.baidu.com'
# print("now acess %s" %(first_url))
# driver.get(first_url)
# driver.implicitly_wait(10)
# second_url='http://news.baidu.com'
# print("now acess %s" %(second_url))
# driver.get(second_url)
# driver.implicitly_wait(10)
# print("back to %s"%(first_url))
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.quit()


# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com/")
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("抗击肺炎")
# driver.find_element_by_xpath("//*[@id='su']").click()
# driver.find_element_by_class_name("s_ipt").send_keys("假偶天成")
# driver.find_element_by_class_name("btn self-btn bg s_btn btn_h btnhover").click()
# driver.find_element_by_name("wd").send_keys("大鱼海棠")
# driver.find_element_by_id("kw").send_keys("虞书欣")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.quit()