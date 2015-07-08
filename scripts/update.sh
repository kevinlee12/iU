#!/bin/bash -e

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

# The purpose of the script is to update outdated pip packages.
# Credit goes to rdp's answer in StackOverflow: 2720014 for line 23
# Line 23 is omitted from the program's licensing restrictions

echo "Starting update of pip packages"
source env/bin/activate
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
echo "...done"
echo "Recoding new versions"
pip freeze > requirements.txt
echo "...done"
