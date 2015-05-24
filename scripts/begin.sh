#!/bin/bash

# Authors: Kevin Lee
# With Credit to Albert's response on StackOverflow: 3466166

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
echo "DB_USER=\"''\"" >> $ENV_ACTIVATE_FILE
echo "export DB_USER" >> $ENV_ACTIVATE_FILE
echo "DB_PASS=\"''\"" >> $ENV_ACTIVATE_FILE
echo "export DB_PASS" >> $ENV_ACTIVATE_FILE
echo "DB_HOST=\"'localhost'\"" >> $ENV_ACTIVATE_FILE
echo "export DB_HOST" >> $ENV_ACTIVATE_FILE
echo "...done"
echo "For the next step in the setup, type in: source env/bin/activate"
