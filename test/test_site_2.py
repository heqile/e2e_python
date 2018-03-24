from page.login_page import LoginPage
import pytest

# site_key is the same value in .json files
site = "CIC"


def test_login(web_driver):
    login_page = LoginPage(web_driver)
    login_page.get()
    login_page.set_login_password()
    assert login_page.is_current_page()

