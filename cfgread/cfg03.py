#!/usr/bin/env python3


fileSelect = input("Please enter the file you would like to load!")

with open(fileSelect, "r") as configfile:
    configlist = configfile.readlines()
    for line in configlist:
        print(line, end="")
    num_lines = len(configlist)
    print(f"\nNumber of lines in the file: {num_lines}")
print(configlist)
