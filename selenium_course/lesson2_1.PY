from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_id("treasure")
x = option1.get_attribute("valuex")
y = calc(x)
inputx = browser.find_element_by_id("answer")
inputx.send_keys(y)
input1 = browser.find_element_by_id("robotCheckbox")
input1.click()
input2 = browser.find_element_by_css_selector("[value='robots']")
input2.click()
time.sleep(3)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()
robotsRule

time.sleep(5)

