# Use words.txt as the file name
fname= input("Enter file name:")
try:
    fh = open(fname,'r')
except:
    print("Check for the file name again")
    quit()
for line in fh:
    line= line.rstrip()
    print(line.upper())


