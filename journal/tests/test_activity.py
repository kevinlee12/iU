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
        self.selenium.get('%s%s' % (self.live_server_url, '/activities/'))

    def test_activity_page(self):
        """Tests to ensure that the word activityies is present"""
        self.selenium.find_elements_by_link_text('Activities')
