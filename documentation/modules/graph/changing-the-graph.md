# Changing the Graph

## `def set_subcategories():`

Given a category or list of categories, create new nodes for subcategories and draw a relationship 'SUBCAT\_OF' from the subcategory to the category that contains it. If depth is greater than 1 then this process continues iteratively, finding subcategories of subcategories.

### Parameters

```python
# This is the graph object to operate on
graph = py2neo.Graph()

# This is a list of categories we want to find the subcategories of
categories = ['str']

# This specifies how far the tree should be expanded
depth = 1
```

## `def set_pages():`

### Parameters

```text
input_list 
```

## `def expand_categories():`

For each page or category in a list, update the graph so that 

#### Examples



