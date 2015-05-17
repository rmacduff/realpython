from __future__ import print_function
from __future__ import division
from random import randint

trials = 1000

flips = 0
heads, tails = 0, 0

for i in range(0,1000):
    while heads == 0 or tails == 0:
        if randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
        flips += 1
    else:
        heads, tails = 0, 0
        
print("In {} trials there were {} flips, giving an everage of {}".format(trials, flips, flips/trials))
