hrs=input("Enter Hours:")
try:
	ihrs=int(hrs)
except:
	ihrs=-1

rate=input("Rate per hour:")
try:
	irate=float(rate)
except:
	irate= -1

if ihrs>40:
	pay= 40*irate
	addHrs= ihrs-40	
	irate=irate*1.5
	newPay=addHrs*irate
	totalPay=pay+newPay
	print(totalPay)
elif ihrs<=40:
	pay=ihrs*irate
	print(pay)
