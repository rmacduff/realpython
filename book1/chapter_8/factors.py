from __future__ import print_function

def factors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print("{} is a divisor of {}".format(i, n))



factors(int(raw_input("Enter a positive integer: ")))
