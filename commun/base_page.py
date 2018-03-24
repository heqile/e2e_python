from selenium.webdriver.common.action_chains import ActionChains
from test_data.globals import GLOBAL_VARIABLES


class BasePage(object):

    # key value in .json files
    page_name = ""

    def __init__(self, driver, site=None):
        self.driver = driver
        self.action_chain = ActionChains(driver)
        if site is not None:
            self.site = site
        else:
            self.site = GLOBAL_VARIABLES.SITE

        self.url = GLOBAL_VARIABLES.SESSION_HOST_DATA[self.site]["host"] + GLOBAL_VARIABLES.SESSION_PAGE_DATA[self.site][self.page_name]["path"]
        self.initialize_page_elements()

    def is_current_page(self):
        return self.driver.current_url == self.url

    def get(self):
        self.driver.get(self.url)

    def get_url(self):
        return self.url

    def initialize_page_elements(self):
        pass

    def _element_locator(self, locator_key):
        return GLOBAL_VARIABLES.SESSION_PAGE_DATA[self.site][self.page_name]["locators"][locator_key]
