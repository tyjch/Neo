---
description: >-
  Interacts with Neo4j using py2neo in order to create, edit and search nodes
  and relationships. Can be used to search for relevant articles as well as
  carry out advanced graph algorithms.
---

# graph

## `def expand_categories():`

For each page or category in a list, update the graph so that 

#### Examples

{% tabs %}
{% tab title="Pages" %}
```python
>>> page = ['Set (mathematics)']
>>> subcategories = expand_categories(page, depth = 1)
>>> print(subcategories)
['Concepts in logic', 'Mathematical objects', 'Set theory']
```
{% endtab %}

{% tab title="Categories" %}
```python
>>> categories = ['Mathematical objects']
>>> subcategories = expand_categories(categories, depth = 1)

```
{% endtab %}
{% endtabs %}

## `def expand_pages():`



