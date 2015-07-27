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

# For use when there is a need to reload the database

echo "Beginning the reload process"
echo "Activating the virtual environment"
source env/bin/activate
echo
for arg in "$@"; do
  if [ "$arg" == "--ignore-pip" ]; then
    echo "Bypassing pip"
  else
    echo "Ensuring that all pip requirements are satisfied"
    pip install -r requirements.txt
    echo "...done"
  fi
done
echo
echo "Dropping the old iu database"
dropdb iu
echo "...done"
echo
echo "Creating new iu database"
createdb iu
echo "...done"
echo
# echo "Removing old migrations"
# rm -rf journal/migrations
# echo "...done"
# echo "Making migrations"
# python3 manage.py makemigrations journal
# echo "...done"
echo
sleep 5
echo "Migrating database"
python3 manage.py migrate
echo "...done"
echo "Loading the databases with data"
echo "Loadding user data"
python manage.py loaddata auth_users
echo "Loadding group data"
python manage.py loaddata groups
echo "Loading users data"
python manage.py loaddata users
echo "Loading school data"
python manage.py loaddata school
echo "Loading student data"
python manage.py loaddata student
# echo "Loading advisor data"
# python manage.py loaddata advisor
echo "Loading coordinator data"
python manage.py loaddata coordinator
echo "Loading activityoptions data"
python manage.py loaddata activityoptions
echo "Loading learningobjectiveoptions data"
python manage.py loaddata learningobjectiveoptions
echo "...done"
echo "Loading sample entries and stuff"
python manage.py loaddata sample_entries
echo
echo "If any tests fail, something went wrong"
python3 manage.py test
echo
deactivate
