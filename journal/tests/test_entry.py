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

from django.conf import settings
import os


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

    def test_text_entry(self):
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

    def test_image_entry(self):
        """Test to ensure that a student can add an image entry"""
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/a/div').click()
        self.selenium.find_element_by_link_text('Add an entry').click()
        # The following has 2 matching: Just walking and Adding entry...block
        header_text = self.selenium.find_elements_by_tag_name('h3')[1].text
        self.assertTrue('Adding entry for Walking around the block!' in header_text)
        # Switching to iframe focus
        self.selenium.switch_to_frame(self.selenium.find_element_by_id('id_entry_iframe'))
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/button[2]').click()
        entry = 'http://images.jfdaily.com/jiefang/wenyu/new/201409/W020140919421426345484.jpg'
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/input')\
            .send_keys(entry)
        #click on the inset image button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[3]/button').click()
        # Switch back out of the iframe.
        self.selenium.switch_to_default_content()
        # Click on the submit button
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_class_name('btn-success').click()
        # Ensure that we are back on the entries page.
        self.selenium.find_element_by_link_text('Add an entry')
        # Ensure that entry exists on the page.
        self.selenium.find_element_by_xpath("//img[@src='http://images.jfdaily.com/jiefang/wenyu/new/201409/W020140919421426345484.jpg']")

    def test_video_entry(self):
        """Test to ensure that a student can add an image entry"""
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/a/div').click()
        self.selenium.find_element_by_link_text('Add an entry').click()
        # The following has 2 matching: Just walking and Adding entry...block
        header_text = self.selenium.find_elements_by_tag_name('h3')[1].text
        self.assertTrue('Adding entry for Walking around the block!' in header_text)
        # Switching to iframe focus
        self.selenium.switch_to_frame(self.selenium.find_element_by_id('id_entry_iframe'))
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/button[3]').click()
        entry = 'https://www.youtube.com/watch?v=Rk_bV0RJRhs&index=20&list=PLJU_WCB1rA2SFwFy3lEvY_NH23ql1-Cgi'
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div/div[2]/div/input')\
            .send_keys(entry)
        #click on the insert video button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div/div[3]/button').click()
        # Switch back out of the iframe.
        self.selenium.switch_to_default_content()
        # Click on the submit button
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_class_name('btn-success').click()
        # Ensure that we are back on the entries page.
        self.selenium.find_element_by_link_text('Add an entry')
        self.selenium.find_element_by_xpath('//iframe[@src="//www.youtube.com/embed/Rk_bV0RJRhs"]')

    def test_image_video_text_entry(self):
        """Test to ensure that a student can add image+text and video+text entries"""
        # TODO(janice): Please split this test into 2: 1) image + text 2) video + text
        # Also, please make sure your comments follow the format that has been used throughout the file:
        # Hash mark, space, then comment, like so: # Comment here.
        # Just to maintain pep8 as much as possible :)
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/a/div').click()
        self.selenium.find_element_by_link_text('Add an entry').click()
        # The following has 2 matching: Just walking and Adding entry...block
        header_text = self.selenium.find_elements_by_tag_name('h3')[1].text
        self.assertTrue('Adding entry for Walking around the block!' in header_text)
        # Switching to iframe focus
        self.selenium.switch_to_frame(self.selenium.find_element_by_id('id_entry_iframe'))
        # insert text
        entry = 'I think I will bring my cat out next time with a flower.'
        self.selenium.find_element_by_class_name('note-editable')\
            .send_keys(entry)
        #insert the image
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/button[2]').click()
        image_path = os.path.join(settings.BASE_DIR, 'journal', 'tests', 'fixtures', 'test.png')
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/input').send_keys(image_path)
        #click on the insert image button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[3]/button').click()
        # Switch back out of the iframe.
        self.selenium.switch_to_default_content()
        # Click on the submit button
        self.selenium.find_element_by_class_name('btn-success').click()
        # Ensure that we are back on the entries page.
        self.selenium.find_element_by_link_text('Add an entry')
        #ensure the text is on the entries page
        box_text = self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/a/div').text
        self.assertTrue(entry in box_text)
        #ensure the image is on the entries page
        self.selenium.find_element_by_xpath('//<img src="/media/django-summernote/2015-08-15/5d55c61e-58df-427a-83a7-58d948b16619.png"]')

    def test_all_three(self):
        """Test to ensure that a student can add all three kinds of entry"""
        # Click on the first activity box: Walking around the block
        self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div[3]/a/div').click()
        self.selenium.find_element_by_link_text('Add an entry').click()
        # The following has 2 matching: Just walking and Adding entry...block
        header_text = self.selenium.find_elements_by_tag_name('h3')[1].text
        self.assertTrue('Adding entry for Walking around the block!' in header_text)
        # Switching to iframe focus
        self.selenium.switch_to_frame(self.selenium.find_element_by_id('id_entry_iframe'))
        #insert text
        text_entry = 'I think I will bring my cat out next time.'
        self.selenium.find_element_by_class_name('note-editable')\
            .send_keys(text_entry)
        #insert image button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/button[2]').click()
        image_entry = 'http://images.jfdaily.com/jiefang/wenyu/new/201409/W020140919421426345484.jpg'
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/input')\
            .send_keys(image_entry)
        #click on the inset image button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[3]/button').click()
        #insert video button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/button[3]').click()
        video_entry = 'https://www.youtube.com/watch?v=Rk_bV0RJRhs&index=20&list=PLJU_WCB1rA2SFwFy3lEvY_NH23ql1-Cgi'
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div/div[2]/div/input')\
            .send_keys(video_entry)
        #click on the insert video button
        self.selenium.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/div/div[3]/button').click()
        # Switch back out of the iframe.
        self.selenium.switch_to_default_content()
        # Click on the submit button
        self.selenium.find_element_by_class_name('btn-success').click()
        # Ensure that we are back on the entries page.
        self.selenium.find_element_by_link_text('Add an entry')
        # Ensure that entry exists as the first box on the page.
        box_text = self.selenium.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/a/div').text
        self.assertTrue(text_entry in box_text)
        self.selenium.find_element_by_xpath("//img[@src='http://images.jfdaily.com/jiefang/wenyu/new/201409/W020140919421426345484.jpg']")
        self.selenium.find_element_by_xpath('//iframe[@src="//www.youtube.com/embed/Rk_bV0RJRhs"]')
