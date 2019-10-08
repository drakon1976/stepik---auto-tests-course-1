from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_id("input_value")
x = option1.text
y = calc(x)

#browser.execute_script("window.scrollBy(0, 150);")

inputx = browser.find_element_by_id("answer")
inputx.send_keys(y)

input1 = browser.find_element_by_id("robotCheckbox")
input1.click()

input2 = browser.find_element_by_css_selector("[value='robots']")
#or the second var
browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
input2.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn.btn-default")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)


