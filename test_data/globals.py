import json
from os.path import dirname, abspath


class GlobalVariables(object):

    # global data
    PROJECT_PATH = dirname(dirname(abspath(__file__)))
    GLOBAL_HOST_DATA = json.load(open(PROJECT_PATH + "/test_data/host_data.json"))
    GLOBAL_PAGE_DATA = json.load(open(PROJECT_PATH + "/test_data/page_data.json"))
    GLOBAL_USER_DATA = json.load(open(PROJECT_PATH + "/test_data/user_data.json"))

    # variables initialize before test session starts
    ENVIRONMENT = ""
    SESSION_HOST_DATA = {}
    SESSION_PAGE_DATA = {}
    SESSION_USER_DATA = {}

    # variables initialize before test module starts
    SITE = ""
    MODULE_HOST_DATA = {}
    MODULE_PAGE_DATA = {}
    MODULE_USER_DATA = {}

    def initialize_test_session(self, environment):
        self.ENVIRONMENT = environment
        self.SESSION_HOST_DATA = self.GLOBAL_HOST_DATA[environment]
        self.SESSION_PAGE_DATA = self.GLOBAL_PAGE_DATA
        self.SESSION_USER_DATA = self.GLOBAL_USER_DATA[environment]

    def initialize_test_module(self, site):
        self.SITE = site
        self.MODULE_HOST_DATA = self.SESSION_HOST_DATA[site]
        self.MODULE_PAGE_DATA = self.SESSION_PAGE_DATA[site]
        self.MODULE_USER_DATA = self.SESSION_USER_DATA[site]

GLOBAL_VARIABLES = GlobalVariables()
