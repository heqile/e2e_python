from page.login_page import LoginPage

# site_key is the same value in .json files
site = "CIC"


def test_login(selenium):
    login_page = LoginPage(selenium)
    login_page.get()
    login_page.set_login_password()
    assert login_page.is_current_page()

