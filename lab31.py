#!/usr/env/python3


def main():

    wordbank = ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)

    number = int(input("Enter a number between 0-20"))

    student = tlgstudents[number]

    print(f"{student} always uses {wordbank[2]} {wordbank[1]} to indent")
main()
