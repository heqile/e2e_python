
DATA = {'CM': {'test1': '', 'test2': ['12', '13']}, 'CIC': {'test1': '1'}}

class TestConfiguration(object):
    site = ''
    param = ''

    def __init__(self, site, param):
        self.site = site
        self.param = param

def pytest_generate_tests(metafunc):
    print('init')
    if 'test_configuration' in metafunc.fixturenames:
        test_config = []
        for site, config in DATA.items():
            for test_name, parameters in config.items():
                if test_name == metafunc.function.__name__:
                    if parameters == '':
                        test_config.append(TestConfiguration(site, parameters))
                    for parameter in parameters:
                        test_config.append(TestConfiguration(site, parameter))
        metafunc.parametrize("test_configuration", test_config)


def test1(test_configuration):
    print("in test 1")
    print(test_configuration.site, test_configuration.param)
    assert True
