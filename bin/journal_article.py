# Import libraries used in the script!
from pprint import pprint
from py2neo import authenticate, Graph, Relationship, neo4j
import json

# Read the Neo4j config file for authentication parameters.
with open('config/neo4j_config.json') as config_file:
	config = json.load(config_file)
authenticate(config['address'], config['username'], config['password'])

# Connect to the graph.
graph = Graph()
print("Connected to graph")

# Read the author data structure file for ACM Scraping.
with open('data/acm_author.json') as author_file:
	author_structure = json.load(author_file)

# Create a node for every author of type "Author" storing the first, middle, last and full name. Currently we use the unique ACM Profile link for the author as the unique constraint while creating the node.
for key, value in author_structure.items():
	for record in value:
		link = record['link']
		first_name = record['FName']
		mid_name = record['MName']
		last_name = record['LName']
		full_name = record['FULL Name']

		author_to_be_added = graph.merge_one("Author", "link", link)
		author_to_be_added['full_name'] = full_name
		author_to_be_added['first_name'] = first_name
		author_to_be_added['middle_name'] = mid_name
		author_to_be_added['last_name'] = last_name
		author_to_be_added.push()
		print(record['FULL Name'])

# Read the journal and article data structure file for ACM Scraping
with open('data/acm_journal_article.json') as journal_article_file:
	journal_structure = json.load(journal_article_file)

j_list = []
a_list = []

# Create a node for every journal and article that is encountered in the data structure. Also, a relationship between the journal and article and article and the corresponding authors is created. While creating the relationship between the journal and the article, properties like volume, issue an issn are added to the relationship. Similarly the relationship between an article and its corresponding authors include a "primary" boolean property indicating whether or not the author is a primary author of the corresponding article.
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
						# article_to_be_added['authors'] = authors
						article_to_be_added['title'] = title
						article_to_be_added.push()
						print(title)
						relationship_to_be_added = graph.create_unique(Relationship(article_to_be_added, "printed_in", journal_to_be_added, volume=volume_key, issue=issue_key, issn=journal_structure[journal_key][volume_key][issue_key]["issn"]))
						primary_author_bool = True
						for author in authors:
							if primary_author_bool:
								author_relationship_to_be_added = graph.create_unique(Relationship(article_to_be_added, "authored_by", graph.find('Author', 'full_name', author), primary_author="YES"))
								primary_author_bool = False
							else:
								author_relationship_to_be_added = graph.create_unique(Relationship(article_to_be_added, "authored_by", graph.find('Author', 'full_name', author), primary_author="NO"))
