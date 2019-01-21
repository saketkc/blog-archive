#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Alexandre Vicenzi'
SITEURL = 'http://localhost:8000'
SITENAME = "Alexandre Vicenzi's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'Software Engineer'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '//s.gravatar.com/avatar/5dc5ba59a94eeab2106ad9d397361b2c?s=120'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = '../flex'
PATH = 'content'
TIMEZONE = 'America/New_York'

i18n_templates_lang = 'en'
default_lang = 'en'
og_locale = 'en_us'
locale = 'en_us'

date_formats = {
    'en': '%b %d, %y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (('Portfolio', 'http://alexandrevicenzi.com'),)

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
          ('github', 'https://github.com/alexandrevicenzi'),
          ('google', 'https://google.com/+AlexandreVicenzi'),
          ('twitter', 'https://twitter.com/alxvicenzi'),
          ('rss', '//blog.alexandrevicenzi.com/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./pelican-plugins']
plugins = ['sitemap', 'post_stats', 'i18n_subsites']

jinja_environment = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "alexandrevicenziblog"
ADD_THIS_ID = 'ra-55adbb025d4f7e55'

STATUSCAKE = {
    'trackid': 'SL0UAgrsYP',
    'days': 7,
    'rumid': 6852,
    'design': 6,
}

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-6625957038449899',
    'page_level_ads': True,
    'ads': {
        'aside': '5340595560',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '9584371569',
        'article_top': '',
        'article_bottom': '7257980762',
    }
}
