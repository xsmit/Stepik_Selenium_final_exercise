from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_HAS_ADDED = (By.CSS_SELECTOR, "#messages > .alert-success")
    PRODUCT_NAME_FROM_CARD = (By.CSS_SELECTOR, ".product_page .product_main > h1")
    PRODUCT_NAME_FROM_HAS_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner > strong")
    MESSAGE_BASKET_TOTAL_COST = (By.CSS_SELECTOR, "#messages > .alert-info")
    PRODUCT_PRICE_FROM_MESSAGE_TOTAL_COST = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p > strong")
    PRODUCT_PRICE_FROM_CARD = (By.CSS_SELECTOR, ".product_page .product_main > .price_color")


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "div.content >  #content_inner > p > a")
