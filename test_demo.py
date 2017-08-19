# Run with:
#  py.test test_demo.py --hub_host YOUR_GRID_IP -s

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import unittest

hub_host = pytest.config.option.hub_host
# Error out if --hub_host value wasn't given or isn't a string
try:
    if not isinstance(hub_host, basestring):
        message = "The --hub_host value '{0}' is not a valid string!".format(hub_host)
        sys.exit(message)
except NameError:
    message = "Please provide the IP of your grid hub with --hub_host."
    sys.exit(message)

class TestDemo(unittest.TestCase):
    def setUp(self):
        # Set desired capabilities
        desired_cap = {
            'platform': "Linux",
            'browserName': "chrome",
        }
        hub_host = pytest.config.option.hub_host
        hub_port = "4444"
        hub_url = "http://test:PUT_YOUR_OWN_UNIQUE_GRID_PASSWORD_HERE@{0}:{1}/wd/hub".format(hub_host, hub_port)
        self.video_dashboard_url = "http://{0}:{1}/dashboard/".format(hub_host, hub_port)
        self.driver = webdriver.Remote(
            command_executor=hub_url,
            desired_capabilities=desired_cap)
        live_url = "http://{0}:{1}/grid/admin/live".format(hub_host, hub_port)
        print("View live VNC session for your test at {0}".format(live_url))

    def tearDown(self):
        # On Sauce Labs this is important to stop running tests:
        self.driver.quit()
        print("View archived video of your test at {0}".format(self.video_dashboard_url))

    # Test logic goes here
    def test_demo(self):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("Zalenium")
        elem.submit()
        print self.driver.title
