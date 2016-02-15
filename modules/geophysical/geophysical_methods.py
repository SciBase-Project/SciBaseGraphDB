import hug

@hug.post('/create_country_nodes', versions=1)
def create_country_nodes(values):
	'''Create country nodes to the GraphDB'''
	# Code goes here!
	return ("Acknowledged!")

@hug.post('/create_continent_nodes', versions=1)
def create_continent_nodes(values):
	# Code goes here! 
	return ()

@hug.post('/attach_countries_to_continent', versions=1)
def attach_countries_to_continent(values):
	# Code goes here! 
	return ()

@hug.get('/get_countries', versions=1)
def get_countries():
	# Code goes here! 
	return ()

@hug.get('/get_countries_by_continent', versions=1)
def get_countries_by_continent():
	# Code goes here! 
	return ()

@hug.get('/get_continents', versions=1)
def get_continents():
	# Code goes here! 
	return ()

@hug.delete('/delete_country_nodes', versions=1)
def delete_country_nodes():
	# Code goes here! 
	return ()

@hug.delete('/delete_continent_nodes', versions=1)
def delete_continent_nodes():
	# Code goes here! 
	return ()
