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

from .utilities import assert_true


class ActivitySeleleniumTests(StaticLiveServerTestCase):
    """Selenium tests for the activity page"""

    def setUp(self):
        """Opens the home page"""
        self.selenium = WebDriver()
        self.selenium.get('{0}{1}'.format(self.live_server_url, '/'))

    def tearDown(self):
        self.selenium.quit()
        super()

    def test_elements(self):
        """Tests to ensure the proper elements are present"""
        self.selenium.find_elements_by_link_text('iU')
        self.selenium.find_elements_by_link_text('Welcome')
        about_us = self.selenium\
            .find_elements_by_xpath('//*[@href="#about-us"]')
        assert_true(len(about_us), 2)
        self.selenium.find_element_by_link_text('Features').click()
