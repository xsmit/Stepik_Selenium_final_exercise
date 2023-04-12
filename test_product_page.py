import time
import pytest
from .pages.product_page import ProductPage


# Запуск: pytest -s test_product_page.py


# @pytest.mark.parametrize('link',
#                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                           pytest.param(
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                               marks=pytest.mark.xfail(
#                                   reason="Product in basket does not equal product name from product card")),
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_has_added()
    page.should_name_in_basket_equal_product_name()
    page.should_be_basket_total_cost()
    page.should_basket_total_cost_equal_product_price()

    time.sleep(5)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_disappeared()
