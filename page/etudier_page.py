from commun.base_page import BasePage
from commun.base_page_element import BasePageElement
from selenium.webdriver.common.by import By


class EtudierPageLocators(object):
    CONTACT_BUTTON_1 = (By.ID, "bt-hb0")


class EtudierPage(BasePage):
    page_name = "EtudierPage"
    # url = "https://www.creditmutuel.fr/fr/particuliers/emprunter/financer-vos-etudes.html"

    def click_etudier_entry(self):
        self.action_chain.move_to_element(self.emprunter_menu).perform()
        self.action_chain.move_to_element(self.etudier_entry).perform()
        self.action_chain.click().perform()
