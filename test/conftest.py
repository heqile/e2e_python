from test_data.globals import GLOBAL_VARIABLES
from selenium import webdriver
import pytest


@pytest.fixture(scope="session", autouse=True)
def initialize_test_session():
    print("before session")
    GLOBAL_VARIABLES.initialize_test_session("PROD")


@pytest.fixture(scope="module", autouse=True)
def initialize_test_module(request):
    print("before module")
    site = getattr(request.module, "site")
    GLOBAL_VARIABLES.initialize_test_module(site)


@pytest.fixture(scope="module", autouse=True)
def web_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    def close_driver():
        driver.close()
    request.addfinalizer(close_driver)
    return driver
