score=input("Enter score:")
try:
	fscore=float(score)
except:
	fscore=print("Not sure")
if 0.0 <= fscore <= 1.0:
	if fscore >= 0.9:
		print ("A")
	elif 0.8 <= fscore < 0.9:
		print ("B")
	elif 0.7 <= fscore < 0.8:
		print ("C")
	elif 0.6 <= fscore < 0.7:
		print ("D")
	else:
		print ("F")
else:
	print ("Error: out of range")
