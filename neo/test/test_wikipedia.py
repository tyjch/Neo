from unittest import TestCase
from neo.graph.wikipedia import WikiNode, Article, Category
from py2neo import Graph


class TestWikiNode(TestCase):

    def setUp(self):
        self.graph = Graph(password="password")
        self.wikinode = WikiNode("Title")

    # Node Parts

    def test_title(self):
        self.assertEqual(self.wikinode.title, "Title")

    def test_primary_label(self):
        self.assertEqual(self.wikinode.__primarylabel__, "WikiNode")

    def test_primary_key(self):
        self.assertEqual(self.wikinode.__primarykey__, "pk")

    def test_primary_value(self):
        self.assertEqual(self.wikinode.__primaryvalue__, "WikiNode:Title")

    def test_pk(self):
        self.assertEqual(self.wikinode.pk, None)

    def test_property_created(self):
        self.assertEqual(self.wikinode.property_created, None)

    def test_property_updated(self):
        self.assertEqual(self.wikinode.property_updated, None)

    def test_property_graph(self):
        self.assertEqual(self.wikinode.graph, "b1abfc987625c719 : 2018-05-13 17:43:55.528000")








