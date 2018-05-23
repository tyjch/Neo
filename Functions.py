import spacy.tokens as tokens
from py2neo.ogm import GraphObject
from py2neo import Graph

# ===== GRAPH CLASSES ===== #


class Node(GraphObject):

    @property
    def graph(self) -> Graph:
        """
        :return: The graph object associated with this node
        """

    @graph.setter
    def graph(self, graph):
        """
        :param graph: The graph object to be associated with this node
        """

    def create(self): pass

    def delete(self): pass

    def push(self): pass

    def pull(self): pass


# ===== WIKI CLASSES ===== #


class WikiNode(Node):

    @property
    def super_categories(self) -> list:
        """
        :return: A list of super-categories of this wikipedia page
        """

    @property
    def linked_articles(self) -> list:
        """
        :return: A list of wikipedia articles that are linked to
        """


class Article(WikiNode):

    @property
    def type(self) -> str:
        """
        :return: str in ['List', 'Outline', 'Index', 'Types']
        """

    @type.setter
    def type(self, article_type):
        """
        :param article_type: str in ['List', 'Outline', 'Index', 'Types']
        """

    def parse_content(self) -> str:
        """
        :return: str representing parsed content of this article
        """

    def create_doc(self) -> tokens.Doc:
        """
        :return: A spacy Doc creating from parsed content
        """


class Category(WikiNode):

    @property
    def sub_categories(self) -> list:
        """
        :return: sub_categories (list): List of instances of Category
        """


# ===== CORPUS CLASSES ===== #

class Doc(Node):

    @property
    def content(self):
        """
        :return:
        """

    @content.setter
    def content(self, doc):
        """
        :param doc: spacy or textacy Doc
        """

    @property
    def metadata(self, dict):
        """
        :param dict: Sets metadata to dict
        """

    def count(self, terms) -> dict:
        """
        :param terms:
        :return:
        """

class Corpus(Node):

    @classmethod
    def load(cls, filepath):


    @property
    def docs(self):
        """
        :return: Doc nodes that belong to this corpus
        """






