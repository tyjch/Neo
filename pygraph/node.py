from py2neo import Graph, Node, Relationship

graph = Graph(password="password")

def add_node():
    node = Node()
    labels = []
    dictionary = {}

    print("Enter a blank string to finish a section\n")

    print(">>> Labels")
    while True:
        label = input().strip()

        if label == '':
            break
        else:
            node.add_label(label)

    print(">>> Properties")
    while True:
        keyvalue = input()
        kvlist = keyvalue.split(',')

        if keyvalue == '':
            break
        else:
            k = kvlist[0].strip()
            v = kvlist[1].strip()
            node[k] = v

    graph.create(node)

    return node


if __name__ == '__main__':

    node = add_node()
