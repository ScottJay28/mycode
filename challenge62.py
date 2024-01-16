#!/usr/bin/env python 3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


NE_animals = farms[0]["agriculture"]

for animals in NE_animals:
    print(animals)

user_choice = input("pick a farm")

if user_choice == "NE Farm":
    ne_things = farms [0]["agriculture"]
    for things in ne_things:
        print(things)
elif user_choice == "W Farm":
    w_things = farms[1]["agriculture"]
    for things in w_things:
        print(things)
elif user_choice == "SE Farm":
    se_things = farms[2]["agriculture"]
    for things in se_things:
        print(things)
