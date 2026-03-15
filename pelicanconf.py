#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

CACHE_CONTENT = False
IGNORE_FILES = [".#*",
                "*-checkpoint.ipynb",
                "*~"]

AUTHOR = "Virgil Chan"
SITENAME = "Virgil Chan's Blog"
SITEURL = "https://virchan.github.io"

THEME = "attila"

# content paths
PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["blog"]

PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_URL = "category/"
CATEGORIES_SAVE_AS = "category/index.html"

ARTICLE_SAVE_AS = "{date:%Y}/{slug}.html"
ARTICLE_URL = "{date:%Y}/{slug}.html"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = u"uk"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# No tags
TAGS_SAVE_AS = ""
DISPLAY_TAGS_ON_SIDEBAR = False

PYGMENTS_STYLE = "default"

JINJA_ENVIRONMENT = {
  "extensions" :[
    "jinja2.ext.loopcontrols",
    "jinja2.ext.i18n",
    "jinja2.ext.do",
  ]
}

SOCIAL = (
  ("Github", "https://www.github.com/virchan"),
  ("LinkedIn", "https://www.linkedin.com/in/virgil-chan-0a65b11b8/"),
)


MENUITEMS = (
    ("Home", "/"),
             )

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = False
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
PAGE_ORDER_BY = "slug"
DELETE_OUTPUT_DIRECTORY = True

DEFAULT_PAGINATION = False

DEFAULT_DATE_FORMAT = "%d %B %Y"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True