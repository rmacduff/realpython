poem_file = open('poem.txt', 'r')

for line in poem_file.readlines():
    print line

poem_file.close()

with open('poem.txt', 'r') as poem_file:
    for line in poem_file.readlines():
        print line

####################################

with open('poem.txt', 'r') as poem_file, open('output.txt', 'w') as out_file:
    for line in poem_file.readlines():
        out_file.write(line)

with open('poem.txt', 'a') as poem_file:
    poem_file.seek(0,2)
    poem_file.write('\nThis poem has been p0wned\n')
