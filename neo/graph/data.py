from py2neo.ogm import GraphObject

class Node(GraphObject):
    """
    A node in the graph, should only be used to represent nodes that can't be parsed

    Main attributes:
        children - a list of nodes this node is related to
        parents - a list of nodes that contain this node
        depth - minimum number of edges away from a root node
        graph - the graph this node belongs to
    """
    def __init__(self, ):
        pass

class SourceNode(Node):
    """
    Main attributes:
        source - The URL or key associated with this node
        parser - The parser that should be used to parse the data

    Main methods:
        fetch_data - Fetches data from source
        save_data - Saves the data
        load_data - Loads data from saved location
    """

class NodeParser(object):
    """
    Main attributes:
        compatible_labels - The types of SourceNodes able to be parsed

    Main methods:
        parse - Parses data from compatible DataNodes and creates new ParsedNodes
    """

class ParsedNode(Node):
    """
    Main attributes:
        children - A list of Concepts associated with this node
        parent - The SourceNode that was parsed into this one
        parser - The NodeParser used to parse the data
        created - The datetime this node was first created
        updated - The datetime this node was last parsed
        is_stale - True if the parser has been changed
    """

class ParserObserver(object):
    """
    Observes the state of the NodeParser. When it changes, notifies ParsedNodes that have been parsed by it that they
    may need to be parsed again.
    """