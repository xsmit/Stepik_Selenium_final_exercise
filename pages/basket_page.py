from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_IN_BASKET), "There are products in the basket"
