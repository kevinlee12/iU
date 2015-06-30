#!/bin/bash -e

# Author: Kevin Lee

# For use when there is a need to reload the database

echo "Beginning the reload process"
echo "Activating the virtual environment"
source env/bin/activate
echo
echo "Ensuring that all pip requirements are satisfied"
pip install -r requirements.txt
echo "...done"
echo
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
echo "Loading school data"
python manage.py loaddata school
echo "Loading coordinator data"
python manage.py loaddata coordinator
echo "Loading advisor data"
python manage.py loaddata advisor
echo "Loading student data"
python manage.py loaddata student
echo "Loading users data"
python manage.py loaddata users
echo "Loading activityoptions data"
python manage.py loaddata activityoptions
echo "Loading learningobjectiveoptions data"
python manage.py loaddata learningobjectiveoptions
echo "...done"
echo
echo "Running tests to ensure nothing is broken"
echo "If any tests fail, something went wrong"
python3 manage.py test
echo
deactivate
