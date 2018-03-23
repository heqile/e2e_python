from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __init__(self, locator):
        self.locator = locator

    def __set__(self, instance, value):
        driver = instance.driver
        element = WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator)
        )
        element.clear()
        element.send_keys(value)

    def __get__(self, instance, owner):
        driver = instance.driver
        element = WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(*self.locator)
        )
        return element
