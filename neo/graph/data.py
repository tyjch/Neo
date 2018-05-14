from py2neo.ogm import GraphObject, Property
from neo.graph.graph import default_graph, neo4j
import datetime

class Node(GraphObject):

    title = Property()
    depth = Property()
    graph_id = Property()

    def __init__(self, title, graph=default_graph, depth=0, label="Node"):
        self.__primarylabel__ = label
        self.title = title
        self.depth = depth
        self.graph_id = neo4j.store_id
        self.graph = graph
        graph.push(self)


class TimeMixin(GraphObject):

    created = Property()
    updated = Property()

    def __init__(self):
        self.created = str(datetime.datetime.now())
        self.updated = str(datetime.datetime.now())


class DataMixin(GraphObject):

    parseable = Property()
    parsed = Property()
    data = Property()

    def __init__(self):
        self.parseable = True
        self.parsed = False
        self.data = None

