from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def get_element(self):
        driver = self.driver
        element = WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator)
        )
        return element

    def set_value(self, value):
        driver = self.driver
        element = WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator)
        )
        element.clear()
        element.send_keys(value)

    def __set__(self, instance, value):
        driver = self.driver
        element = WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator)
        )
        element.clear()
        element.send_keys(value)

    def __get__(self, instance, owner):
        driver = self.driver
        element = WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator)
        )
        return element
