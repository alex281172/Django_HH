import requests
import pprint

# response_cities = requests.get('http://127.0.0.1:8000/cities-api/cities/')
# response_skills = requests.get('http://127.0.0.1:8000/skills-api/skills/')

response_cities = requests.get('http://127.0.0.1:8000/api/v0/cities/')
response_skills = requests.get('http://127.0.0.1:8000/api/v0/skills/')

pprint.pprint(response_cities.json())
pprint.pprint(response_skills.json())


