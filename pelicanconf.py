#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Saket Choudhary'
SITENAME = u'Piddling Pertinent'
SITESUBTITLE = 'trivially relevant'
SITEDESCRIPTION = 'Musings'
SITEURL = 'http://saket-choudhary.me/pertinent-blog'

PATH = 'content'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'


TIMEZONE = 'America/Los_Angeles'

i18n_templates_lang = 'en'
default_lang = 'en'
og_locale = 'en_us'
locale = 'en_us'

date_formats = {
    'en': '%b %d, %y',
}


# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = [('Probability Screening Solutions', 'http://www.saket-choudhary.me/usc-math-505A-screening-solutions/'),
         ('Stats A Screening Solutions', 'http://www.saket-choudhary.me/usc-math-541A-screening-solutions/'),
         ('Stats B Screening Solutions', 'http://www.saket-choudhary.me/usc-math-541B-screening-solutions/'),
         ('Royal Statistical Society Diploma Solutions', 'http://www.saket-choudhary.me/rss-graduate-diploma-solutions')]

THEME = 'pelican-themes/Flex'
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
PLUGIN_PATHS = ['../pelican-plugins', './plugins/']
PLUGINS = ['assets', 'sitemap', 'gravatar', 'render_math', 'ipynb.markup', 'post_stats', 'i18n_subsites']
GOOGLE_ANALYTICS = 'UA-55540107-1'
COPYRIGHT_YEAR = 2018

MARKDOWN = {
    'extension_configs': {
                'markdown.extensions.codehilite': {'css_class': 'codehilite'},
                'markdown.extensions.extra': {},
                'markdown.extensions.meta': {},

    },
        'output_format': 'html5',

}


DEFAULT_PAGINATION = 10

jinja_environment = {'extensions': ['jinja2.ext.i18n']}
#GOSQUARED_SITENAME = 'GSN-123456-A'
MENUITEMS = [('Home', 'http://saket-choudhary.me/pertinent-blog'), ('Github', 'https://github.com/saketkc/pertinent-blog/tree/master/content'),]
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

## pelican-blue

SIDEBAR_DIGEST = ''

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True
IPYNB_IGNORE_CSS = True
