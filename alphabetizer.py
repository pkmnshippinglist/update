#Reads a text file, splits it into strings at each newline, and alphabetizes
import sys

def alphabetizer():
    ships = open(sys.argv[1], 'rb')
    fileout = open(sys.argv[2],'wb')
    output = list()
    for line in ships:
        output.append(line)
    output.sort()
    for line in output:
        fileout.write(line)
    print(len(output))

alphabetizer()
