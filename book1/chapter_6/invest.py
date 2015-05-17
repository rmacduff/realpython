from __future__ import print_function

def invest(amount, rate, time):
    print("principal amount: ${}".format(amount))
    print("annual rate of return: {}".format(rate))

    for year in range(1,time+1):
        value = amount + amount * rate 
        print("year {}: ${}".format(year, value))
        amount = value

invest(100, 0.05, 8)
invest(2000, 0.025, 5)
