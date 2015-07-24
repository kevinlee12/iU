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
echo "Ensuring that all pip requirements are satisfied"
pip install -r requirements.txt
echo "...done"
echo
# echo "Checking npm"
# if [[ -n $(npm -v || grep "No") ]]; then
#     echo "NPM is not installed"
#     echo "Ensuring all npm files are satisfied"
#     nodeenv --requirements=node-requirements.txt --jobs=4 --force env
#     echo
# elif  [[ -n $(npm --version || grep "1.") ]]; then
#     echo "NPM installed, moving on"
# fi
# deactivate_node
echo "Dropping the old iu database"
dropdb iu
echo "...done"
echo
echo "Creating new iu database"
createdb iu
echo "...done"
echo
echo "Removing old migrations"
rm -rf journal/migrations
echo "...done"
echo "Making migrations"
python3 manage.py makemigrations journal
echo "...done"
echo
echo "Migrating database"
python3 manage.py migrate
echo "...done"
echo "Loading the databases with data"
echo
echo "Loading activityoptions data"
python manage.py loaddata activityoptions
echo "Loading learningobjectiveoptions data"
python manage.py loaddata learningobjectiveoptions
echo "Loading users data"
python manage.py loaddata users
echo "Loading school data"
python manage.py loaddata school
echo "Loading student data"
python manage.py loaddata student
echo "Loading advisor data"
python manage.py loaddata advisor
echo "Loading coordinator data"
python manage.py loaddata coordinator
echo "...done"
echo "Loading sample entries and stuff"
python manage.py loaddata sample_entries
echo
echo "Running tests to ensure nothing is broken"
echo "If any tests fail, something went wrong"
python3 manage.py test
echo
deactivate
