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

