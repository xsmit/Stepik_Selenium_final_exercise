import time
from .pages.login_page import LoginPage

# Запуск: pytest -v --tb=line --language=en test_login_page.py


def test_login_page_is_it(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    time.sleep(5)
