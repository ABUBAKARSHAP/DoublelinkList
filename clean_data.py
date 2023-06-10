import csv

with open('favorites.csv') as f:
    reader = csv.DictReader(f)
    for rows in reader:
        c = 0
        print(rows['genres'],['Comedy'])
    


