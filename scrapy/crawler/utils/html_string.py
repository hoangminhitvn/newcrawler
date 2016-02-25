from crawler.utils.moduleimport import *
import re

def remove_tags(html):
    # Allow attrs
    allow_attrs = ['src', 'href']
    cleaner = clean.Cleaner(safe_attrs_only=True, safe_attrs=frozenset(allow_attrs))
    results = cleaner.clean_html(html)
    return results


def add_base_url_to_src(base_url, input_html):
    data_output = []
    data_input = re.findall("src=\"(/\\w+/[^\"]+)", input_html)
    for data in data_input:
        if data.startswith("http"):
            data_output.append(data)
        else:
            data_output.append(base_url + data)
    return data_output


