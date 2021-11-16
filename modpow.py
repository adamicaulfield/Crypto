def modpow(x,e,m):
	# conducts x^e mod m via for loop
	xe = x
	for i in range(0, e-1):
		xe = (xe*x)%m
	return xe