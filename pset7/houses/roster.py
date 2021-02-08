import cs50
import csv
from sys import argv
from sys import exit
if not (len(argv) == 2 and isinstance(argv[1], str)):
    print("Usage: python roster.py housename")
    exit()
house = argv[1]
db = cs50.SQL("sqlite:///students.db")
table = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house = '{house}' ORDER BY last, first")
for row in table:
    print(row["first"], end=" ")
    if (row["middle"]) != None:
        print(row["middle"], end=" ")
    print(row["last"], end=", ")
    print("born", row["birth"])