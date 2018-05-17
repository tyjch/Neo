from unittest import TestCase
from unittest.mock import patch
from neo.graph.node import Node, TimeMixin, DataMixin, GraphMixin


class TestNode(TestCase):

    def setUp(self):
        self.node = Node("Title")

    def test_title(self):
        self.assertEqual(self.node.title, "Title")

    def test_primary_label(self):
        self.assertEqual(self.node.__primarylabel__, "Node")

    def test_primary_key(self):
        self.assertEqual(self.node.__primarykey__, "pk")

    def test_primary_value(self):
        self.assertEqual(self.node.__primaryvalue__, "Node:Title")


class TestTimeMixin(TestCase):

    def setUp(self):
        self.timemixin = TimeMixin()

    # TODO: Patch in time to test datetime created

    # TODO: Patch in time to test datetime updated

    def test_primary_label(self):
        self.assertEqual(self.timemixin.__primarylabel__, "TimeMixin")

    def test_primary_key(self):
        self.assertEqual(self.timemixin.__primarykey__, "__id__")

    def test_primary_value(self):
        self.assertEqual(self.timemixin.__primaryvalue__, None)


class TestDataMixin(TestCase):

    def setUp(self):
        self.datamixin = DataMixin()

    def test_primary_label(self):
        self.assertEqual(self.datamixin.__primarylabel__, "DataMixin")

    def test_primary_key(self):
        self.assertEqual(self.datamixin.__primarykey__, "__id__")

    def test_primary_value(self):
        self.assertEqual(self.datamixin.__primaryvalue__, None)


class TestDefaultGraphMixin(TestCase):

    def setUp(self):
        self.graphmixin = GraphMixin()

    # TODO: Patch in database info to test graph id

    def test_primary_label(self):
        self.assertEqual(self.graphmixin.__primarylabel__, "GraphMixin")

    def test_primary_key(self):
        self.assertEqual(self.graphmixin.__primarykey__, "__id__")

    def test_primary_value(self):
        self.assertEqual(self.graphmixin.__primaryvalue__, None)