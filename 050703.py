from selenium import webdriver
import os,time
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('html_file/upload.html')
driver.get(file_path)

driver.find_element_by_xpath('/html/body/div/div/input').send_keys('D:/图管会/图管会/《极花》读后感.docx')
time.sleep(2)
driver.quit()