from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_class_name("form-control.first")
input1.send_keys("Helen")
input2 = browser.find_element_by_xpath("//input[@placeholder = 'Введите фамилию']")
input2.send_keys("Sydorchenko")
input3 = browser.find_element_by_class_name("form-control.third")
input3.send_keys("example@gmail.com")
#input4 = browser.find_element_by_id("country")
time.sleep(5)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(5)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_id("mat-error-0")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "This field may not be blank." == welcome_text