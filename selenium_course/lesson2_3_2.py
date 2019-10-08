from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
#the first page with button
time.sleep(5)
button = browser.find_element_by_css_selector("button.btn").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
#the page with formula
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
option1 = browser.find_element_by_id("input_value")
x = option1.text
y = calc(x)
option2 = browser.find_element_by_name("text")
option2.send_keys(y)
button2 = browser.find_element_by_css_selector("button.btn").click()