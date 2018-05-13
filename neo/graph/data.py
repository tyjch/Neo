from py2neo.ogm import GraphObject, Property
from neo.graph.graph import default_graph, neo4j
import datetime

class Node(GraphObject):
    """
    A node in the graph, should only be used to represent nodes that can't be parsed

    Main attributes:
        children - a list of nodes this node is related to
        parents - a list of nodes that contain this node
        depth - minimum number of edges away from a root node
        graph - the graph this node belongs to
    """

    title = Property()
    depth = Property()
    graph_id = Property()
    parseable = Property()
    parsed = Property()
    data = Property()
    created = Property()
    updated = Property()

    def __init__(self, title, graph=default_graph, depth=0, label="Node"):
        self.__primarylabel__ = label
        self.title = title
        self.depth = depth
        self.graph_id = neo4j.store_id
        self.parseable = True
        self.parsed = False
        self.graph = graph
        self.data = title  # TODO: Change this
        self.created = str(datetime.datetime.now())
        self.updated = str(datetime.datetime.now())
        graph.push(self)
