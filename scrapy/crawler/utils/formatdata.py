from crawler.utils.html_string import *
import re


class FormatData:
    @staticmethod
    def description(self, input_value):

        html_desc = None
        html_desc_list = []
        if isinstance(input_value, list):
            for input_v in input_value:
                html_desc_list.append(remove_tags(input_v))
                html_desc = ' '.join(html_desc_list)

            src_url_short = re.findall("src=\"(/\\w+/[^\"]+)", html_desc)
            src_url_full = add_base_url_to_src(base_url=self.base_url, input_html=html_desc)

            if len(src_url_short) > 0:
                for i in src_url_short:
                    for j in src_url_full:
                        if i in j:
                            html_desc = html_desc.replace(i, j)

            return html_desc

        elif isinstance(input_value, unicode):
            return remove_tags(input_value)

    @staticmethod
    def title(self, input_value):
        if isinstance(input_value, list):
            return input_value[0]

    @staticmethod
    def post_date(self, input_value):
        if isinstance(input_value, list):
            return input_value[0]

    @staticmethod
    def image_urls(self, input_value):
        results = []
        if isinstance(input_value, list):
            for url in input_value:
                url = url.encode('utf-8', 'ignore')
                if url.startswith('http'):
                    results.append(url)
                else:
                    results.append(self.base_url + url)

            return '; '.join(results)

    @staticmethod
    def categories(self, input_value):
        if isinstance(input_value, list):
            return '; '.join(input_value)

    @staticmethod
    def tags(self, input_value):
        if isinstance(input_value, list):
            return '; '.join(input_value)
