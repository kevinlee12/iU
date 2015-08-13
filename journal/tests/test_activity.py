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
from django.core.management import call_command


class ActivitySeleleniumTests(StaticLiveServerTestCase):
    """Selenium tests for the activity page"""
    fixtures = ['groups', 'school', 'permissions', 'auth_users', 'student',
                'advisor', 'coordinator', 'activityoptions',
                'learningobjectiveoptions', 'sample_entries']

    def __init__(self, *args, **kwargs):
        super(ActivitySeleleniumTests, self).__init__(*args, **kwargs)
        if not settings.DEBUG:
            settings.DEBUG = True

    def setUp(self):
        """Handles login and things"""
        self.selenium = WebDriver()
        self.selenium.set_window_size(1024, 800)
        self.selenium.get('{0}/{1}'.format(self.live_server_url, ''))
        self.selenium.find_element_by_xpath('//*[@id="djHideToolBarButton"]').click()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_link_text('Login with Google').click()
        self.selenium.find_element_by_xpath('//*[@id="Email"]').send_keys('comet.tester', Keys.ENTER)
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_xpath('//*[@id="Passwd"]').send_keys("halley's comet", Keys.ENTER)
        wait = WebDriverWait(self.selenium, 30)
        wait.until(EC.element_to_be_clickable((By.ID,'submit_approve_access')))
        self.selenium.find_element_by_xpath('//*[@id="submit_approve_access"]').click()
        super()

    def tearDown(self):
        self.selenium.quit()
        super()

    def test_activity_form(self):
        """Tests to ensure that activities page has all necessary elements."""
        self.selenium\
            .find_element_by_xpath("//img[@src='/static/journal/activities/img"
                                   "/journal_sign.png']")
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[3]/a/div')
        self.selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/a").click()
        self.selenium.find_element_by_name('activity_name').send_keys('Walking the cat')
        self.selenium.find_element_by_name('activity_description').send_keys('Walking the cat around the neighborhood')
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[2]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[3]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_learned_objective"]/li[6]/label').click()
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[5]/div/div/div[1]/input').send_keys('Cat')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[5]/div/div/div[3]/input').send_keys('kitty@cats.cat')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[6]/div/input').click()
        self.selenium\
            .find_element_by_xpath("//img[@src='/static/journal/activities/img"
                                   "/journal_sign.png']")
        body_text = self.selenium.find_element_by_tag_name('body').text
        self.assertTrue('Walking the cat' in body_text)
        self.assertTrue('Walking the cat around the neighborhood' in body_text)
