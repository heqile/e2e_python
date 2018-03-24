from commun.base_page import BasePage
from commun.base_page_element import BasePageElement


class LoginPage(BasePage):

    page_name = "LoginPage"
    emprunter_menu = None
    etudier_entry = None
    login_input = None
    password_input = None

    def _initialize_page_elements(self):
        """"reload method"""
        # locator_key is the same value in .json files
        self.emprunter_menu = BasePageElement(self.driver, self._element_locator(locator_key="emprunter_menu"))
        self.etudier_entry = BasePageElement(self.driver, self._element_locator(locator_key="etudier_entry"))
        self.login_input = BasePageElement(self.driver, self._element_locator(locator_key="login_input"))
        self.password_input = BasePageElement(self.driver, self._element_locator(locator_key="password_input"))

    def click_etudier_entry(self):
        self.action_chain.move_to_element(self.emprunter_menu.get_element()).perform()
        self.action_chain.move_to_element(self.etudier_entry.get_element()).perform()
        self.action_chain.click().perform()

    def set_login_password(self):
        self.login_input.set_value(self.user_data["login"])
        self.password_input.set_value(self.user_data["password"])
