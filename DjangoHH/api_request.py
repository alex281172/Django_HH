import requests
import pprint



# response_cities = requests.get('http://127.0.0.1:8000/api/v0/cities/')
# response_skills = requests.get('http://127.0.0.1:8000/api/v0/skills/')
#
# pprint.pprint(response_cities.json())
# pprint.pprint(response_skills.json())

token = '640e8bd57c579ff197d2932fd157d480503e616c'
headers = {'Authorization': f'Token {token}'}
# response_skills = requests.get('http://127.0.0.1:8000/api/v0/skills/')
response_skills = requests.get('http://127.0.0.1:8000/api/v0/skills/', headers=headers)
# response_skills = requests.get('http://127.0.0.1:8000/api/v0/skills/', auth=('AlexGT', 'r7:VhGGnnPd4C:h'))

pprint.pprint(response_skills.json())

