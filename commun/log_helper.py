from test_data.globals import GLOBAL_VARIABLES


class Log(object):

    description = ''
    url = ''
    screenshot = ''
    html = ''
    error = ''

    def __init__(self, description, driver=None):
        self.description = description
        if driver:
            self._gather_url(driver)
            self._gather_screenshot(driver)
            self._gather_html(driver)

    def _gather_url(self, driver):
        try:
            self.url = driver.current_url
        except Exception as e:
            self.error = 'WARNING: Failed to gather URL: {0}'.format(e)
            return

    def _gather_screenshot(self, driver):
        try:
            self.screenshot = driver.get_screenshot_as_base64()
        except Exception as e:
            self.error = 'WARNING: Failed to gather screenshot: {0}'.format(e)
            return

    def _gather_html(self, driver):
        try:
            self.html = driver.page_source
        except Exception as e:
            self.error = 'WARNING: Failed to gather HTML: {0}'.format(e)
            return


def add_log_point(description, driver=None):
    log_item = Log(description, driver)
    GLOBAL_VARIABLES.LOG_ASSETS.append(log_item)


# do in browser fixture
def set_up_log_list():
    GLOBAL_VARIABLES.LOG_ASSETS = []
