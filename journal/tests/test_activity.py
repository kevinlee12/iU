# coding: utf-8
#
# Copyright 2015 The iU Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from django.conf import settings


class ActivitySeleleniumTests(StaticLiveServerTestCase):
    """Selenium tests for the activity page"""
    fixtures = ['auth_users', 'groups', 'users', 'activityoptions', 'learningobjectiveoptions',
                'school', 'student', 'coordinator', 'sample_entries']

    def __init__(self, *args, **kwargs):
        super(ActivitySeleleniumTests, self).__init__(*args, **kwargs)
        if not settings.DEBUG:
            settings.DEBUG = True

    def setUp(self):
        self.selenium = WebDriver()
        # self.selenium.get('http://{0}:{1}@{2}{3}'.format("comet.tester@gmail.com", "!1WBaSr0IhPHt9aLzyBgCOOYdM1WI5pqkPKJcIpxJ", 'localhost:8081', '/activities'))
        self.selenium.get('{0}/{1}'.format(self.live_server_url, ''))

    def tearDown(self):
        self.selenium.quit()

    def test_activity_page(self):
        """Tests to ensure that activities page has all necessary elements."""
        self.selenium.find_element_by_xpath('//*[@id="djHideToolBarButton"]').click()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_link_text('Login with Google').click()
        self.selenium.find_element_by_xpath('//*[@id="Email"]').send_keys('comet.tester', Keys.ENTER)
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_xpath('//*[@id="Passwd"]').send_keys("halley's comet", Keys.ENTER)
        wait = WebDriverWait(self.selenium, 30)
        wait.until(EC.element_to_be_clickable((By.ID,'submit_approve_access')))
        self.selenium.find_element_by_xpath('//*[@id="submit_approve_access"]').click()
        self.selenium.implicitly_wait(20)
        self.selenium.find_element_by_xpath("//img[@src='/static/journal/activities/"
                                   "img/journal_sign.png']")
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[3]/a/div')
