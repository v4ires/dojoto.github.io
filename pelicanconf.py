#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
BASE = os.path.dirname(__file__)

AUTHOR = u'DojoTO'
AUTHOR_EMAIL = u'gravatar@dojoto.xyz'
SITENAME = u'CodingDojoTocantins'
SITEURL = 'http://dojoto.xyz'
SITELOGO = '{0}/{1}'.format(SITEURL, 'images/dojo-white.png')
MASCOTEDOJO = '{0}/{1}'.format(SITEURL, 'images/ninja-dojo.png')

GITHUB_USERNAME = 'dojoto'
GITHUB_PROJECT = 'dojoto.github.io'
GITHUB_URL = 'https://github.com/{0}/{1}'.format(GITHUB_USERNAME, GITHUB_PROJECT)
DISQUS_SITENAME = 'dojotoinfo'

GOOGLE_ANALYTICS = 'UA-57626842-1'
FACEBOOK_APPID = '741446559283044'

TIMEZONE = 'America/Araguaina'

DEFAULT_LANG = u'pt'

DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
MENUITEMS = (
    ('Arquivo', 'archives.html'),
    ('Quem Somos', 'pages/about.html'),
    # ('Autores', 'authors.html'),
    # ('Categorias', 'categories.html'),
    # ('Tags', 'tags.html'),
)

TEMPLATE_PAGES = {
    os.path.join(BASE, 'theme/templates/search.html'): os.path.join(BASE, 'output/pages/search.html')
}

# Social widget
SOCIAL = (
    ('github', GITHUB_URL),
    ('rss', 'feeds/all.atom.xml'),
)

STATIC_PATHS = ['images', 'extras/CNAME', 'extras/robots.txt']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
    'extras/robots.txt': {'path': 'robots.txt'}
}

# Plugins
PLUGIN_PATHS = [
    'pelican-plugins'
]

PLUGINS = [
    'gravatar',
    'pelican_alias', # para criar alias para artigos
    'sitemap',
    'pelican_youtube', # funciona somente com arquivos rst
    'pelican_vimeo', # funciona somente com arquivos rst
    'gzip_cache', # deve ser o ultimo plugin
    # 'pdf', # funciona somente com arquivos rst

]


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Theme
THEME = 'theme'

# Theme Pure config
PROFILE_IMAGE_URL = "http://res.cloudinary.com/diu8g9l0s/image/upload/v1399566411/fundo_python_a6iqip.png"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Geracao de PDF
# PDF_GENERATOR = True
