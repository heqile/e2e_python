from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.action_chain = ActionChains(driver)

    def is_current_page(self):
        return self.driver.current_url == self.url

    def get(self):
        self.driver.get(self.url)
