# Graph

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

# Get the schema resource for this graph
graph.schema
```

### Transactions

#### Beginning a New Transaction

```text
graph.begin(autocommit=False)
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

#### Check if Subgraphs Exist

```python
# Returns True if all entities exist remotely
# If any nodes or relationships in 'subgraph' do not exist remotely, returns False
graph.exists(subgraph)
```

#### Merge Subgraph

```python
# Merges a subgraph based on matching labels or properties
graph.merge(subgraph, 
            label=None,
            *property_keys)
```

#### Separate Subgraph

```python
# Deletes remote relatinoships that correspond to those in local subgraph
graph.separate(subgraph)
```

### Searching the Graph

#### Matching Relationships

```python
# Matches and returns all relationships with specific criteria
graph.match(start_node=None,
            rel_type=None,
            end_node=None,
            bidirectional=False,
            limit=None)
```

#### Match One Relationship

```python
# Match and return one relationship with specific criteria
graph.math_one(start_node=None,
               rel_type=None,
               end_node=None,
               bidirectional=False)
```

### Pushing and Pulling Data

#### Fetching a Node by ID

```python
# Creates and object representing the remote node with specified ID
# Fetches no data from the server, so no guarantee it exists remotely
graph.node(identity)
```

#### Fetching a Relationship by ID

```python
# Creates and object representing the remote node with specified ID
# Fetches no data from the server, so no guarantee it exists remotely
graph.relationship(identity)
```

#### Pulling from Remote Counterparts

```text
graph.pull(subgraph)
```

#### Pushing to Remote Counterparts

```text
graph.push(subgraph)
```

### Cypher

#### Evaluate a Cypher Query

```python
# Returns the first value from the first record returned or None
graph.evaluate(cypher,
               parameters=None,
               **kwparameters)
```

#### Run a Cypher Query

```python
# Runs a Transaction.run() operation within an autocommit Transaction
graph.run(cypher,
          parameters=None,
          **kwparameters)
```

