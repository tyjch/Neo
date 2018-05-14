from py2neo import Database


def get_default_database():

    default_graph = Database.default_graph

    return default_graph
