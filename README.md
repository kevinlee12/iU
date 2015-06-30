CAS Management
===
**Master:** [![Circle CI](https://circleci.com/gh/kevinlee12/iU/tree/master.svg?style=svg&circle-token=02f06191194ac379a0c4b7244fa361a6a619098a)](https://circleci.com/gh/kevinlee12/iU/tree/master)

**Develop:**
[![Circle CI](https://circleci.com/gh/kevinlee12/iU/tree/develop.svg?style=svg&circle-token=02f06191194ac379a0c4b7244fa361a6a619098a)](https://circleci.com/gh/kevinlee12/iU/tree/develop)

For a hosted version of this app, please click [here](http://cas-codestig.rhcloud.com).

###Features

- Core journal features: text, images, documents, video(TBD)
- Gmail, Yahoo, or Windows login
- Facebook/Twitter Feed Pulls
- Email reminders

###Installation on local machine

1. Install Python 3 (do **not** install Python 2):

 - For Macs (with homebrew):

 -- Install homebrew if you have not already:
 `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

 -- Install Python 3 using Brew:

 `brew install python3`

 -- Ubuntu systems should have Python 3 preinstalled.

2. Clone repo:
 `git clone https://github.com/kevinlee12/iu.git`

3. Navigate to the cas folder, on Unix/Linux the command is

 `cd iu`

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
