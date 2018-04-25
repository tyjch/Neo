# Schema

## `class Schema():`

### Instantiation

```python
# A Schema is created solely from a Graph object
schema = Schema(graph)
```

### Attributes

```python
# Return the set of node labels currently defined
schema.node_labels

# Return the set of relationship types currently defined
schema.relationship_types
```

### Indexes

```python
# Creating a schema index
schema.create_index(label, *property_keys)

# Removing a label index
schema.drop_index(label, *property_keys)

# Geting indexes
schema.get_indexes(label)
```

### Uniqueness Constraints

```python
# Creating a uniqueness constraint
schema.create_uniqueness_constraint(label, *property_keys)

# Removing a uniqueness constraint
schema.drop_uniqueness_constraint(label, *property_keys)

# Getting uniqueness constraints
schemda.get_uniqueness_constrains(label)
```

