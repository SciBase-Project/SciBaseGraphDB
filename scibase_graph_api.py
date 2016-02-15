import hug

@hug.get('/hi')
def say_hi():
	return "Hey YOU! :) "

from modules.geophysical import geophysical_methods
__hug__.extend(geophysical_methods, '/geophysical')

from modules.entity import entity_methods
__hug__.extend(entity_methods, '/entity')

from modules.member import member_methods
__hug__.extend(member_methods, '/member')

from modules.computed import computed_methods
__hug__.extend(computed_methods, '/computed')






