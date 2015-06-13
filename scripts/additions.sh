#!/bin/bash -e

#For Google Login stuff

ENV_ACTIVATE_FILE=env/bin/activate
echo "Setting up keys for Google Login..."
echo "" >> $ENV_ACTIVATE_FILE
echo "#Keys for Google Login" >> $ENV_ACTIVATE_FILE
echo "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='414510227299-0nk01g19f5oo6sll4nr50m3da2en9dt9.apps.googleusercontent.com'" >> $ENV_ACTIVATE_FILE
echo "export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY" >> $ENV_ACTIVATE_FILE
echo "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='PeL51ko5yGsZs9V2k0uoV1--'" >> $ENV_ACTIVATE_FILE
echo "export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET" >> $ENV_ACTIVATE_FILE
echo "...done"
