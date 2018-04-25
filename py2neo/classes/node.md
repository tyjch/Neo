# Node

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

