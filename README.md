# donation-manager

== installation ==

sudo apt install virtualenvwrapper git
git clone https://github.com/isaaclw/donation-manager.git
mkvirtualenv donation-manager -p /usr/bin/python3
pip install Django
pip install "setuptools!=50.0" --force-reinstall

create a 'app/mysite/local\_settings.py' file with the appropriate key:
SECRET\_KEY = '<some secret password>'

== continued use ==
activate donation-manager
