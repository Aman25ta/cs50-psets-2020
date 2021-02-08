from sys import argv
from sys import exit
import csv
import re

def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit()
    dbase = argv[1]
    seq = argv[2]
    fd = open(f"{dbase}")
    fs = open(f"{seq}")
    fdo = fd.read().rstrip("\n")
    fso = fs.read().rstrip("\n")
    
    with open(dbase, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        db = list(reader)
    vAGATC = count("AGATC", fso)
    vTTTTTTCT = count("TTTTTTCT", fso)
    vTCTAG = count("TCTAG", fso)
    vAATG = count("AATG", fso)
    vGATA = count("GATA", fso)
    vTATC = count("TATC", fso)
    vGAAA = count("GAAA", fso)
    vTCTG = count("TCTG", fso)
    
    if dbase == ("databases/small.csv"):
        for i in range(len(db)):
            if ([db[i]["AGATC"] == str(vAGATC), db[i]["AATG"] == str(vAATG), db[i]["TATC"] == str(vTATC)]):
                name = db[i]["name"]
                break
            else:
                name = "No match"
    else:
        for i in range(len(db)):
            if all([db[i]["AGATC"] == str(vAGATC), db[i]["TTTTTTCT"] == str(vTTTTTTCT), db[i]["TCTAG"] == str(vTCTAG), db[i]["AATG"] == str(vAATG),
                    db[i]["GATA"] == str(vGATA), db[i]["TATC"] == str(vTATC), db[i]["GAAA"] == str(vGAAA), db[i]["TCTG"] == str(vTCTG)]):
                name = db[i]["name"]
                break
            else:
                name = "No match"
    print(name)
    
def count(c, s):
    p = rf'({c})\1*'
    pattern = re.compile(p)
    match = [match for match in pattern.finditer(s)]
    max = 0
    for i in range(len(match)):
        if match[i].group().count(c) > max:
            max = match[i].group().count(c)
    return max

main()