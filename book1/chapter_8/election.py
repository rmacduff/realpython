from __future__ import print_function
from __future__ import division
from random import random

elections = 10000

candidate_a_wins = 0
candidate_b_wins = 0

for i in range(0,10000):
    candidate_a_votes = 0
    candidate_b_votes = 0

    if random() <= 0.87:
        candidate_a_votes += 1
    else:
        candidate_b_votes += 1

    if random() <= 0.65:
        candidate_a_votes += 1
    else:
        candidate_b_votes += 1

    if random() <= 0.17:
        candidate_a_votes += 1
    else:
        candidate_b_votes += 1
        
    if candidate_a_votes > candidate_b_votes:
        candidate_a_wins += 1
    else:
        candidate_b_wins += 1


print("Candidate A has a probibility of {}% of winning".format(candidate_a_wins/elections))
print("Candidate B has a probibility of {}% of winning".format(candidate_b_wins/elections))
