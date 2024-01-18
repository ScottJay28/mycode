#!/user/bin/python3

import pandas as pd

def main():
    #define xls file
    excel_file = "movies.xls"

    #create DataFrame DF object
    #becasue a sheet wasnt specified only the first shee will be read into DF

    movies = pd.read_excel(excel_file)

    #show the first 5 rows of DF
    #DF has 5 rows and 25 columns
    print(movies.head())

    #choose the first column TITLE as index[0]
    movies_sheet1 = pd.read_excel(excel_file, sheet_name = 0, index_col = 0)

    print(movies_sheet1.head())

    #export 5 movies from the top dataframe to excel
    movies_sheet1.head(5).to_excel("5movies.xlsx")

    #export 5 movies from the top of DF to json
    movies_sheet1.head(5).to_json("5movies.json")

    #export 5 movies from top of DF to CSV
    movies_sheet1.head(5).to_csv("5movies.csv")

if __name__ == "__main__":
    main()
