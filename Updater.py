#Reads a text file, splits it into strings at each newline, and alphabetizes
import sys

def alphabetizer():
    newships = open(sys.argv[1], 'rb') #ships to add
    currpage = open(sys.argv[2], 'rb') #current page
    fileout = open(sys.argv[3],'wb') #file to write to
    alphnew = list()
    #alphabetize new ships
    for line in newships:
        alphnew.append(line)
    alphnew = sorted(alphnew, key=lambda s: s.lower()) #case insensitive sort
    inShips = False
    for line in currpage:
        if inShips:
            checkline = line
            if (line.find("<p>") != -1):
                checkline = line[3:] #fragile solution - better is to find start of <p>
            #these check that we have a ship to look for, that it
            #should be subsituted, and that the line has a ship on it
            #workaround for e.g. GymLeaderShipping, that spills onto
            #multiple lines
            #will cause problems with e.g. 3Shi - might want to get rid of
            while ((len(alphnew)>0) and (alphnew[0].lower() < checkline.lower()) and line.find("Shipping") != -1):
                    fileout.write(alphnew.pop(0).strip('\r\n') + "<br>"+"\n")
        fileout.write(line)
        if (line.find("blockquote") != -1):
            inShips = not inShips
        print line
    print("All done!")

alphabetizer()
