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


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from django.conf import settings
from django.core.management import call_command


class ActivitySeleleniumTests(StaticLiveServerTestCase):
    """Selenium tests for the activity page"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not settings.DEBUG:
            settings.DEBUG = True
        if not settings.TESTING:
            settings.TESTING = True

    def setUp(self):
        """Handles login and things"""
        call_command('flush', interactive=False, verbosity=0)  # Clears db
        call_command('loaddata', 'groups', commit=False, verbosity=0)
        call_command('loaddata', 'school', commit=False, verbosity=0)
        call_command('loaddata', 'permissions', commit=False, verbosity=0)
        call_command('loaddata', 'auth_users', commit=False, verbosity=0)
        call_command('loaddata', 'student', commit=False, verbosity=0)
        call_command('loaddata', 'advisor', commit=False, verbosity=0)
        call_command('loaddata', 'coordinator', commit=False, verbosity=0)
        call_command('loaddata', 'activityoptions', commit=False, verbosity=0)
        call_command('loaddata', 'learningobjectiveoptions', commit=False, verbosity=0)
        call_command('loaddata', 'sample_entries', commit=False, verbosity=0)
        self.selenium = WebDriver()
        self.selenium.set_window_size(1024, 800)
        self.selenium.get('{0}/{1}'.format(self.live_server_url, ''))
        self.selenium.find_element_by_xpath('//*[@id="djHideToolBarButton"]').click()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_link_text('Login').click()
        # Click on the student button in the gateway
        self.selenium.find_element_by_xpath('/html/body/center/md-content/div/div/div[1]/a').click()
        self.selenium\
            .find_element_by_xpath("//img[@src='/static/journal/activities/img"
                                   "/journal_sign.png']")
        super()

    def tearDown(self):
        self.selenium.quit()
        super()

    def test_activity_form_back(self):
        """make sure the back button works"""
        self.selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/a").click()
        self.selenium.find_element_by_name('activity_name').send_keys('Walking the cat')
        self.selenium.find_element_by_name('activity_description').send_keys('Walking the cat around the neighborhood')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/input').send_keys('02/07/1990')
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[2]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[3]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_learned_objective"]/li[6]/label').click()
        self.selenium.find_element_by_name('activity_adviser').send_keys('Cat')
        self.selenium.find_element_by_name('advisor_phone').send_keys('1234567890')
        self.selenium.find_element_by_name('advisor_email').send_keys('kitty@cats.cat')
        self.selenium.find_element_by_link_text('Back').click()
        self.selenium\
            .find_element_by_xpath("//img[@src='/static/journal/activities/img"
                                   "/journal_sign.png']")

    def test_activity_form_error(self):
        """Tests to check errors on the activity form"""
        self.selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/a").click()
        # self.selenium.find_element_by_name('activity_name').send_keys('')
        self.selenium.find_element_by_name('activity_description').send_keys('Walking with huahua around the neighborhood')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/input').send_keys('02/07/1990')
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[2]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[3]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_learned_objective"]/li[6]/label').click()
        self.selenium.find_element_by_name('activity_adviser').send_keys('Cat')
        self.selenium.find_element_by_name('advisor_phone').send_keys('1234567890')
        self.selenium.find_element_by_name('advisor_email').send_keys('kitty@cats.cat')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[6]/div/input').click()
        self.selenium.find_element_by_name('activity_description').text

    def test_activity_form(self):
        """Tests to ensure that activities page has all necessary elements."""
        self.selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/a").click()
        self.selenium.find_element_by_name('activity_name').send_keys('Walking the cat')
        self.selenium.find_element_by_name('activity_description').send_keys('Walking the cat around the neighborhood')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/input').send_keys('02/07/1990')
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[2]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_activity_type"]/li[3]/label').click()
        self.selenium.find_element_by_xpath('//*[@id="id_learned_objective"]/li[6]/label').click()
        self.selenium.find_element_by_name('activity_adviser').send_keys('Cat')
        self.selenium.find_element_by_name('advisor_phone').send_keys('1234567890')
        self.selenium.find_element_by_name('advisor_email').send_keys('kitty@cats.cat')
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[6]/div/input').click()
        self.selenium\
            .find_element_by_xpath("//img[@src='/static/journal/activities/img"
                                   "/journal_sign.png']")
        body_text = self.selenium.find_element_by_tag_name('body').text
        self.assertTrue('Walking the cat' in body_text)
        self.assertTrue('Walking the cat around the neighborhood' in body_text)
