import hug

@hug.post('/', versions=1)
def say_hi(values):
	# Code goes here!
	return ("hi from computed")