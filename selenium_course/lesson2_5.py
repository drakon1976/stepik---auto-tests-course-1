from selenium import webdriver
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Helen")

input2 = browser.find_element_by_name("lastname")
input2.send_keys("Sydorchenko")

input3 = browser.find_element_by_name("email")
input3.send_keys("lem@gmail.com")

input4 = browser.find_element_by_id("file")
input4.send_keys("C://Users/Base/environments/lesson5_step4.txt")    # получаем путь к директории текущего исполняемого файла 

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()

time.sleep(5)


