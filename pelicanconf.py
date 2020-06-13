#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pelican_jupyter import markup as nb_markup

AUTHOR = "Saket Choudhary"
SITENAME = "Piddling Pertinent"
SITESUBTITLE = "trivially relevant"
SITEDESCRIPTION = "Musings"
SITEURL = "https://saket-choudhary.me"

PATH = "content"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"


TIMEZONE = "America/Los_Angeles"

i18n_templates_lang = "en"
default_lang = "en"
og_locale = "en_us"
locale = "en_us"

date_formats = {"en": "%b %d, %y"}


# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://python.org/'),
#         ('Jinja2', 'https://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = [
    (
        "Probability Screening Solutions",
        "https://www.saket-choudhary.me/usc-math-505A-screening-solutions/",
    ),
    (
        "Stats A Screening Solutions",
        "https://www.saket-choudhary.me/usc-math-541A-screening-solutions/",
    ),
    (
        "Stats B Screening Solutions",
        "https://www.saket-choudhary.me/usc-math-541B-screening-solutions/",
    ),
    (
        "Royal Statistical Society Diploma Solutions",
        "https://www.saket-choudhary.me/rss-graduate-diploma-solutions",
    ),
]

THEME = "pelican-themes/elegant"
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#         ('Another social link', '#'),)
SOCIAL = (
    ("Twitter", "https://twitter.com/saketkc"),
    ("Github", "https://github.com/saketkc"),
    ("Google-Scholar", "https://scholar.google.com/citations?user=BmC4P-oAAAAJ", "google-scholar"),
    ("Stackoverflow", "https://stats.stackexchange.com/users/11668/rightskewed", "mathoverflow"),
    ("CV", "https://www.saket-choudhary.me/resume/saket_cv.pdf", "CV"),
)
DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
MARKUP = ("md", "ipynb")
LOAD_CONTENT_CACHE = False
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}
PLUGIN_PATHS = ["./pelican-plugins", "./plugins/"]
GOOGLE_ANALYTICS = "UA-55540107-1"
COPYRIGHT_YEAR = 2020

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "codehilite"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "true"},
    },
    "output_format": "html5",
}


DEFAULT_PAGINATION = 10

jinja_environment = {"extensions": ["jinja2.ext.i18n"]}
# GOSQUARED_SITENAME = 'GSN-123456-A'
MENUITEMS = [
    ("Home", "https://saket-choudhary.me/pertinent-blog"),
    ("Github", "https://github.com/saketkc/pertinent-blog/tree/master/content"),
]
GITHUB_URL = "https://github.com/saketkc"
TWITTER_USERNAME = "saketkc"

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

## pelican-blue

SIDEBAR_DIGEST = ""

FAVICON = "url-to-favicon"

DISPLAY_PAGES_ON_MENU = True
IPYNB_SKIP_CSS = True


## elegant
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
STATIC_PATHS = ["theme/images", "images"]
PLUGINS = [
    "sitemap",
    "extract_toc",
    "tipue_search",
    "neighbors",
    "assets",
    "share_post",
]
PLUGINS += [
    "render_math",
    nb_markup,
    "post_stats",
    "i18n_subsites",
    "related_posts",
    "series",
    #"minchin.pelican.plugins.cname",
]
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")
LANDING_PAGE_ABOUT = {
    "details": """I am Saket Choudhary. I am currently a PhD student at the University Of Southern California, Los Angeles, where I develop methods to understand post transcriptional regulation.
               I spent the most wonderful years of my life(ever!) at Indian Institute of Technology Bombay graduating with a Bachelors and Masters degree in Chemical Engineering. """,
}
SITE_SUBTITLE = "Trivially Important"
RECENT_ARTICLES_COUNT = 100

PROJECTS = [
    {
        "name": "pysradb",
        "url": "https://github.com/saketkc/pysradb",
        "description": "Python package for interacting with SRAdb and downloading datasets from SRA",
    },
    {
        "name": "pyseqlogo",
        "url": "https://github.com/saketkc/pyseqlogo",
        "description": "Python package to plot sequence logos",
    },
    {
        "name": "sklearn-hogsvd",
        "url": "https://github.com/saketkc/sklearn-hogsvd/",
        "description": "Scikit-learn compatible python implementation of higher order generalized SVD",
    },
]
DISQUS_SITENAME = 'https://piddlingpertinent.disqus.com'
