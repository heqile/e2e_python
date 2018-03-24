from commun.e2e_test_case import E2ETestCase
from page.etudier_page import EtudierPage
from page.login_page import LoginPage
import unittest
import pytest

# site_key is the same value in .json files
site = "CM"

class SiteTest(E2ETestCase):

    @pytest.mark.second
    def test_etudier_menu(self):
        driver = self.webdriver
        login_page = LoginPage(driver)
        etudier_page = EtudierPage(driver)

        login_page.get()
        login_page.set_login_password()
        login_page.click_etudier_entry()

        self.assertTrue(etudier_page.is_current_page())

    # @pytest.mark.first
    # def test_login(self):
    #     driver =self.webdriver
    #     login_page = LoginPage(driver)
    #     login_page.get()
    #     self.assertTrue(login_page.is_current_page())

    @pytest.mark.third
    def test_click_contact_button(self):
        driver = self.webdriver
        etudier_page = EtudierPage(driver)

        etudier_page.get()
        etudier_page.click_contact_button_1()


if __name__ == "__main__":
    unittest.main()

