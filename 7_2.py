# Use the file name mbox-short.txt as the file name
fname= input("Enter filename:")
try:
    fh= open(fname,'r')
except:
    print("Check again.")
    quit()
total=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        value= float(line[len("X-DSPAM-Confidence:"):])
        total = total+value
        count= count+1
print("Average spam confidence:",total/count)

