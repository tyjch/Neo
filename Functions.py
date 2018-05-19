class WikiNode: pass
class Article: pass
class Category: pass

def get_article_kind(article: Article) -> str:
    """
    :param article := Article()
    :return: str in ['List', 'Outline', 'Index', 'Types'
    """
    pass

def get_super_categories(wikinode: WikiNode) -> list:
    """
    Args:
        wikinode (WikiNode): Instance of WikiNode or its subclasses

    Returns:
        super_categories (list): List of instances of Category
    """

def get_sub_categories(category: Category) -> list:
    """
    Args:
        category (Category): Instance of Category or its subclasses

    Returns:
        sub_categories (list): List of instances of Category
    """

def get_related_pages(wikinode: WikiNode) -> list:
    """
    Args:
        wikinode (WikiNode): Instance of WikiNode or its subclasses

    Returns:
        articles (list): List of instances of Article
    """

def parse_node(article: Article) -> str:
    """
    Args:
        article (Article): Instance of Article

    Returns:
        parsed_article (str): String representing parsed article
    """

def