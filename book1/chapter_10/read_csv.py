import csv
import os
import copy

path = "/Users/ross/projects/realpython/book1/chapter_10"
read_file = "pastimes.csv"
write_file = "catagorized_pastimes.csv"

with open(os.path.join(path, read_file), "rb") as input_file, open(os.path.join(path, write_file), "wb") as output_file:
    csv_file_reader = csv.reader(input_file)
    csv_file_writer = csv.writer(output_file)
    #old_header = next(csv_file_reader)
    #print old_header
    header = copy.deepcopy(next(csv_file_reader))
    header.append("Type of Pastime")
    print header
    csv_file_writer.writerow(header)
    for line in csv_file_reader:
        if line[1].lower().find("fighting") >= 0:
            line.append("combat")
        else:
            line.append("other")
        csv_file_writer.writerow(line)

