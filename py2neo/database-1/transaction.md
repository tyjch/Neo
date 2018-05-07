# Transaction

## `class Transaction():`

### Initialization

```python
# Created from a Graph object with graph.begin()
transaction = graph.begin()
```

### Transaction Actions

```python
# Commit a transaction
transaction.commit()

# Indicate whether or not this transaction has been completed
transaction.finished()

# Send all pending statements to the server for processing
transaction.process()

# Undo all actions previously taken in current transaction
transaction.rollback()
```

### Using Subgraphs

```python
# Creating remote nodes & relationships
transaction.create(subgraph)

# Deleting remote nodes & relationships
transaction.delete(subgraph)

# Return the total number of relationships attached to all nodes
transaction.degree(subgraph)

# Check if all entities in 'subgraph' exist remotely
transaction.exists(subgraph)

# Merge nodes & relationships from local subgraph into database
transaction.merge(subgraph,
                  primary_label=None,
                  primary_key=None)

# Delete remote relationships that correspond to those in the local subgraph
transaction.separate(subgraph)
```

### Pushing and Pulling Data

```python
# Push data from subgraph to remote counterparts
transaction.push(subgraph)

# Pull data into subgraph from remote counterparts
transaction.pull(subgraph)
```

### Using Cypher

```python
# Execute a single Cypher statement
transaction.evaluate(cypher,
                     parameters=None,
                     **kwparameters)
                      
# Send a Cypher statement to the server for execution
# Returns a cursor to navigate the result
transaction.run(cypher,
                parameters=None,
                **kwparameters)
                
```

