from commun.base_page import BasePage
from commun.base_page_element import BasePageElement
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMPRUNTER_MENU = (By.LINK_TEXT, "Emprunter")
    ETUDIER_ENTRY = (By.PARTIAL_LINK_TEXT, "tudier en France et")


class LoginPage(BasePage):
    url = "https://www.creditmutuel.fr/fr/authentification.html"
    emprunter_menu = BasePageElement(LoginPageLocators.EMPRUNTER_MENU)
    etudier_entry = BasePageElement(LoginPageLocators.ETUDIER_ENTRY)

    def click_etudier_entry(self):
        self.action_chain.move_to_element(self.emprunter_menu).perform()
        self.action_chain.move_to_element(self.etudier_entry).perform()
        self.action_chain.click().perform()
