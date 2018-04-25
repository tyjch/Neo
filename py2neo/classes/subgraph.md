# Subgraph

## `class Subgraph():`

### Instantiation

```python
subgraph = Subgraph(nodes, relationships)
```

### Set Operations

Subgraph is the base class for Node, Relationship, and Walkable; therefore they can use these set operations as well.

#### Union

```python
# Returns a new subgraph containing all nodes and relationships in any subgraph
subgraph | other | ...
```

#### Intersection

```python
# Returns a new subgraph containing all nodes and relationships common to all subgraphs
subgraph & subgraph & ...
```

#### Difference

```python
# Returns a new subgraph containing all nodes and relationships in 'subgraph'
# that do not exist in 'other' as well as all nodes that are connected by those
# relationships regardless of whether they are common to 'subgraph' or 'other'
subgraph - other - ...
```

#### Symmetric Difference

```python
# Returns a new subgraph containing all nodes and relationships that exist in
# 'subgraph' or 'other' but not in both, as well as all nodes that are connected
# By those relationships regardless of whether or not they are common to 'subgraph'
# and 'other'
subgraph ^ other ^ ...
```

### Attributes

```python
# Returns the set of all property keys used by nodes and relationships in this subgraph
subgraph.keys()

# Returns the set of all node labels in this subgraph
subgraph.labels()

# Returns the set of all nodes in this subgraph
subgraph.nodes()

# Returns the set of all relationships in this subgraph
subgraph.relationships()

# Returns the set of all relationship types in this subgraph
subgraph.types()

# Returns the number of nodes in the subgraph
order(subgraph)

# Returns the number of relationships in the subgraph
size(subgraph)
```

