# Walkable

## `class Walkable():`

### Instantiation

```python
# You can create a 'walkable' directly from an iterable
walkable = Walkable(iterable)

# You can also create one by concatenating existing graph objects
walkable + other + ...
```

### Traversal

```python
# Yield alternating nodes and relationships; starts and ends on a node
walk(walkable)

# Walks over multiple walkables
walk(*walkables)

# Return the first node encountered on a walk()
walkable.start_node

# Return the last node encountered on a walk()
walkable.end_node

# Return a tuple of all nodes traversed in the order they were encountered 
walkable.nodes

# Return a tuple of all relationships in the order they were encountered
walkable.relationships
```

