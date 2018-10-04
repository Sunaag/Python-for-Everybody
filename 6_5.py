text = "X-DSPAM-Confidence:    0.8475"
search1= text.find('0')

search2= text.find('5',search1)

slicedOut= text[search1:search2+1]
print(float(slicedOut))
