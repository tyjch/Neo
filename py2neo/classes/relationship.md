# Relationship

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

