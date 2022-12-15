from json import load
import sys
from tkinter.font import names
from load import load_strings

names = load_strings(sys.argv[1])

search_names = [
"Caroline Winters", "Maverick Oconnell", "Yahir Estrada", "Krish Larson", "Brianna Chandler",
"Brett Miller", "Branson Decker", "Tiara Crane", "Damaris Patton","Cailyn Cline","Michelle Huerta",
"Stephany Watkins", "Morgan Schafer", "Corbin Ruggiero", "Reuben Rouse","Joseluis Forsythe",
"Natalya Bautista", "Star Alston", "Ignacio Mohamed", "Andrew Stahl","Haleigh Farias","Siobhan Felder"
]

# this fuction takes the list we're seaching through and the value we're seaching for 

def binary_string_search(collection, target):
    first = 0
    last = len(collection) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] < target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

for n in search_names:
    index = binary_string_search(names, n)
    print(index)
