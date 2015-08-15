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


class EntrySeleleniumTests(StaticLiveServerTestCase):
    """Selenium tests for the entry form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not settings.DEBUG:
            settings.DEBUG = True

    def setUp(self):
        """Handles login and things"""
        call_command('flush', interactive=False, verbosity=0)  # Clears db
        call_command('loaddata', 'test_init', commit=False, verbosity=0)
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
        self.selenium\
            .find_element_by_xpath("//img[@src='/static/journal/activities/img"
                                   "/journal_sign.png']")
        super()

    def tearDown(self):
        self.selenium.quit()
        super()

    def test_text_enty(self):
        """Test to ensure that a student can add a text entry"""
        # Click on the first activity box: Walking around the block
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/a/div').click()
        self.selenium.find_element_by_link_text('Add an entry').click()
        # The following has 2 matching: Just walking and Adding entry...block
        header_text = self.selenium.find_elements_by_tag_name('h3')[1].text
        self.assertTrue('Adding entry for Walking around the block!' in header_text)
        # Switching to iframe focus
        self.selenium.switch_to_frame(self.selenium.find_element_by_id('id_entry_iframe'))
        entry = 'I think I will bring my cat out next time.'
        self.selenium.find_element_by_class_name('note-editable')\
            .send_keys(entry)
        # Switch back out of the iframe.
        self.selenium.switch_to_default_content()
        # Click on the submit button
        self.selenium.find_element_by_class_name('btn-success').click()
        # Ensure that we are back on the entries page.
        self.selenium.find_element_by_link_text('Add an entry')
        # Ensure that entry exists as the first box on the page.
        box_text = self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/a/div').text
        self.assertTrue(entry in box_text)
