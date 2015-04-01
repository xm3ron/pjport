#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#########
# PATHS #
#########
BASEDIR = os.path.dirname(os.path.realpath(__file__))
PATH = 'content'

DOMAIN = None
SITEURL = None

AUTHOR = u''
SITENAME = u''

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'all.rss.xml'
CATEGORY_FEED_RSS = '%s.rss.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('twitter', ''),
    ('linkedin', ''),
    ('facebook', ''),
    ('rss', SITEURL + '/' +FEED_ALL_RSS),
)

DEFAULT_PAGINATION = 10

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('', ''), # this item is to show link on top and bottom of page
)

THEME = None # path to pjport repository clone

###########
# PLUGINS #
###########
PLUGIN_PATHS = [os.path.join(BASEDIR, 'plugins')]
PLUGINS = ['gravatar', 'sitemap', ]

#
# GRAVATAR PLUGIN
#
AUTHOR_EMAIL = None # your gravatar email

#
# SITEMAP PLUGIN
#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_DATE_FORMAT = ('- %d -<br/>%B<br/>%Y')

STATIC_PATHS = ['extra/CNAME', 'extra/robots.txt', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/robots.txt': {'path': 'robots.txt'}, }

#
# pjport theme settings
#


# about me
ABOUT_ME = None # showed on left side of footer

# contacts
CONTACT_EMAIL = None
CONTACT_PHONE = None
CONTACT_CITY = None

# GOOGLE ANALYTICS (set to  None if don't want it)
GOOGLE_ANALYTICS = None
