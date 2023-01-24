from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    #def go_to_product_page(self):

    def add_product(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_button.click()