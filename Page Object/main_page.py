from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link: WebElement = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
