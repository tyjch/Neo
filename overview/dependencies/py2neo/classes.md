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
# Returns True if 'relationship' and 'other' are equal based on the IDs of the nodes, and the relationship type
node == other

# Returns True if 'node' and 'other' don't have the same remote ID
node != other
```

```text

```



