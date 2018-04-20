---
description: >-
  Interacts with Neo4j using py2neo in order to create, edit and search nodes
  and relationships. Can be used to search for relevant articles as well as
  carry out advanced graph algorithms.
---

# graph

## `def expand_categories():`

{% tabs %}
{% tab title="From Page" %}
```python
>>> page = 'Set (mathematics)'
>>> categories = expand_categories(page, depth = 1)
>>> print(categories)
['Concepts in logic', 'Mathematical objects', 'Set theory']
```
{% endtab %}

{% tab title="From Pages" %}
```python
>>> pages = ['Set (mathematics)', 'Kernel method']
>>> 
```
{% endtab %}

{% tab title="From Category" %}

{% endtab %}

{% tab title="From Categories" %}

{% endtab %}
{% endtabs %}

## `def expand_pages():`



