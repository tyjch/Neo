import textacy
from textacy.datasets import Wikipedia
import wikipedia
from wikipedia import DisambiguationError
import datetime

WP_PATH = textacy.__file__[:-11] + 'data/wikipedia'

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

    return categories;

