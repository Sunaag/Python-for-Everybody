
fname= input("Enter the filename:")
try:
    fhand= open(fname,'r')
except:
    print("Check the filename again")
    exit()
wordlist= list()
count= dict()
for eachline in fhand:
    line= eachline.rstrip()
    if not line.startswith("From "):
        continue
    else:
        newlist= line.split()
    emails=newlist[1]
    #print(emails)
    wordlist.append(emails)
#print(wordlist)

for eachemail in wordlist:
    count[eachemail]= count.get(eachemail,0)+1
#print(count)

bigword= None
bigcount= None
for word,count in count.items():
    if bigcount is None or count>bigcount:
        bigcount= count
        bigword= word
print(bigword,bigcount)


