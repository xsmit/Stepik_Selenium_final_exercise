import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# Запуск: pytest -v --tb=line --language=en test_main_page.py


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # Пример фикстуры для задания начальных условий перед запуском каждого теста,
    # и очистки данных после выполнения теста
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
    #     self.product = ProductFactory(title="Best book created by robot")
    #     # создаем по апи
    #     self.link = self.product.link
    #     yield
    #     # после этого ключевого слова начинается teardown
    #     # выполнится после каждого теста в классе
    #     # удаляем те данные, которые мы создали
    #     self.product.delete()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(5)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        time.sleep(5)


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(5)


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(5)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_message_about_empty_basket()
    time.sleep(5)
