from __future__ import print_function
from __future__ import division
from random import randint

trials = 10000
total = 0

for i in range(0, trials):
    total += randint(1,6)

avg_roll = total/trials

print("The average number from {} trials is {}".format(trials, avg_roll))
