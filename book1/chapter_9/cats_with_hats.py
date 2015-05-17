from __future__ import print_function

# outter loop with 100 iterations (i)
# inner loop also with 100 iterations (j)
# on the ith iteration only visit the n*ith cat, where n < 100
number_cats = 100
cats = {}
cat_results = []

for i in xrange(1,number_cats+1):
    for j in xrange(1,number_cats+1):
        if i*j > 100:
            continue
        #print "{} {}".format(i, j)
        if i*j not in cats or cats[i*j] == 0:
            cats[i*j] = 1
        else:
            cats[i*j] = 0
    cat_results.append([])
    for cat in cats:
        cat_results[i-1].append(cats[cat])
        print("{}: {}".format(cat, cats[cat]))

for cat in cats:
    print("{}: {}".format(cat, cats[cat]))

for k in xrange(1,number_cats+1):
    for l in xrange(1,number_cats+1):
        print("{} ".format(cat_results[k-1][l-1]), end="")
    print("")
