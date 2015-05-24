#!/bin/bash

# Authors: Kevin Lee

# This file is intended to simplify setup of the program.
# What the file does:
# 1. Check to ensure that Python3 is installed
# 2. Sets up virtualenv to use Python3
# 3. Sets the appropriate environment variables in the virtualenv
#    for the SECRET_KEY and Database basic information

echo "Checking to ensure right Python is installed"
if [[ -n $(python3 --version || grep "Python 3") ]]; then
    echo "Right Python version installed"
elif  [[ -n $(python --version || grep "Python 3") ]]; then
    echo "Right Python version installed"
else
    echo "Incorrect Python version installed, quitting..."
    exit
fi
echo

echo "Setting up Virtualenv..."
if [ "$(uname)" == "Darwin" ]; then
    virtualenv -p /usr/local/bin/python3 env
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    virtualenv -p /usr/bin/python3 env
fi
ENV_ACTIVATE_FILE=env/bin/activate
echo "...Done"
echo
echo "Setting Environment Varibles for Virtualenv"
echo "" >> $ENV_ACTIVATE_FILE
echo "# Env Variables Required for this Project" >> $ENV_ACTIVATE_FILE
echo "SECRET_KEY=\"sy-cmx%i$8*cgz0*\)r_l&qbc1b2wu-hhmr-g5s9p$\(n0hehsb8\"" >> $ENV_ACTIVATE_FILE
echo "export SECRET_KEY" >> $ENV_ACTIVATE_FILE
echo "" >> $ENV_ACTIVATE_FILE
echo "...Done"
echo
echo "Setting up Database Variables"
echo "# Database Variables" >> $ENV_ACTIVATE_FILE
echo "OPENSHIFT_POSTGRESQL_DB_USERNAME=''" >> $ENV_ACTIVATE_FILE
echo "export OPENSHIFT_POSTGRESQL_DB_USERNAME" >> $ENV_ACTIVATE_FILE
echo "OPENSHIFT_POSTGRESQL_DB_PASSWORD=''" >> $ENV_ACTIVATE_FILE
echo "export OPENSHIFT_POSTGRESQL_DB_PASSWORD" >> $ENV_ACTIVATE_FILE
echo "OPENSHIFT_POSTGRESQL_DB_HOST='localhost'" >> $ENV_ACTIVATE_FILE
echo "export OPENSHIFT_POSTGRESQL_DB_HOST" >> $ENV_ACTIVATE_FILE
echo "...done"
echo "For the next step in the setup, type in: source env/bin/activate"
