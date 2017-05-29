# Run with:
#  py.test test_demo.py --grid_ip YOUR_GRID_IP -s

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import unittest

grid_ip = pytest.config.option.grid_ip
# Error out if --grid_ip value wasn't given or isn't a string
try:
    if not isinstance(grid_ip, basestring):
        message = "The --grid_ip value '{0}' is not a valid string!".format(grid_ip)
        sys.exit(message)
except NameError:
    message = "Please provide the IP of your grid hub with --grid_ip."
    sys.exit(message)

class TestDemo(unittest.TestCase):
    def setUp(self):
        # Set desired capabilities
        desired_cap = {
            'platform': "Linux",
            'browserName': "chrome",
        }
        self.grid_ip = pytest.config.option.grid_ip
        self.driver = webdriver.Remote(
            command_executor="http://{0}:4444/wd/hub".format(self.grid_ip),
            desired_capabilities=desired_cap)
        print("View live VNC session for your test at http://{0}:4444/grid/admin/live".format(self.grid_ip))

    def tearDown(self):
        # On Sauce Labs this is important to stop running tests:
        self.driver.quit()
        print("View archived video of your test at http://{0}:5555".format(self.grid_ip))

    # Test logic goes here
    def test_demo(self):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("Zalenium")
        elem.submit()
        print self.driver.title
