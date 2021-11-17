import math
from modpow import *
import random as rand
import sys
import numpy as np

def millerrabin(a,p):
	[u,r] = decompose(p)

	z = squareAndMult(a,r,p) #z=(a**r)%p

	if z != 1 and z != p-1:
		for j in range(1, u):
			z = squareAndMult(z,2,p) #z = (z**2)%p
			if z == 1:
				return 0 # Return 0 : NOT PRIME 
		if z!= p-1:
			return 0 # Return 0 : NOT PRIME
	
	return 1 # Return 1 : PRIME

def decompose(p):
	u = 0
	r = 2
	x = p-1
	while(r%2==0):
		u += 1
		r = int(p/(2**u))
	return [u,r]

if __name__ == "__main__":
	# Main, which calls the functions

	# sys.stdout.write("Type an integer, for total times to test each prime: ")
	# total = int(input())
	sys.stdout.write("\n")

	errorsP = [] # p's with the top 10 errors
	errors = [] # top 10 errors
	exp = [] # expected for incorrect guesses
	freqs = [] # freq for incorrect guesses

	# I added all primes (100000, 115000) to this text file
	# in order to get the proper accuracy of M-R algorithm
	primesFile = open("primes.txt","r").read().splitlines()
	primes = []
	for i in range(0,len(primesFile)):
		primes.append(int(primesFile[i]))

	# Iterate through all odd primes between 100,000 and 115,000
	count = 0
	for p in range(100001,115001,2):
		sys.stdout.write("Processing test primes.\tTesting p=%d\tProgress: %d%%   \r" % (p, 100*count/((115000-100001)/2)))
		sys.stdout.flush()
		count += 1		
	
		# Variable expected is the expected result of M-R algorithm, used to get the error later on
		expected = int(np.isin(p, primes, assume_unique=True)) # returns 1 if it is prime, returns 0 if it is not prime

		a_tot = 0 # Variable for the counts of prime/notprime from M-R function 

		# Test all a for the given p
		total = p-4 # total a's is (p-2)-2 = p-4
		for a in range(2,p-1):
		 	a_tot += millerrabin(a,p)
		a_freq = a_tot/total # calculate the frequency of times M-R guessed PRIME

		p_err = abs(expected - a_freq)

		# If error is 0, do not add to list
		if(p_err != 0):
			# Add to list of errors
			if(len(errors)<10):
				# If 10 primes havent been tested, add the p and error to the lists
				errors.append(p_err)
				errorsP.append(p)
				exp.append(expected)
				freqs.append(a_freq)
			else:
				# Find member in the top 10 error list with the smallest error
				minIndex = 0
				for i in range(0, len(errors)):
					if errors[i] < errors[minIndex]:
						minIndex = i
				
				# If the error for this p is larger than the list minimum, replace it
				if(errors[minIndex] < p_err):
					errors[minIndex] = p_err
					errorsP[minIndex] = p
					exp[minIndex] = expected
					freqs[minIndex] = a_freq

		# sys.stdout.write("p=%d \t freq=%.3f\t expected=%d\n" % (p, a_freq,expected))
		
	print("Largest errors:")
	for i in range(0, len(errors)):
		sys.stdout.write("p=%d\terr=%.3f\texp=%d\tfreq=%.3f\n" % (errorsP[i], errors[i], exp[i], freqs[i]))

	# print("Incorrect: "+str(len(errors)))
	# print("Total: "+str(len(primes)))







