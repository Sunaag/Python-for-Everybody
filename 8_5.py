fname= input("Enter the filename:")
try:
    fhand=open(fname,'r')
except:
    print("Check Again")
count=0
for eachline in fhand:
    eachline= eachline.rstrip()
    if eachline.startswith("From "):
        line=eachline.split()
        print(line[1])
        count= count+1

print("There were", count, "lines in the file with From as the first word")

