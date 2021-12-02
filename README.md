# Code for Foundations of Cryptogrpahy (CSCI662)
This repo contains miscellaneous programs for written by Adam Caulfield (ac7717@rit.edu) for the cryptography course CSCI662

## How to run
They are all python programs which can be executed as python scripts.

## Descriptions

### millerrabin.py
This program tests the Miller-Rabin primality test for odd primes between 100,000 and 115,000.

### modpow.py
This is just a helper file, defining two functions `bruteForce()` and `squareAndMult()`, two methods to do the modular power operator.

### monic.py
This program finds all irreducible monic polynomials (with leading coefficient at x^2 equal to 1) in Z_5[x] of degree 2

### sbox.py
This program simulates the affine mapping step of the sbox, given the defined map on line 13.
