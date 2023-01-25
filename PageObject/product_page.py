import time

from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_product(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_button.click()

    def price_check(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        text_product_price = product_price.text
        text_message_price = message_price.text
        assert text_product_price == text_message_price, "INCORRECT PRICE!!!"
        print("Correct PRICE!!!!!!!!!!!!!!!!!!!!!")

    def add_to_cart_check(self):
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text_product_name = product_name.text
        text_message_product_name = message_product_name.text
        assert text_message_product_name == text_product_name, "INCORRECT PRODUCT!!!"
        print(f"Correct product '{text_product_name}' add to cart!!!!")

    # def should_not_be_success_message(self):
    #     assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

