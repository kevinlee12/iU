from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class ActivitySeleleniumTests(StaticLiveServerTestCase):
    """Selenium tests for the activity page"""

    @classmethod
    def setUpClass(cls):
        super(ActivitySeleleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ActivitySeleleniumTests, cls).tearDownClass()

    def setUp(self):
        """Opens the home page"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))

    def test_elements(self):
        """Tests to ensure the proper elements are present"""
        self.selenium.find_elements_by_link_text('iU')
        self.selenium.find_elements_by_link_text('Welcome')
