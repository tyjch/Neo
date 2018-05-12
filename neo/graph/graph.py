from py2neo import Graph

class Database(object):
    """
    Allows access to a Neo4j graph database

    Main methods:
        default_graph - returns the default Graph exposed by this database

    Main attributes:
        config - a dictionary of configuration parameters used to configure Neo4j
        database_name - the name of the active Neo4j database
        kernel_start_time - the time from which the Neo4j instance was operational
        kernel_version - the version of Neo4j
        store_creation_time - the time the graph store was created
        store_id - the id of the graph store
        uri - the URL to which the database is connected
    """
    def __init__(self):
        # TODO: Write __init__ documentation
        """ Initializes a Database object """
        pass

class ConceptGraph(Graph):
    # TODO: Write class documentation
    """

    """
    def __init__(self):
        # TODO: Write __init__ documentation
        pass

    # TODO: Write Graph methods
