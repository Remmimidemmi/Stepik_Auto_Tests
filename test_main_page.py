import pytest

from .PageObject.main_page import MainPage
from .PageObject.login_page import LoginPage


@pytest.mark.go_login
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    page = MainPage(browser)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()


@pytest.mark.should_login_link
def test_guest_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    browser.get(link)
    page = MainPage(browser)
    page.open()
    page.should_be_login_link()


@pytest.mark.should_register_form
def test_guest_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    browser.get(link)
    page = LoginPage(browser)
    page.open()
    page.should_be_register_form()


@pytest.mark.should_login_form
def test_guest_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    browser.get(link)
    page = LoginPage(browser)
    page.open()
    page.should_be_login_form()


@pytest.mark.should_url
def test_guest_should_be_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    browser.get(link)
    page = LoginPage(browser)
    page.open()
    page.should_be_login_url()
