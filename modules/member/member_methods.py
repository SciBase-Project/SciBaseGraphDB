import hug

@hug.post('/create_author_nodes', versions=1)
def create_author_nodes(values):
	# Code goes here!
	return ()

@hug.get('/get_authors', versions=1)
def get_authors(values):
	# Code goes here!
	return ()

@hug.get('/get_authors_by_affiliation', versions=1)
def get_authors_by_affiliation(values):
	# Code goes here!
	return ()

@hug.get('/get_authors_by_origin_country', versions=1)
def get_authors_by_origin_country(values):
	# Code goes here!
	return ()

@hug.get('/get_authors_by_resident_country', versions=1)
def get_authors_by_resident_country(values):
	# Code goes here!
	return ()

@hug.get('/get_authors_by_domain', versions=1)
def get_authors_by_domain(values):
	# Code goes here!
	return ()

@hug.post('/update_author_nodes', versions=1)
def update_author_nodes(values):
	# Code goes here!
	return ()

@hug.delete('/delete_author_nodes', versions=1)
def delete_author_nodes(values):
	# Code goes here!
	return ()

@hug.post('/create_publisher_nodes', versions=1)
def create_publisher_nodes(values):
	# Code goes here!
	return ()

@hug.get('/get_publishers', versions=1)
def get_publishers(values):
	# Code goes here!
	return ()

@hug.get('/get_publishers_by_country', versions=1)
def get_publishers_by_country(values):
	# Code goes here!
	return ()

@hug.get('/get_publishers_by_domain', versions=1)
def get_publishers_by_domain(values):
	# Code goes here!
	return ()

@hug.post('/update_publisher_nodes', versions=1)
def update_publisher_nodes(values):
	# Code goes here!
	return ()

@hug.delete('/delete_publisher_nodes', versions=1)
def delete_publisher_nodes(values):
	# Code goes here!
	return ()

@hug.post('/create_affiliation_nodes', versions=1)
def create_affiliation_nodes(values):
	# Code goes here!
	return ()

@hug.delete('/delete_affiliation_nodes', versions=1)
def delete_affiliation_nodes(values):
	# Code goes here!
	return ()

@hug.get('/get_affiliations', versions=1)
def get_affiliations(values):
	# Code goes here!
	return ()

@hug.get('/get_affiliations_by_country', versions=1)
def get_affiliations_by_country(values):
	# Code goes here!
	return ()

@hug.get('/get_affiliations_by_domains', versions=1)
def get_affiliations_by_domains(values):
	# Code goes here!
	return ()