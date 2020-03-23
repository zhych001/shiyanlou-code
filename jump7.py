for a in range(1,101):
	if a%7==0:
		continue
	if a%10==7:
		continue
	if a-70>=0 and a-70<10:
		continue
	print(a)

