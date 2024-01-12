#!/usr/bin/env python3

def main():
    user_name = input("Please enter your name:\n>").title()
    user_date = int(input("PLease enter your birth year in YYYY format:\n>"))
    zodiac_signs = {  (2011, 1999, 1987, 1975, 1963): "Rabbit",
        (2020, 2008, 1996, 1984, 1972, 1960): "Rat",
        (2010, 1998, 1986, 1974, 1962): "Tiger",
        (2021, 2009, 1997, 1985, 1973, 1961): "Ox",
        (2012, 2000, 1988, 1976, 1964): "Dragon",
        (2013, 2001, 1989, 1977, 1965): "Snake",
        (2014, 2002, 1990, 1978, 1966): "Horse",
        (2015, 2003, 1991, 1979, 1967): "Sheep",
        (2016, 2004, 1992, 1980, 1968): "Monkey",
        (2017, 2005, 1993, 1981, 1969): "Rooster",
        (2018, 2006, 1994, 1982, 1970): "Dog",
        (2019, 2007, 1995, 1983, 1971): "Pig"}
    
    for years, sign in zodiac_signs.items():
        if user_date in years:
            print(f"{usr_name} your zodiac sign is {sign}, {get_sign_traits(sign)}.")
            break

def get_traits(sign):
    traits = {"Rabbit": "vigilant, witty, quick-minded, and ingenious",
        "Rat": "artistic, sociable, industrious, charming, and intelligent",
        "Tiger": "courageous, enthusiastic, confident, charismatic, and a leader",
        "Ox": "strong, thorough, determined, loyal, and reliable",
        "Dragon": "talented, powerful, lucky, and successful",
        "Snake": "wise, likes to work alone, and determined",
        "Horse": "animated, active, and energetic",
        "Sheep": "creative, resilient, gentle, mild-mannered, and shy",
        "Monkey": "sharp, smart, curious, and mischievous",
        "Rooster": "hardworking, resourceful, courageous, and talented",
        "Dog": "loyal, honest, cautious, and kind",
        "Pig": "a symbol of wealth, honesty, and practicality"
    }
if __name__ == "__main__":
    main()
