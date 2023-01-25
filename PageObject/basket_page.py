import pytest

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET), "Product is present, but not should"

    def negative_should_not_be_product_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET), "Product is absent like a should"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message is absent!!!"
