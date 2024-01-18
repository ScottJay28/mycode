#!/usr/bin/python3

import pandas

def main():

    #create DF from csv data
    superdf = pandas.read_csv("superbirthday.csv")

    # display column names
    print(f"Column names are {', '.join(superdf)}")

    for row in superdf.to_dict(orient='records'):
        print(f"\t{row['name']} aka {row['heroname']}, was born in {row['birthday month']}.")

        print(f"Total lines processed {superdf.shape[0]}")

if __name__ == "__main__":
    main()
