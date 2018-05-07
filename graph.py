from py2neo import Node, Relationship, Graph, NodeSelector

def create_indexes(graph=graph):
    graph.run('CREATE INDEX ON :Category(catId)')
    graph.run('CREATE INDEX ON :Category(catName)')
    graph.run('CREATE INDEX ON :Page(pageTitle)')
   
def create_root(category_name, graph=graph):
	graph.run('CREATE (c:Category:RootCategory {{catId:0, catName: "{0!s}", subcatsFetched: false, pagesFetched: false, level: 0}})'.format(category_name))
	   
def expand_categories(graph=graph, levels = 3):

	graph.run('''
			  UNWIND range(0, {level}) as level \n
			  CALL apoc.cypher.doit(" \n
			  MATCH (c:Category {subcatsFetched: false, level: $level}) \n
			  CALL apoc.load.json('https://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers&cmtype=subcat&cmtitle=Category:' + apoc.text.urlencode(c.catName) + '&cmprop=ids%7Ctitle&cmlimit=500') \n
			  YIELD value as results \n
		      UNWIND results.query.categorymembers AS subcat \n
			  MERGE (sc:Category {catId: subcat.pageid}) \n
			  ON CREATE SET sc.catName = substring(subcat.title, 9), \n
              sc.subcatsFetched = false, \n
              sc.pagesFetched = false, \n
              sc.level = $level + 1 \n
			  WITH sc,c \n
			  CALL apoc.create.addLabels(sc,['Level' +  ($level + 1) + 'Category']) YIELD node \n
			  MERGE (sc)-[:SUBCAT_OF]->(c) \n
			  WITH DISTINCT c \n
			  SET c.subcatsFetched = true", { level: level }) YIELD value \n
			  RETURN value \n
			  '''.format(level = levels))


