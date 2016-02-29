import hug

@hug.post('/create_country_nodes', versions=1)
def create_country_nodes(values):
	"""This function call creates COUNTRY type nodes in the graph database. Developer must responsibly ensure that the country being added does indeed exist!"""
	output = []
	for country in values:
		print("Add COUNTRY node: {country}".format(**locals()))
		output.append("{country} added.".format(**locals()))
	return (output)

@hug.post('/create_continent_nodes', versions=1)
def create_continent_nodes(values):
	"""This function call creates CONTINENT type nodes in the graph database. Developer must responsibly ensure that the continent being added does indeed exist!"""
	output = []
	for continent in values:
		print("Add CONTINENT node: {continent}".format(**locals()))
		output.append("{continent} added.")
	return (output)

@hug.post('/attach_countries_to_continent', versions=1)
def attach_countries_to_continent(values):
	"""This function call creates a relationship between a COUNTRY type node and a CONTINENT type node. Developer must respnsibly ensure the correctness of the data being passed to this function"""
	output = []
	for country, continent in values.items():
		print("MAP: {country}\t -> \t{continent}".format(**locals()))
		output.append("Attached {country} to {continent}".format(**locals()))
	return (output)

@hug.get('/get_countries', versions=1)
def get_countries():
	"""This function call returns all the COUNTRY type nodes currently present in the database."""
	# Code goes here! 
	return ("Here are all the countries!")

@hug.get('/get_countries_by_continent', versions=1)
def get_countries_by_continent(continent_name):
	"""This function call returns all the COUNTRY type nodes mapped to a specified CONTINENT type node present in the database."""
	print(continent_name[1:-1])
	# Code goes here! 
	output = {}
	output[continent_name[1:-1]] = "Countries in this continent!"
	return (output)

@hug.get('/get_continents', versions=1)
def get_continents():
	"""This function calls returns all the CONTINENT type nodes in the database"""
	# Code goes here! 
	return ("Here are all the continents!")

@hug.delete('/delete_country_nodes', versions=1)
def delete_country_nodes():
	# Code goes here! 
	return ("All Countries Deleted!")

@hug.delete('/delete_continent_nodes', versions=1)
def delete_continent_nodes():
	# Code goes here! 
	return ("All Continents Deleted!")
