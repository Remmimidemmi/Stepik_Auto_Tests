import pytest
from .PageObject.login_page import LoginPage
from .PageObject.main_page import MainPage
from .PageObject.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    enter_code = MainPage(browser, browser.current_url)
    enter_code.solve_quiz_and_get_code()