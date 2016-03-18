from py2neo import authenticate, Graph
import json
from pprint import pprint

def create_city_nodes(list_of_cities):
	for city in list_of_cities:
    	city_to_be_added = graph.merge_one("City", "name", city) 
	return

def create_country_nodes(list_of_countries):
	for country in list_of_countries:
        country_to_be_added = graph.merge_one("Country", "name", country) 
	return

def create_continent_nodes(list_of_continents):
	for continent in list_of_continents:
        continent_to_be_added=graph.merge_one("Continent", "name", continent)
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

def create_entity_nodes():
	with open('data/new.json') as journal_article_file:
		journal_structure = json.load(journal_article_file)

	j_list = []
	a_list = []

	for journal_key, journal_value in journal_structure.items():
		j_list.append(journal_key)
		print(journal_key)
		journal_to_be_added = graph.merge_one("Journal", "name", journal_key)
		for volume_key, volume_value in journal_value.items():
			print('\t' + volume_key)
			for issue_key, issue_value in volume_value.items():
				print('\t\t' + issue_key)
				for issue_attributes_key, issue_attributes_value in issue_value.items():
					# print(issue_attributes_key)
					if issue_attributes_key in "articles":
						for article_key, article_value in issue_attributes_value.items():
							title = journal_structure[journal_key][volume_key][issue_key][issue_attributes_key][article_key]["title"]
							abstract = journal_structure[journal_key][volume_key][issue_key][issue_attributes_key][article_key]["abstract"]
							authors = journal_structure[journal_key][volume_key][issue_key][issue_attributes_key][article_key]["authors"]
							doi = journal_structure[journal_key][volume_key][issue_key][issue_attributes_key][article_key]["doi"]		
							article_to_be_added = graph.merge_one("Article", "doi", doi)
							article_to_be_added['abstract'] = abstract
							article_to_be_added['authors'] = authors
							article_to_be_added['title'] = title
							article_to_be_added.push()
							print(title)
							relationship_to_be_added = graph.create_unique(Relationship(article_to_be_added, "printed_in", journal_to_be_added, volume=volume_key, issue=issue_key, issn=journal_structure[journal_key][volume_key][issue_key]["issn"]))
	return
	
def populate_db():
	with open('config/neo4j_config.json') as config_file:
		config = json.load(config_file)

	authenticate(config['address'], config['username'], config['password'])
	graph = Graph()
	print("Connected to graph...")

	print("Building GEOPHYSICAL nodes in the SciBase Graph!")
	create_geophysical_nodes()

	print("Building MEMBER nodes in the SciBase Graph!")
	create_member_nodes()
	
	print("Building ENTITY nodes in the SciBase Graph!")
	create_entity_nodes()


	return

if __name__ == '__main__':
	populate_db()