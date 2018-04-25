# NodeSelection

## `class NodeSelection():`

An immutable set of node selection criteria. Acts like a filter on a graph; returns results that meet criteria.

### Instantiation

```text
selection = NodeSelection(graph,
                          labels = frozenset(),
                          conditions = (),
                          order_by = (),
                          skip = None,
                          limit = None)                       
```

### Methods

```python
# Returns the first Node that meets the criteria
first_node = selection.first()

# Limits the maximum number of nodes returned
selection = selection.limit(50)

# Order by the fields or field expressions specified
# '_' represents the current node
selection.order_by("_.name", "max(._a, _.b)")

# Skips the first 'n' nodes in the result
selection.skip(5)



```

## 

