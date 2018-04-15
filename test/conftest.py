from test_data.globals import GLOBAL_VARIABLES
import pytest, pytest_html
import chromedriver_binary


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


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--start-maximized')
    return chrome_options


def pytest_selenium_runtest_makereport(item, report, summary, extra):
    # update report.sections, add screenshot, disable default screenshot option,
    # remove summary to avoid pytest-selenium add summary again
    # no., desciption, url, screenshot, (html?)

    for item in GLOBAL_VARIABLES.LOG_ASSETS :
        description = item.description
        log = ''
        if item.error != '':
            log = item.error
        else:
            log = 'url: {url} \nhtml: {html}\n' .format(url=item.url, html=item.html)
            if item.screenshot:
                extra.append(pytest_html.extras.image(item.screenshot, description))
        report.sections.append((description, log))
