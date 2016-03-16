from py2neo import authenticate, Graph
import json
from pprint import pprint


def create_country_nodes():
	return

def create_city_nodes():
	return

def create_continent_nodes():
	return

def create_article_nodes(article_dict, journal):
	create_article_cypher_query = "MERGE (n:Article {name:{N}}) RETURN n"
	tx = graph.cypher.begin()

	for volume_key, volume_value in article_dict:
		for issue_key, issue_value in article_dict[volume_key]:
			for article in issue_value:
				latest_article_ref = graph.merge_
				tx.append(create_article_cypher_query, {"N":article})
			tx.process()
				# py2neo code for creating new article node.
				# py2neo code for creating relationship between article and journal node using volume & issue info from the corresponding parent loop variables
	return

def create_journal_nodes(journal_structure):
	create_journal_cypher_query = "MERGE (n:Journal {name:{N}}) RETURN n"

	for journal in journal_structure.keys():
		# py2neo code for inserting new journal node.
		article_structure = {k:v for k, v in journal_article(journal)}
		create_article_nodes(article_structure, journal)
	return

def create_geophysical_nodes():
	with open('data/geophysical.json') as geophysical_file:
		geophysical = json.load(geophysical_file)

	print("\t\t CONTINENTS:")
	create_continent_nodes(list(geophysical.keys()))
	print("\t\t COUNTRIES:")
	create_country_nodes(list())
	print("\t\t CITIES:")
	create_city_nodes()
	return

def create_member_nodes():
	with open('data/acm_journal_article.json') as journal_article_file:
		 journal_structure = json.load(journal_article_file)
	
	create_journal_nodes(journal_structure)
	return


	article_list = [article in journal_article[journal_article[vol] for vol in ]]
	create_article_nodes(article_list)
def populate_db():
	with open('config/neo4j_config.json') as config_file:
		config = json.load(config_file)

	authenticate(config['address'], config['username'], config['password'])
	graph = Graph()
	print("Connected to graph")

	print("Building GEOPHYSICAL nodes in the SciBase Graph!")
	create_geophysical_nodes()
	return

if __name__ == '__main__':
	populate_db()