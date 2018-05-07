# NodeSelector

## `class NodeSelector():`

### Instantiation

```python
# Created by a graph
selector = NodeSelector(graph)
```

### Methods

Because this returns a `NodeSelection` instance, you can further refine the selection with`NodeSelection.where()`

```python
# Returns a NodeSelection instance
selected = selector.select(*labels, **properties)
```

