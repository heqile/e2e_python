from commun.e2e_test_case import E2ETestCase
from page.etudier_page import EtudierPage
from page.login_page import LoginPage
import unittest


class SiteTest(E2ETestCase):

    # def test_etudier_menu(self):
    #     driver = self.webdriver
    #     login_page = LoginPage(driver)
    #     etudier_page = EtudierPage(driver)
    #
    #     login_page.get()
    #     login_page.click_etudier_entry()
    #
    #     self.assertTrue(etudier_page.is_current_page())

    def test_login(self):
        driver =self.webdriver
        login_page = LoginPage(driver)
        login_page.get()
        self.assertTrue(login_page.is_current_page())


if __name__ == "__main__":
    unittest.main()

