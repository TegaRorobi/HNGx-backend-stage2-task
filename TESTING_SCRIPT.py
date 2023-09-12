'''
File to be used to test CRUD operations on the api.

The data for the Create operation can be passed as command line 
arguments, or simply ignored as defaults are put in place.
'''

import requests, argparse
from json import dumps as _

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', help='The name of the Person object to be created through the api')
parser.add_argument('-e', '--email', help = 'The email of the Person object to be created through the api')
parser.add_argument('-b', '--bio', help='The bio of the Person object to be created through the api')

args = parser.parse_args()

if not args.name and not args.email and not args.bio:
	import sys
	print(f"\nThis file comes with a CLI, run `python {sys.argv[0]} -h` to view the help option\n")

# provided name or default value
name = args.name or 'Jonathan Ma'
email = args.email or 'Joma@gmail.com' 
bio = args.bio or 'Tech youtuber.'

# endpoints
list_create = 'http://tegarorobi.pythonanywhere.com/api/persons/'
retrieve_update_destroy = f'http://tegarorobi.pythonanywhere.com/api/persons/{name}/'


print(f"Create Person object: {name}")
persons_create = requests.post(list_create, {
	'name':name, 
	'email':args.email or 'Joma@gmail.com', 
	'bio':args.bio or 'Tech youtuber.'})
if persons_create.status_code == 400:
	import sys 
	sys.exit(_(persons_create.json(), indent=4))
print(_(persons_create.json(), indent=4), '\n\n')

print("Person objects' list:")
persons_list = requests.get(list_create)
print(_(persons_list.json(), indent=4), '\n\n')

print(f"Retrieve Person object: {name}")
person_retrieve = requests.get(retrieve_update_destroy)
print(_(person_retrieve.json(), indent=4), '\n\n')

print(f"Update Person object: {name}")
person_update = requests.patch(retrieve_update_destroy, {'email':'updated@domain.com'})
print(_(person_update.json(), indent=4), '\n\n')

print(f"Delete Person obect: {name}")
person_delete = requests.delete(retrieve_update_destroy)
print('\n')

print("Person objects' list:")
persons_list = requests.get(list_create)
print(_(persons_list.json(), indent=4), '\n\n')