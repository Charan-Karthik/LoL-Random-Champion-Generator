import random
import requests
import simplejson as json

# Get data from API through link
data = requests.get("http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion.json")

# Convert data to JSON object
data_dict = data.json()

# Get the relevant information needed (only the champions)
only_champions = data_dict['data']

champ_dict = {}

for key, value in only_champions.items():
    champ_dict[value['name']] = []
    
    # Not used (yet!)
    champ_dict[value['name']].append(value['title'])
    champ_dict[value['name']].append(value['info']) 
    champ_dict[value['name']].append(value['tags'])

random_champion = random.choice(list(champ_dict))
print("Random champion generated is:", random_champion)
