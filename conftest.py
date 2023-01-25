import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


#def pytest_addoption(parser):
#    parser.addoption('--language', action='store', default='en',
#                     help="Choose language: 'en', 'fr', 'ru'")


#@pytest.fixture(scope="function")
#def language_chs(request, browser):
#    language = request.config.getoption("language")
#    if language == 'en':
#        link_en = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
#        yield browser.get(link_en)
#    elif language == 'fr':
#        link_fr = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
#        yield browser.get(link_fr)
#    elif language == 'ru':
#        link_ru = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#        yield browser.get(link_ru)
#    else:
#        raise pytest.UsageError("--language should be: 'en', 'fr', or 'ru'")

