#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Graziano, Daniel Molina Hurtado, Esmail Fadae, Paxton Maeder-York'
SITENAME = "Alzheimer's Disease Diagnosis Prediction"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'ipynb.liquid']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]

# Use the `docs` directory for GitHub pages
OUTPUT_PATH = 'docs/'

# Allow an article to be used for `index.html`
INDEX_SAVE_AS = 'blog.html'

# Flat directory structure
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# No feed clutter
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Use customized theme
THEME = './themes/notmyidea'
CSS_FILE = "override.css"
