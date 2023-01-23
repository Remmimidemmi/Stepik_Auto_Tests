import pytest
from selenium.webdriver.common.by import By
from .PageObject.main_page import MainPage
from .PageObject.base_page import BasePage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
