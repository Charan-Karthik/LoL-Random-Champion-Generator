import random
import requests
import simplejson as json

# Get data from API through link
data = requests.get("http://ddragon.leagueoflegends.com/cdn/12.14.1/data/en_US/champion.json")

# Convert data to JSON object
data_dict = data.json()

# Get the relevant information needed (only the champions)
only_champions = data_dict['data']

champion_list = []

for key in only_champions:
    champion_list.append(key)

random_champion = random.choice(champion_list)
print("\nRandom champion generated is:", random_champion, "\n")

# To-Do:
# Add champion roles (top, mid, bot, jungle)
# allow user to select which role to generate a champion for
# create a GUI for the program