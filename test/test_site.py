from page.etudier_page import EtudierPage
from page.login_page import LoginPage
import commun.log_helper as log

# site_key is the same value in .json files
site = "CM"


def test_login(selenium):
    login_page = LoginPage(selenium)
    login_page.get()
    assert login_page.is_current_page()


def test_etudier_menu(selenium):
    log.set_up_log_list()
    login_page = LoginPage(selenium)
    etudier_page = EtudierPage(selenium)

    login_page.get()
    login_page.set_login_password()
    log.add_log_point("set login", selenium)
    login_page.click_etudier_entry()
    log.add_log_point("click etudier entry", selenium)

    assert etudier_page.is_current_page()


def test_click_contact_button(selenium):
    log.set_up_log_list()
    etudier_page = EtudierPage(selenium)

    etudier_page.get()
    etudier_page.click_contact_button_1()
    log.add_log_point("click contact button", selenium)
