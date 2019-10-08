from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
a = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_link_text(a)
time.sleep(5)
link.click()


input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Helen")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Sydorchenko")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Zp")
input4 = browser.find_element_by_id("country")
input4.send_keys("UK")
button = browser.find_element_by_css_selector("button.btn")
button.click()