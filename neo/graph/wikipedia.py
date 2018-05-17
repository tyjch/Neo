from py2neo.ogm import GraphObject, Property, RelatedTo
from wikipedia import WikipediaPage
from neo.graph.node import Node, TimeMixin, GraphMixin


class WikiNode(Node):

    #__primarykey__ = 'pk'

    def __init__(self, init_title):
        super().__init__(init_title)
        self.label = "WikiNode"
        self.pk = self.label + ':' + init_title
        self.title = init_title


class Article(WikiNode):

    __primarykey__ = 'pk'
    property_depth = Property(key='depth')
    has_article = RelatedTo("Article")

    def __init__(self, title, depth=0):
        super(Article, self).__init__(title, "Article")
        self.property_depth = depth
        self.__primarylabel__ = "Article"

    def get_categories(self):

        article = WikipediaPage(self.title)

        for category in article.categories:
            title = prefix + category
            category = WikiNode(title, self.graph, label="Category")
            category.depth = self.depth + 1

            self.graph.create(category)
            self.graph.push(category)

            self.has_category.add(category)
            self.graph.push(self)


class Category(WikiNode):

    __primarykey__ = 'title'
    property_depth = Property(key='depth')
    has_category = RelatedTo("Category")
    has_article = RelatedTo("Article")

    def __init__(self, title, depth=0):
        super(Category, self).__init__(title, "Category")
        self.property_depth = depth

    def get_categories(self, graph):

        category = WikipediaPage(self.__primarylabel__ + ':' + self.property_title)

        for cat in category.categories:
            category = Category(cat, depth=self.property_depth + 1)
            graph.push(category)

            self.has_category.add(category)
            graph.push(self)

    def get_articles(self, graph):

        category = WikipediaPage(self.__primarylabel__ + ':' + self.property_title)

        for page in category.links:
            article = Article(page, depth=self.property_depth + 1)
            graph.push(article)

            self.has_article.add(article)
            graph.push(self)
