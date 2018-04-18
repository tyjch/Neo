import textacy
from textacy.datasets import Wikipedia
import wikipedia
from wikipedia import DisambiguationError
import datetime

WP_PATH = textacy.__file__[:-11] + 'data/wikipedia'

class Dataset(Wikipedia):
    def __init__(self, category_filter = set(), title_filter = set()):
        self.category_filter = category_filter
        self.title_filter = title_filter

    def generate_stream(self, category_filter = set(), title_filter = set(), limit = 5, fast = True):
        
        if not Bool(category_filter):
            category_filter = self.category_filter
        if not Bool(title_filter):
            title_filter = self.title_filter

        for record in self.records(limit=limit, fast=fast):
            if record['title'] in title_filter or set(record['categories']) in category_filter:
                yield record
                
    def split_stream(content_field='text'):
        stream = generate_stream(self.category_filter, self.text_filter)
        text_stream, metadata_stream = textacy.io.split_records(stream, content_field)
        return text_stream, metadata_stream
    
    def expand_filters(self,
                       title_filter=None,
                       category_filter=None):
        
        if title_filter is None:
            title_filter = self.title_filter
        if category_filter is None:
            category_filter = self.category_filter
        
        titles, categories = get_related_pages(title_filter,
                                               titles = title_filter,
                                               categories = category_filter)


def get_related_titles(pages, rate_limit=True, min_wait=datetime.timedelta(0, 0, 50000), titles=set()):
    if rate_limit is True:
        wikipedia.set_rate_limiting(True, min_wait)

    for page in pages:
        wikipage = wikipedia.WikipediaPage(page)

        for title in wikipage.links:
            titles.add(title)

    return titles


def get_related_categories(pages, rate_limit=True, min_wait=datetime.timedelta(0, 0, 50000), categories=set()):

    if rate_limit is True:
        wikipedia.set_rate_limiting(True, min_wait)

    for page in pages:
        wikipage = wikipedia.WikipediaPage(page)

        for category in wikipage.categories:
            categories.add(category)

    return categories
