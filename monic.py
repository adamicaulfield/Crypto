# Adam Caulfield (ac7717@rit.edu)
# CSCI662 - HW4
# monic.py
# Find all irreducible monic polynomials (with leading coefficient at x^2 equal to 1) in Z_5[x] of degree 2

# Set modulus
p = 5

# Add all monic polynomials to the list
monic = []
for i in range(0, p):
	for j in range(0, p):
		monic.append([i,j,1])

print("Total monic: "+str(len(monic)))
for poly in monic:
	print(poly)

# Test all possible products of all degree 1 polynomials in Z_5[x]
# NOTE : A polynomial f = ax^2 + bx + c is represented as the list [c,b,a]
testPoly = [0,0,0]
print("Testing")
for b2 in range(0,p):
	for b1 in range(0, p):
		for a2 in range(0,p):
			for a1 in range(0, p):
				# Given two degree 1 in Z_5[x] as f1 = a1*x + b1, f2 = a2*x+b2
				# The product f1*f2 = (a1*a2)x^2 + (a1*b2+a2*b1)x + (b1*b2)

				# Don't need to check if polynomial is not monic
				if((a2*a1)%p == 1):
					testPoly[2] = (a2*a1)%p
					testPoly[1] = (a1*b2+a2*b1)%p
					testPoly[0] = (b1*b2)%p

					# If the product is found in the list, remove from master list					
					if(monic.count(testPoly)>0):
						monic.remove(testPoly)
# All polynomials with factors were removed
print("Irreducible polys: "+str(len(monic)))
for poly in monic:
	print(poly)

