from py2neo.ogm import GraphObject, Property, RelatedTo
from wikipedia import WikipediaPage
# from neo.graph.data import NodeParser

# class CategoryNode(WikiNode):
# class ArticleNode(WikiNode):
# class WikiParser(NodeParser):

class WikiNode(GraphObject):

    title = Property()
    depth = Property()

    has_category = RelatedTo("WikiNode")
    has_article = RelatedTo("WikiNode")

    def __init__(self, title, graph, depth=0, label="Article"):
        self.__primarylabel__ = label
        self.title = title
        self.depth = depth
        self.graph = graph
        graph.push(self)

    def get_categories(self):

        wikipage = WikipediaPage(self.title)

        prefix = "Category:"

        for category in wikipage.categories:
            title = prefix + category
            category = WikiNode(title, self.graph, label="Category")
            category.depth = self.depth + 1

            self.graph.create(category)
            self.graph.push(category)

            self.has_category.add(category)
            self.graph.push(self)

    def get_articles(self):

        wikipage = WikipediaPage(self.title)

        # TODO: 'wikipage.links' doesn't return all links when the page is a category

        for article in wikipage.links:
            article = WikiNode(article, self.graph, label="Article")
            article.depth = self.depth + 1

            self.graph.create(article)
            self.graph.push(article)

            self.has_article.add(article)
            self.graph.push(self)
