import random
import requests
import simplejson as json

# Get data from API through link
data = requests.get("http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion.json")

# Convert data to JSON object
data_dict = data.json()

# Get the relevant information needed (only the champions)
only_champions = data_dict['data']

# Randomly select a champion
random_champion = random.choice(list(only_champions))
print("Random champion generated is:", random_champion)
