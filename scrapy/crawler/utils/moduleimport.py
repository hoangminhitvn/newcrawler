from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.selector.unified import SelectorList
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor as lxml

from scrapy import FormRequest
from scrapy import Request
from scrapy import log

from langdetect import detect
from urlparse import urljoin

from crawler.items import *
from crawler.utils.formatdata import *

import os
import json
import re
import unicodedata
import locale
import traceback

from crawler.supportclient.cocvu import *
from crawler.supportclient.khothuthuat import *





