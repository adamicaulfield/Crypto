def bruteForce(x,e,n):
	# conducts x^e mod n via for loop
	xe = x
	for i in range(0, e-1):
		xe = (xe*x)%n
	return xe

def squareAndMult(x,e,n):
	# compute x^e mod n using squareAndMult
	b = bin(e).replace("0b","")
	t = len(b)	
	r = x
	for i in range(1, t):
		r = (r**2)%n
		if(b[i]=='1'):
			r = (r*x)%n
	return r