import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL for login page does not contain word 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_element = self.get_element(*LoginPageLocators.REGISTER_EMAIL)
        assert email_element is not None, 'No "Email address" field on registration form'
        password1_element = self.get_element(*LoginPageLocators.REGISTER_PASSWORD1)
        assert password1_element is not None, 'No "Password" field on registration form'
        password2_element = self.get_element(*LoginPageLocators.REGISTER_PASSWORD2)
        assert password2_element is not None, 'No "Confirm password" field on registration form'
        button_register = self.get_element(*LoginPageLocators.REGISTER_BUTTON)
        assert button_register is not None, 'No "Register" button on registration form'

        email_element.send_keys(email)
        password1_element.send_keys(password)
        password2_element.send_keys(password)
        button_register.click()
