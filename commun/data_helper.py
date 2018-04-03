# from test_data.globals import GLOBAL_VARIABLES


class Selects(object):

    def __init__(self, data):
        self.data = data

    def get_entry(self):
        return self.data['entry']

    def get_option(self, option_name):
        return self.data["options"][option_name]


class PageData(object):

    def __init__(self, page_data):
        # print(page_data)
        self.data = page_data

    def get_path(self):
        # type: () -> str
        return self.data['path']

    def get_locator(self, locator_name):
        return self.data['locators'][locator_name]

    def get_select(self, select_name):
        # type: (str) -> Selects
        return Selects(self.data['selects'][select_name])


class SiteData(object):

    def __init__(self, host_data_on_site, page_data_on_site, user_data_on_site):
        # print(page_data)
        self.host_data = host_data_on_site
        self.page_data = page_data_on_site
        self.user_data = user_data_on_site

    def get_page(self, page_name):
        # type: (str) -> PageData
        return PageData(self.page_data[page_name])

    def get_host(self):
        return self.host_data['host']

    def get_cookie(self, cookie_name):
        return self.host_data['cookie_list'][cookie_name]

    def get_login(self):
        return self.user_data['login']

    def get_password(self):
        return self.user_data['password']

    def get_wrong_login(self):
        return self.user_data['wrong_login']

    def get_user_data(self):
        return self.user_data


class GlobalData(object):

    def __init__(self, global_host_data, global_page_data, global_user_data):
        self.host_data = global_host_data
        self.page_data = global_page_data
        self.user_data = global_user_data

    def get_site(self, site):
        # type: (str) -> SiteData
        return SiteData(self.host_data[site], self.page_data[site], self.user_data[site])


# def main():
#     GLOBAL_VARIABLES.initialize_test_session('PROD', True)
#     GLOBAL_VARIABLES.initialize_test_module('CM')
#     d = GlobalData(GLOBAL_VARIABLES.SESSION_HOST_DATA, GLOBAL_VARIABLES.SESSION_PAGE_DATA, GLOBAL_VARIABLES.SESSION_USER_DATA)
#     print(d.get_site('CM').get_page('LoginPage').get_select('test').get_option('option_name1'))
#     print(d.get_site('CM').get_cookie('cookie_1'))
#     print(d.get_site('CM').get_login())
#
#
# if __name__ == '__main__':
#     main()
