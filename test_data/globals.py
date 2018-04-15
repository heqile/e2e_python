import json
from os.path import dirname, abspath
from commun.data_helper import GlobalData, SiteData


class GlobalVariables(object):

    """ Global variables """

    # global data
    PROJECT_PATH = dirname(dirname(abspath(__file__)))
    GLOBAL_HOST_DATA = json.load(open(PROJECT_PATH + "/test_data/host_data.json"))
    GLOBAL_PAGE_DATA = json.load(open(PROJECT_PATH + "/test_data/page_data.json"))
    GLOBAL_USER_DATA = json.load(open(PROJECT_PATH + "/test_data/user_data.json"))

    # variables initialize before test session starts
    ENVIRONMENT = ""
    DEBUG_ENABLE = True
    SESSION_HOST_DATA = {}
    SESSION_PAGE_DATA = {}
    SESSION_USER_DATA = {}

    # variables initialize before test module starts
    SITE = ""
    MODULE_HOST_DATA = {}
    MODULE_PAGE_DATA = {}
    MODULE_USER_DATA = {}

    GLOBAL_DATA = None  # type: GlobalData
    SITE_DATA = None  # type: SiteData

    LOG_ASSETS = []

    def initialize_test_session(self, environment, debug_enable):
        self.ENVIRONMENT = environment
        self.DEBUG_ENABLE = debug_enable
        self.SESSION_HOST_DATA = self.GLOBAL_HOST_DATA[environment]
        self.SESSION_PAGE_DATA = self.GLOBAL_PAGE_DATA
        self.SESSION_USER_DATA = self.GLOBAL_USER_DATA[environment]
        self.GLOBAL_DATA = GlobalData(self.SESSION_HOST_DATA, self.SESSION_PAGE_DATA, self.SESSION_USER_DATA)

    def initialize_test_module(self, site):
        self.SITE = site
        # self.MODULE_HOST_DATA = self.SESSION_HOST_DATA[site]
        # self.MODULE_PAGE_DATA = self.SESSION_PAGE_DATA[site]
        # self.MODULE_USER_DATA = self.SESSION_USER_DATA[site]
        self.SITE_DATA = self.GLOBAL_DATA.get_site(site)


# Create GlobalVariables instance
GLOBAL_VARIABLES = GlobalVariables()
