# Classes

## `class Node():`

### Instantiation

```python
node = Node(*labels, **properties)
```

### Equality

```python
# Returns True if 'node' and 'other' have the same remote ID
node == other

# Returns True if 'node' and 'other' don't have the same remote ID
node != other
```

### Properties

```python
# Returns the value a property in a node
node[key]

# Set the value of a property in a node
node[key] = value

# Deleting a property in a node
del node[key]

# Return the number of properties in a node
len(node)

# Return a dictionary of the properties in a node
dict(node)
```

### Labels

```python
# Return labels associated with a node
node.labels()

# Return True if a node has a particular label
node.has_label(label)

# Add a label to a node
node.add_label(label)

# Remove a label from a node
node.remove_label(label)

# Remove all labels from a node
node.clear_labels

# Add multiple labels to a node from an iterable
node.update_labels(labels)
```

## `class Relationship():`

### Instantiation

#### Relationship between one node

```python
# Untyped relationship
rel = Relationship(node, **properties)

# Typed relationship
rel = Relationship(node, type, **properties)
```

#### Relationship between two nodes

```python
# Untyped relationship
rel = Relationship(start_node, end_node, **properties)

# Typed relationship
rel = Relationship(start_node, type, end_node, **properties)
```

### Equality

```python
# Returns True if 'relationship' and 'other' are equal
# Based on the IDs of the nodes, and the relationship type
relationship == other

# Returns True if 'relationship' and 'other' don't have the same remote ID
relationship != other
```

### Properties

```python
# Returns the value a property in a relationship
relationship[key]

# Set the value of a property in a relationship
relationship[key] = value

# Deleting a property in a relationship
del relationship[key]

# Return the number of properties in a node
len(node)

# Return a dictionary of the properties in a node
dict(node)
```

### Type

```python
# Return the type of a relationship
type(relationship)
```

## `class PropertyDict():`

### Instantiation

```python
property_dict = PropertyDict(iterable, **kwargs)
```

### Equality

```python
# Returns True if equal to 'other' 
# After all None values are removed from 'other' first
properties == other

# Returns True if unequal to 'other' 
# After all None values are removed from 'other' first
properties != other
```

### Properties

```python
# Returns the value associated with 'key'
# If 'key' is missing, None is returned
properties[key]

# Set the value of a property with 'key'
relationship[key] = value

# If 'key' is in 'properties' return its value
# If not, then insert key with value 'default'
properties.setdefault(key, default=None)

# Adds or overwrites the values with an iterable of key-value pairs
# Or with keyword arguments
# Any value of None will effectively delete the property with that key
properties.update(iterable=None, **kwargs)
```

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
# Return the set of all property keys used by nodes and relationships in this subgraph
subgraph.keys()

# Return the set of all node labels in this subgraph
subgraph.labels()

# 
```

