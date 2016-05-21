#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Saket Choudhary'
SITENAME = u'Piddling Pertinent'
SITEURL = 'http://saket-choudhary.me/pertinent-blog'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

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
SOCIAL = (('twitter', 'https://twitter.com/saketkc'),
                    ('github', 'https://github.com/saketkc'),)
DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')
LOAD_CONTENT_CACHE = False
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [ 'ipynb',  'assets', 'sitemap', 'gravatar', 'render_math', 'ipynb']
GOOGLE_ANALYTICS = 'UA-55540107-1'
#GOSQUARED_SITENAME = 'GSN-123456-A'
MENUITEMS = [('Home', 'http://saket-choudhary.me/pertinent-blog'), ('Github', 'https://github.com/saketkc/pertinent-blog/tree/master/content'),
             ('Screening Solutions', 'http://www.saket-choudhary.me/math-screening-solutions'),
             ('Royal Statistical Society GD Solutions', 'http://www.saket-choudhary.me/rss-graduate-diploma-solutions')]
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
