from test_data.globals import GLOBAL_VARIABLES
import pytest


@pytest.fixture(scope="session", autouse=True)
def initialize_test_session():
    print("before session")
    GLOBAL_VARIABLES.initialize_test_session("PROD")


@pytest.fixture(scope="module", autouse=True)
def initialize_test_module(request):
    print("before module")
    site = getattr(request.module, "site")
    GLOBAL_VARIABLES.initialize_test_module(site)
