def computepay(h,r):
	if h>40:
		pay= 40*r
		addHrs= h-40	
		r=r*1.5
		newPay=addHrs*r
		totalPay=pay+newPay
		return totalPay
	elif h<=40:
		pay=h*r
		return pay

hrs=float(input("Enter Hours:"))

rate=float(input("Rate per hour:"))

print (computepay(hrs,rate))



    
