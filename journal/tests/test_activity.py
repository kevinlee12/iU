from django.test import TestCase, Client, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class ActivitySeleleniumTests(LiveServerTestCase):
    """Selenium tests for the activity page"""

    @classmethod
    def setUpClass(cls):
        super(ActivitySeleleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ActivitySeleleniumTests, cls).tearDownClass()

    def test_activity_page(self):
        """Tests to ensure that the word activityies is present"""
        self.selenium.get('%s%s' % (self.live_server_url, '/activities/'))
        self.selenium.find_elements_by_link_text('Activities')
