#!/usr/bin/env python3
def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").lower()


    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()


    marvelchars = {
        "Starlord": {
            "real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"
        },
        "Mystique": {
            "real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"
        },
        "Hulk": {
            "real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"
        }
    }

    if char_name in marvelchars:
        if char_stat in marvelchars[char_name]:
            value = marvelchars[char_name][char_stat]
            if char_stat == "real name":
                value = value.title()
            print(f"{char_name}'s {char_stat} is: {value}")
        else:
            print(f"Invalid char_stat: {char_stat}")
    else:
        print(f"Invalid char_name: {char_name}")


main()

