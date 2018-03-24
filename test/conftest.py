from test_data.globals import GLOBAL_VARIABLES
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    """Parse pytest arguments"""
    parser.addoption("--environment", action="store", default="PROD")
    parser.addoption("--site", action="store", default="")
    parser.addoption("--debug_mode", action="store_true", default=True)


@pytest.fixture(scope="session", autouse=True)
def initialize_test_session(request):
    """Initialize test data before all tests"""
    GLOBAL_VARIABLES.initialize_test_session(request.config.option.environment, request.config.option.debug_mode)
    print("Test for world : {environment}".format(environment=request.config.option.environment))


@pytest.fixture(scope="module", autouse=True)
def initialize_test_module(request):
    """Initialize test data before current test module"""
    site = request.module.site
    GLOBAL_VARIABLES.initialize_test_module(site)
    enable_sites = request.config.option.site.split()
    # enable/disable test
    if len(enable_sites) != 0 and site not in enable_sites:
        pytest.skip("Tests disabled for site : {site} ".format(site=site))
    else:
        print("Tests start for site : {site} ".format(site=site))


@pytest.fixture(scope="module", autouse=True)
def web_driver(request):
    """Create webdriver instance which used for current test module"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    def close_driver():
        driver.close()
    request.addfinalizer(close_driver)
    return driver
