django bootstrap registration and faq template layout
====================

A starter project with bootstrapped forms, user registration and debug-toolbar included! It also have a simple FAQ app with a simple WYSIWYG editor based on Twitter's Bootstrap.

Example usage
=============

    $ virtualenv mysite-env --no-site-packages
    $ source mysite-env/bin/activate
    (mysite-env)$ pip install django==1.5.1
    (mysite-env)$ django-admin.py startproject --template=https://github.com/kl4us/django-bootstrap-registration-faq/zipball/master mysite
    (mysite-env)$ cd mysite
    (mysite-env)$ pip install -r requirements.txt
    (mysite-env)$ python manage.py syncdb
    (mysite-env)$ python manage.py runserver

Hit http://127.0.0.1:8000 to view the site!