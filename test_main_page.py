# это лишнее
import time
from selenium.webdriver.common.by import By

# Запуск: pytest -v --tb=line --language=en test_main_page.py

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    go_to_login_page(browser)
    # это лишнее
    time.sleep(5)