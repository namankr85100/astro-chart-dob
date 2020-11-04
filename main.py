from kerykeion.astrocore import AstroData, Calculator
from kerykeion.output import output
import json

kanye = Calculator("Kanye", 1985, 12, 2, 8, 45, "Atlanta")
# print(kanye)
# y = output(kanye)
# print(y)
# print(kanye.houses()[3]) 
# print(output(kanye))
# Instantiate 
# hname = [] 
# Append new element 
dict1 = {}


for i in range(0,12):
    # hname.append(kanye.planets_house()[i]["name"])
    dict1[kanye.planets_house()[i]["name"]]=kanye.planets_house()[i]["house"]
    # print(kanye.planets_house()[i]["name"]+" "+kanye.planets_house()[i]["house"]) 
    # print(len(hname))

# print(hname)
print(dict1)