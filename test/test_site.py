from page.etudier_page import EtudierPage
from page.login_page import LoginPage
import pytest

# site_key is the same value in .json files
site = "CM"


def test_login(web_driver):
    login_page = LoginPage(web_driver)
    login_page.get()
    assert login_page.is_current_page()
#
#
# def test_etudier_menu(web_driver):
#     login_page = LoginPage(web_driver)
#     etudier_page = EtudierPage(web_driver)
#
#     login_page.get()
#     login_page.set_login_password()
#     login_page.click_etudier_entry()
#
#     assert etudier_page.is_current_page()
#
#
# def test_click_contact_button(web_driver):
#     etudier_page = EtudierPage(web_driver)
#
#     etudier_page.get()
#     etudier_page.click_contact_button_1()


