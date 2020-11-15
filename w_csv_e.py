import csv
# experimenting.csv will just be a throwaway spreadsheet that we make probably, and add stuff to it
import pandas as pd
book4 = pd.read_csv("book4.csv", encoding='iso-8859-1')

def getMin(array):
    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return array.index(min)
def getRows(glacier, given_year):
    given_name_rows1 = book4.loc[book4["NAME"] == glacier]
    year_df = given_name_rows1["YEAR"]
    year_difference = []
    for i in range(len(year_df)):
        year_difference.append(abs(year_df[i] - given_year))
    min = getMin(year_difference)
    year_min = year_df[min]
    # min is row of closest year to given year
    final_filter = given_name_rows1.loc[given_name_rows1["YEAR"] == year_min]
    with open('book1.csv', mode='w') as book1:
        book1_writer = csv.writer(book1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        book1_writer.writerow(given_name_rows1.columns)
    final_filter.to_csv("book1.csv", index=False)
    myFile = csv.reader(open('book1.csv'))  # Here your csv file
    lines = list(myFile)
    print(lines)
    lines[1][3] = given_year
    lines[1][8] = str(float(lines[1][8]) - year_difference[min] * 0.075)


getRows("BAHIA DEL DIABLO", 2004)
