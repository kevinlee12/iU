from setuptools import setup

import os
import sys

setup(name='iU',
    version='0.3',
    description='CAS Management App',
    author='Kevin Lee, Rodney Ho, Janice Zhao',
    author_email='',
    url='cas-codestig.rhcloud.com',
)

os.environ['DJANGO_SETTINGS_MODULE'] = 'openshift.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'openshift'))
virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass
