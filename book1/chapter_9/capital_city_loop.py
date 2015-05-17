from capitals import capitals_dict
import random

correct = False
answer = ""

while True:
    state = random.choice(list(capitals_dict))
    answer = raw_input("What is the capital of {}?\n".format(state)).lower()
    if answer == 'exit':
        break
    elif answer == capitals_dict[state].lower():
        correct = True
    else:
        correct = False

if correct:
    print "Correct"
else:
    print "Bye"

