﻿from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
#the first page with button
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button1 = browser.find_element_by_id("book")
button1.click()

#the page with formula
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
option1 = browser.find_element_by_id("input_value")
x = option1.text
y = calc(x)
option2 = browser.find_element_by_name("text")
option2.send_keys(y)

button2 = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()