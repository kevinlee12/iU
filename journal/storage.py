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
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.core.files.storage import Storage
import cloudinary
import cloudinary.uploader
import urllib
from urllib.error import HTTPError
import os

import sys
import logging
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
logging.config.dictConfig(LOGGING)


class CloudinaryStorage(Storage):
    """Storage class to store files on Cloudinary"""

    def __init__(self, option=None):
        self.server_response = {}

    def _open(self, name, mode):
        logging.info('opening file')
        name = '{0}.{1}'.format(self.server_response['public_id'], self.server_response['format'])
        return cloudinary.CloudinaryImage(name).image()

    def _save(self, name, content):
        logging.info("saving file")
        self.server_response = cloudinary.uploader.upload(content)
        logging.info(self.server_response)
        return '{0}.{1}'.format(self.server_response['public_id'], self.server_response['format'])

    def exists(self, name):
        logging.info("checking existance")
        try:
            urllib.request.urlopen(self.server_response['secure_url'])
        except:
            return False
        return True

    def delete(self, name):
        logging.info("deleting")
        name = '{0}.{1}'.format(self.server_response['public_id'], self.server_response['format'])
        return cloudinary.uploader.destroy(name)

    def size(self, name):
        logging.info("checking size")
        img = urllib.request.urlopen(self.url(name))
        return int(img.headers['Content-Length'])

    def url(self, name):
        logging.info('getting something')
        logging.info(self.server_response)
        return self.server_response['secure_url']
