from cs50 import SQL
from csv import reader
from sys import argv
from sys import exit
db = SQL("sqlite:///students.db")
if len(argv) < 2:
    print("usage error, import.py characters.csv")
    exit()
with open(argv[1], newline='') as charactersFile:
    characters = reader(charactersFile)
    for char in characters:
        if char[0] == 'name':
            continue
        fname = char[0].split()
        if len(fname) < 3:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       fname[0], None, fname[1], char[1], char[2])
        else:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       fname[0], fname[1], fname[2], char[1], char[2])