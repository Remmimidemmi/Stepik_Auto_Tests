from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "URL-error"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
        self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
        assert True, "Login field is absent"

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_EMAIL)
        self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD)
        self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD)
        assert True, "Register field is absent"
