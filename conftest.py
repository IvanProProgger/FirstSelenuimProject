import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxProfile()
        options.set_preference("intl.accept_languages", user_language)
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox()
    else:
        print(f"{browser_name} wasn't implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()
