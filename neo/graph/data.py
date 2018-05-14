from py2neo import Database
from py2neo.ogm import GraphObject, Property
import datetime


class Node(GraphObject):

    __primarykey__ = 'pk'

    title = Property()
    pk = Property()

    def __init__(self, title, label="Node"):

        self.title = title
        self.pk = label + ':' + title

        self.__primarylabel__ = label


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


class DefaultGraphMixin(GraphObject):

    graph = Property()

    def __init__(self):

        identifier = Database.store_id
        time_created = Database.store_creation_time

        self.graph = "{} : {}".format(identifier, time_created)

