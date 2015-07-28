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

from PIL import Image

from imagekit.processors import ResizeToFill

MAX_WIDTH = 500
MAX_HEIGHT = 500

class ResizeToRatio:
    """A Processor that will resize an image to MAX_WIDTH and MAX_HEIGHT."""

    def process(self, image):
        w, h = image.size
        if w > MAX_WIDTH and w > h:
            h = (h * MAX_WIDTH) // w
            w = MAX_WIDTH
        elif h > MAX_HEIGHT and h > w:
            w = (w * MAX_HEIGHT) // h
            h = MAX_HEIGHT
        return image.resize((w, h), Image.ANTIALIAS)
