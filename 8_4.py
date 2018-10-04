fname= input("Enter the filename:")
try:
    fhand=open(fname,'r')
except:
    print("Check again")
wordlist=list()
for eachline in fhand:
    eachline= eachline.rstrip()
    words= eachline.split()
    for eachword in words:
        if not eachword in wordlist:
            wordlist.append(eachword)
        else:
            continue
wordlist.sort()
print(wordlist)


