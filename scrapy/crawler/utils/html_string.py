from crawler.utils.moduleimport import *


def remove_tags(html):
    # Allow attrs
    allow_attrs = ['src', 'href']
    cleaner = clean.Cleaner(safe_attrs_only=True, safe_attrs=frozenset(allow_attrs))
    results = cleaner.clean_html(html)
    return results

