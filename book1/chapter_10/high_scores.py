import os
import csv

file_path = "/Users/ross/projects/realpython/book1/chapter_10/scores.csv"

with open(file_path, "rb") as file:
    scores = {}
    csv_reader = csv.reader(file)
    next(csv_reader)
    for line in csv_reader:
        name = line[0]
        score = line[1]
        if name in scores and score > scores[name]:
            scores[name] = score
        elif name not in scores:
            scores[name] = score
    
    for name in sorted(scores):
        print "{} {}".format(name, scores[name])
            

