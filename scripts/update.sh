#!/bin/bash -e

# Author: Kevin Lee

# The purpose of the script is to update outdated pip packages.
# Credit goes to rdp's answer in StackOverflow: 2720014

echo "Starting update of pip packages"
source env/bin/activate
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
echo "...done"
echo "Recoding new versions"
pip freeze > requirements.txt
echo "...done"
