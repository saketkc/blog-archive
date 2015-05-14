#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Saket Choudhary'
SITENAME = u'Piddling Pertinent'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = ()
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#         ('Another social link', '#'),)
SOCIAL = ()
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [ 'assets', 'sitemap', 'gravatar', 'render_math']
GOOGLE_ANALYTICS = 'UA-55540107-1'
MENUITEMS = [('Home', 'http://saket-choudhary.me'), ('Github', 'https://github.com/saketkc/pertinent-blog/tree/master/content')]
GITHUB_URL = 'https://github.com/saketkc'
TWITTER_USERNAME = 'saketkc'

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
