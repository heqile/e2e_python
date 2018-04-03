from selenium.webdriver.common.action_chains import ActionChains
from test_data.globals import GLOBAL_VARIABLES


class BasePage(object):

    # key value should be same to .json files
    page_name = ""

    def __init__(self, driver, site=None):
        self.driver = driver
        self.action_chain = ActionChains(driver)
        if site is not None:
            # if specify to create a page for one site in constructor
            self.site = site
        else:
            self.site = GLOBAL_VARIABLES.SITE

        # self.url = GLOBAL_VARIABLES.SESSION_HOST_DATA[self.site]["host"] + GLOBAL_VARIABLES.SESSION_PAGE_DATA[self.site][self.page_name]["path"]
        self.url = GLOBAL_VARIABLES.SITE_DATA.get_host() + GLOBAL_VARIABLES.SITE_DATA.get_page(self.page_name).get_path()

        # self.user_data = GLOBAL_VARIABLES.SESSION_USER_DATA[self.site]
        self.user_data = GLOBAL_VARIABLES.SITE_DATA.get_user_data()
        self._initialize_page_elements()

    def is_current_page(self):
        return self.driver.current_url == self.url

    def get(self):
        """load page"""
        self.driver.get(self.url)
        cookie_sinbar = {"name": "debug_bar", "value": "1"}
        cookie_debug = {"name": "sinbar", "value": "1"}
        if GLOBAL_VARIABLES.DEBUG_ENABLE \
                and cookie_sinbar not in self.driver.get_cookies() \
                and cookie_debug not in self.driver.get_cookies():
            self.driver.add_cookie(cookie_sinbar)
            self.driver.add_cookie(cookie_debug)
            self.driver.get(self.url)

    def _get_url(self):
        return self.url

    def _get_cookies(self):
        return self.driver.get_cookies()

    def _initialize_page_elements(self):
        """reload method"""
        pass

    def _element_locator(self, locator_key):
        try:
            from selenium.webdriver.common.by import By
            # return GLOBAL_VARIABLES.SESSION_PAGE_DATA[self.site][self.page_name]["locators"][locator_key]
            return GLOBAL_VARIABLES.SITE_DATA.get_page(self.page_name).get_locator(locator_key)
        except:
            # if locator not exist in current page
            return None

    def _add_cookie(self, cookie_name):
        # self.driver.add_cookie(GLOBAL_VARIABLES.SESSION_HOST_DATA[self.site]["cookie_list"][cookie_name])
        self.driver.add_cookie(GLOBAL_VARIABLES.SITE_DATA.get_cookie(cookie_name))
