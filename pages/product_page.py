from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_has_added(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_HAS_ADDED), "Message that product has added to basket is not presented"

    def should_name_in_basket_equal_product_name(self):
        product_name_from_card = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_FROM_CARD)
        assert product_name_from_card is not None, "Product name in product card does not exist"
        product_name_from_message = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_FROM_HAS_ADDED_MESSAGE)
        assert product_name_from_message is not None, "Product name in basket message does no exist"
        assert product_name_from_card == product_name_from_message, "Product name has added to basket does not equal product name from product card"

    def should_be_basket_total_cost(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL_COST), "Message about basket total cost is not presented"

    def should_basket_total_cost_equal_product_price(self):
        product_price_from_card = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_FROM_CARD)
        assert product_price_from_card is not None, "Price in product card does not exist"
        product_price_from_message = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_FROM_MESSAGE_TOTAL_COST)
        assert product_price_from_message is not None, "Total basket cost does not exist"
        assert product_price_from_card == product_price_from_message, "Total basket cost does not equal product price from product card"
