from py2neo import authenticate, Graph
import json
from pprint import pprint


def create_country_nodes():
	return

def create_city_nodes():
	return

def create_continent_nodes():
	return

def create_journal_nodes():
	return

def create_article_nodes():
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
	return

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