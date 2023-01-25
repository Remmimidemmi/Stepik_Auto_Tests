import pytest
from .PageObject.main_page import MainPage
from .PageObject.product_page import ProductPage
from .PageObject.basket_page import BasketPage
from .PageObject.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        browser.get(link)
        page = LoginPage(browser)
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        browser.get(link)
        page = ProductPage(browser)
        page.open()
        page.add_product()
        enter_code = MainPage(browser)
        enter_code.solve_quiz_and_get_code()
        page.add_to_cart_check()
        page.price_check()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        browser.get(link)
        page = ProductPage(browser)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    browser.get(link)
    page = ProductPage(browser)
    page.open()
    page.add_product()
    enter_code = MainPage(browser)
    enter_code.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    browser.get(link)
    page = ProductPage(browser)
    page.open()
    page.add_product()
    enter_code = MainPage(browser)
    enter_code.solve_quiz_and_get_code()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    browser.get(link)
    page = MainPage(browser)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    browser.get(link)
    page = ProductPage(browser)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    browser.get(link)
    page = BasketPage(browser)
    page.open()
    page.open_basket()
    page.should_not_be_product_present()
    # page.negative_should_not_be_product_present()
    page.should_be_message_about_empty_basket()
