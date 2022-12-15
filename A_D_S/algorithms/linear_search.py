import sys
from load import load_strings

nombres = load_strings(sys.argv[1])

names = [
"Caroline Winters", 
"Maverick Oconnell",
"Yahir Estrada",
"Krish Larson",
"Brianna Chandler",
"Brett Miller",
"Branson Decker",
"Tiara Crane",
"Damaris Patton",
"Cailyn Cline",
"Michelle Huerta",
"Stephany Watkins",
"Morgan Schafer",
"Corbin Ruggiero",
"Reuben Rouse",
"Joseluis Forsythe",
"Natalya Bautista",
"Star Alston",
"Ignacio Mohamed",
"Andrew Stahl",
"Haleigh Farias",
"Siobhan Felder"]

# This funtion takes the python list you want to 
# search through, and a single target you want 
# to search for
def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None
# Loops over the list we're looking for 
for i in names: 
    index = index_of_item(nombres, i) 
    print(index)
