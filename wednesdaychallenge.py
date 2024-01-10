#!/usr/bin/env/ python3

name = input("What is your name?")

age_input = input("How old are you?")

age = int(age_input)

favmovie = input("What is your favorite movie?")

user_list = [name, age, favmovie]

def greeting():
    print("Hello " + name.capitalize() + " you are " + age + " and your favorite movie is " + favmovie.capitalize() + ".")


greeting()

genre = input("What genre is " + favmovie + "?")

actor = input("Who is your favorite actor in " + favmovie + "?")


def info():
    print("OK " + name.capitalize() + favmovie.capitalize() + " is a " + genre.capitalize() + " movie and your favorite actor is " + actor.capitalize() + ".")

info()

