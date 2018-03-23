from selenium import webdriver
import unittest


class E2ETestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.webdriver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.webdriver.close()