import hug

@hug.post('/create_country_nodes', versions=1)
def create_country_nodes(values):
	'''Create country nodes to the GraphDB'''
	# Code goes here!

	return ("Created: " + str(values))

@hug.post('/create_continent_nodes', versions=1)
def create_continent_nodes(values):
	# Code goes here! 
	return ("Created: " + str(values))

@hug.post('/attach_countries_to_continent', versions=1)
def attach_countries_to_continent(values):
	# Code goes here! 
	output = []
	for country, continent in values.items():
		output.append("Attached {country} to {continent}".format(**locals()))
	return (output)

@hug.get('/get_countries', versions=1)
def get_countries():
	# Code goes here! 
	return ("Here are all the countries!")

@hug.get('/get_countries_by_continent', versions=1)
def get_countries_by_continent(continent_name):
	print(continent_name[1:-1])
	# Code goes here! 
	output = {}
	output[continent_name[1:-1]] = "Countries in this continent!"
	return (output)

@hug.get('/get_continents', versions=1)
def get_continents():
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
