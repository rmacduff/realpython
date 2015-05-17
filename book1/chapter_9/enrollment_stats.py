from __future__ import division

def enrollment_stats(universities):
    students = []
    tuition_fees = []
    for university in universities:
        students.append(university[1])
        tuition_fees.append(university[2])
    return students, tuition_fees

def mean(items):
    total = 0
    for item in items:
        total += item
    return total/len(items)

def median(items):
    items.sort()
    return items[len(items)//2]

universities = [
        ['California Institute of Technology', 2175, 37704], ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732], ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
        ]

students, tuition = enrollment_stats(universities)
print students
print tuition

print "Total students: {}".format(sum(students))
print "Total tuituin: ${}".format(sum(tuition))
print ""
print "Student mean: {}".format(mean(students))
print "Student median: {}".format(median(students))
print ""
print "Tuition mean: {}".format(mean(tuition))
print "Tuition median: {}".format(median(tuition))

