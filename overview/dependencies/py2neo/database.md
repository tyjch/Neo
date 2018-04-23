# database

## `class Database():`

### Instantiation

```python
# Can be created via an explicit URL
db = Database("bolt://camelot.example.com:7687")

# The default value of 'bolt://localhost:7687' can also be used
default_db = Database()
```

### Attributes

```python
# Returns a dictionary of configuration parameters
db.config

# Returns the name of the active Neo4j database
db.database_name

# Returns the default Graph object in the database
db.default_graph

# Return the time the Neo4j instance became operational
db.kernel_start_time

# Return the version of Neo4j
db.kernel_version

# Return a dictionary of estimates of the numbers of different primitives
db.primitive_counts

# Query the JMX service attached to this database
db.query_jmx(namespace,
             instance=None,
             name=None,
             type=None)
             
# Return the time the Neo4j graph store was created
db.store_creation_time

# Return the Neo4j store directory
db.store_directory

# Return a dictionary of file sizes for each file in the graph store
db.store_file_sizes

# Return an unique ID of the graph store
db.store_id

# Return the URI to which this database is connected
db.uri
```

## `class Graph():`

### Instantiation

```python
# A Graph can be created using default arguments
graph = Graph()

# Parameters can be supplied as keywords
graph = Graph(host='localhost')

# Parameters can also be supplied in the URI scheme
graph = Graph('bolt://localhost:7687')
```

#### Support URI Schemes

| http |
| --- | --- | --- | --- |
| https |
| bolt |
| bolt+routing |

#### Supported Settings

| Keyword | Description | Type | Default |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auth | A 2-tuple of \(user, password\) | tuple | \('neo4j', 'password'\) |
| host | Database server host name | str | 'localhost' |
| password | Password to use for authentication | str | 'password' |
| port | Database server port | int | 7687 |
| scheme | Use a specific URI scheme | str | 'bolt' |
| secure | Use a secure connection \(TLS\) | bool | False |
| user | User to authenticate as | str | 'neo4j' |
| user\_agent | User agent to send for all connections | str | Depends on URI scheme |

### Attributes

```python
# Get the database to which this graph belongs
graph.database
```

### Working with Subgraphs

#### Creating a Subgraph

```python
graph.create(subgraph)
```

#### Deleting a Subgraph

```python
graph.delete(subgraph)
```

#### Deleting all Nodes & Relationships

```python
graph.delete_all()
```

#### Get Total Degree of Nodes

```python
# Get the total degree of all nodes in the subgraph
graph.degree(subgraph)
```



### Cypher



