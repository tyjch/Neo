from py2neo import Database


# TODO: Check if the default database/graph has changed
def get_default_graph():
    database = Database()
    graph = database.default_graph
    return graph



