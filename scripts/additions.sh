#!/bin/bash -e

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
