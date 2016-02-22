from crawler.utils.moduleimport import *


class FormatData:
    @staticmethod
    def description(self, input_value):
        if isinstance(input_value, list):
            return ' '.join(input_value)
        elif isinstance(input_value, unicode):
            return input_value.encode('utf-8', 'ignore')

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

            return results

    @staticmethod
    def categories(self, input_value):
        if isinstance(input_value, list):
            return '/'.join(input_value)
