---
description: >-
  Interacts with Neo4j using py2neo in order to create, edit and search nodes
  and relationships. Can be used to search for relevant articles as well as
  carry out advanced graph algorithms.
---

# graph

## Module Limitations

In **Neo4j**, operations are handled by a query language called **Cypher**. Although **py2neo **helps us avoid using **Cypher** directly, there are many advanced features that are much easier to carry out in **Cypher **than** Python. **Rather than completely reinventing the wheel, we will provide basic functionality for creating nodes and relationships and querying graphs to pull data into **Python**. If you need more advanced capabilities, I would recommend learning [Cypher](../../../overview/dependencies/neo4j.md). From there you can work directly with **Cypher** scripts or extend **py2neo** or this package if you want to provide a object-oriented interface.

## Wikipedia Structure

In constructing corpora from Wikipedia, we are mainly interested in two things: categories and pages. While pages contain actual content, categories help group related content together. We represent these as nodes in **Neo4j**. There are several ways that these nodes can be related on Wikipedia. 

```text
(Category)-[CONTAINS]->(Category)
(Category)-[CONTAINS]->(Page)
(Category)-[IS_CONTAINED_BY]->(Category)
(Page)-[IS_CONTAINED_BY]->(Category)

(Page)-[LINKS_TO]->(Page)
(Page)-[LINKS_FROM]->(Page)


```





## Creating vs. Querying

There are two main types of operations we will be performing on the graph:

* Creating, editing, deleting nodes and relationships
* Retrieving data from the graph

** **

### Creating







