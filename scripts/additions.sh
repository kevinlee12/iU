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

#For Google Login stuff

ENV_ACTIVATE_FILE=env/bin/activate
echo "Setting up keys for Google Login..."
echo "" >> $ENV_ACTIVATE_FILE
echo "#Keys for Google Login" >> $ENV_ACTIVATE_FILE
echo "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='<Google Client Key>'" >> $ENV_ACTIVATE_FILE
echo "export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY" >> $ENV_ACTIVATE_FILE
echo "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='<Google Client Secret>'" >> $ENV_ACTIVATE_FILE
echo "export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET" >> $ENV_ACTIVATE_FILE
echo "...done"
