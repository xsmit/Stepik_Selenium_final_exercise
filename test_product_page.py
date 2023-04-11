import time
from .pages.product_page import ProductPage

# Запуск: pytest -s test_product_page.py


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_has_added()
    page.should_name_in_basket_equal_product_name()
    page.should_be_basket_total_cost()
    page.should_basket_total_cost_equal_product_price()

    time.sleep(5)


