import hug

@hug.post('/create_journal_nodes', versions=1)
def create_journal_nodes(values):
	# Code goes here!
	return ()

@hug.post('/create_article_nodes', versions=1)
def create_article_nodes(values):
	# Code goes here!
	return ()

@hug.post('/attach_articles_to_journals', versions=1)
def attach_articles_to_journals(values):
	# Code goes here!
	return ()

@hug.get('/get_journals', versions=1)
def get_journals(values):
	# Code goes here!
	return ()

@hug.get('/get_journals_by_domain', versions=1)
def get_journals_by_domain(values):
	# Code goes here!
	return ()

@hug.get('/get_journals_by_country', versions=1)
def get_journals_by_country(values):
	# Code goes here!
	return ()

@hug.get('/get_journals_by_continent', versions=1)
def get_journals_by_continent(values):
	# Code goes here!
	return ()

@hug.get('/get_journals_by_publisher', versions=1)
def get_journals_by_publisher(values):
	# Code goes here!
	return ()

@hug.get('/get_articles_by_primary_author', versions=1)
def get_articles_by_primary_author(values):
	# Code goes here!
	return ()

@hug.get('/get_articles_by_domain', versions=1)
def get_articles_by_domain(values):
	# Code goes here!
	return ()

@hug.get('/get_articles_by_country', versions=1)
def get_articles_by_country(values):
	# Code goes here!
	return ()

@hug.get('/get_articles_by_continent', versions=1)
def get_articles_by_continent(values):
	# Code goes here!
	return ()

@hug.get('/get_articles_by_journal', versions=1)
def get_articles_by_journal(values):
	# Code goes here!
	return ()

@hug.delete('/delete_journal_nodes', versions=1)
def delete_journal_nodes(values):
	# Code goes here!
	return ()

@hug.delete('/delete_article_nodes', versions=1)
def delete_article_nodes(values):
	# Code goes here!
	return ()

@hug.post('/update_journal_nodes', versions=1)
def update_journal_nodes(values):
	# Code goes here!
	return ()

@hug.post('/update_article_nodes', versions=1)
def update_article_nodes(values):
	# Code goes here!
	return ()

@hug.post('/create_domain', versions=1)
def create_domain(values):
	# Code goes here!
	return ()

@hug.post('/attach_subdomain_to_domain', versions=1)
def attach_subdomain_to_domain(values):
	# Code goes here!
	return ()
