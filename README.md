CAS Management
===
For a hosted version of this app, please click [here](http://cas-codestig.rhcloud.com).

###Features

- Core journal features: text, images, documents, video(TBD)
- Gmail, Yahoo, or Windows login
- Facebook/Twitter Feed Pulls
- Email reminders

###Installation on local machine
Notes: Due to complexity issues, we will not be officially supporting Windows platforms. As an alternative, please install a Debian-based Linux distro (ie. Ubuntu, Linux Mint, etc) on VirtualBox.

1. Install Python 3 (do **not** install Python 2):

 - For Macs (with homebrew):

 -- Open the terminal

 -- Install homebrew if you have not already:
 `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

 -- Install Python 3 using Brew:

 `brew install python3`

 - For Debian based systems there should already be Python 3 installed. To be sure, type in the following command into the terminal:

  `python3`

  If the terminal does not give you any errors, you are good to go! Else:

  `apt-get install python3` (sudo permissions may be necessary)

2. To ensure that everything goes smoothly, restart your computer. Then, open the terminal and ensure that the correct version of Python is installed by typing in

 For Macs/Linux:

 `python3`

 If you see something like (most importantly, it says Python3.x at the top) this:
 `Python 3.4.0 (default, Apr 11 2014, 13:05:11) `
 `[GCC 4.8.2] on linux `
 ` Type "help", "copyright", "credits" or "license" for  more information.`
 `>>> `

 then you've installed Python 3 successfully! :)

3. Clone repo:
 `git clone https://github.com/kevinlee12/cas.git`

4. Navigate to the cas folder, on Unix/Linux the command is

 `cd cas`

5. Start the virtual environment in the terminal
 - For Debian-based systems:

   `virtualenv -p /usr/bin/python3 env`

 - For Macs:

 `virtualenv -p /usr/local/bin/python3 env`

 It will then do some pip installation to ensure all the dependencies are satisfied

6. Activate the virtual environment

 `source env/bin/activate`

7. Install the required dependencies:

 `pip install -r requirements.txt`

8. Set up the database:

 `django-admin manage.py migrate`

9. Run the server:

 `django-admin manage.py runserver`

 Here the terminal will tell you how to access the website, like http://127.0.0.1:8000/. Copy and paste that link from the terminal into your favorite browser. That's it!

10. To close the server:
 - Press CTRL - C on your keyboard
 - Type `deactivate` into the terminal.

###Zen of Python
>Beautiful is better than ugly.

>Explicit is better than implicit.

>Simple is better than complex.

>Complex is better than complicated.

>Flat is better than nested.

>Sparse is better than dense.

>Readability counts.

>Special cases aren't special enough to break the rules.

>Although practicality beats purity.

>Errors should never pass silently.

>Unless explicitly silenced.

>In the face of ambiguity, refuse the temptation to guess.

>There should be one-- and preferably only one --obvious way to do it.

>Although that way may not be obvious at first unless
you're Dutch.

>Now is better than never.

>Although never is often better than *right* now.

>If the implementation is hard to explain, it's a bad idea.

>If the implementation is easy to explain, it may be a good idea.

>Namespaces are one honking great idea -- let's do more of those!
