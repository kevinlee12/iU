CAS Management
===
[![Circle CI](https://circleci.com/gh/kevinlee12/cas.svg?style=svg)](https://circleci.com/gh/kevinlee12/cas)

For a hosted version of this app, please click [here](http://cas-codestig.rhcloud.com).

###Features

- Core journal features: text, images, documents, video(TBD)
- Gmail, Yahoo, or Windows login
- Facebook/Twitter Feed Pulls
- Email reminders

###Installation on local machine
Notes: We will not be officially supporting Windows platform at this time. As an alternative, please install a Debian-based Linux distro (ie. Ubuntu, Linux Mint, etc) on VirtualBox.

1. Install Python 3 (do **not** install Python 2):

 - For Macs (with homebrew):

 -- Open the terminal

 -- Install homebrew if you have not already:
 `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

 -- Install Python 3 using Brew:

 `brew install python3`

 -- Ubuntu systems should have Python 3 preinstalled.

2. Clone repo:
 `git clone https://github.com/kevinlee12/cas.git`

3. Navigate to the cas folder, on Unix/Linux the command is

 `cd cas`

4. Start the setup script:
 `bash scripts/begin.sh`

 It will then do some pip installation to ensure all the dependencies are satisfied and modify the default virtualenv to satisfy the requirements of our project.

7. Set up the database:

 `django-admin manage.py migrate`

8. Run the server:

 `django-admin manage.py runserver`

 Here the terminal will tell you how to access the website, like http://127.0.0.1:8000/. Copy and paste that link from the terminal into your favorite browser. That's it!

10. To close the server:
 - Press CTRL - C on your keyboard
 - Type `deactivate` into the terminal.
