from selenium import webdriver 
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_id("num1")
a = option1.text
option2 = browser.find_element_by_css_selector("span:nth-child(4)")
b = option2.text
def calc(a,b):
  return str(int(a)+int(b))
sum = calc(a,b)
select = webdriver.support.ui.Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum)

button = browser.find_element_by_css_selector("button.btn")
button.click()

