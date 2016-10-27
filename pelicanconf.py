#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Egi Gundari'
SITENAME = u'egig.org'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = u'id'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

THEME = "themes/egig.org"
THEME_STATIC_DIR = '.'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Subscribe', 'http://eepurl.com/bo4tmb'),
    ('Feed', '/feeds/all.atom.xml'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
