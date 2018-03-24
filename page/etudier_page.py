from commun.base_page import BasePage
from commun.base_page_element import BasePageElement


class EtudierPage(BasePage):
    page_name = "EtudierPage"
    contact_button_1 = None

    def initialize_page_elements(self):
        # locator_key is the same value in .json files
        self.contact_button_1 = BasePageElement(self.driver, self._element_locator(locator_key="contact_button_1"))

    def click_contact_button_1(self):
        self.action_chain.move_to_element(self.contact_button_1.get_element()).perform()
        self.action_chain.click().perform()
