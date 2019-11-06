import csv

f = open('problems.csv', 'r')

reader = csv.reader(f)

problems = []

for row in reader:
    try:
        problems.append([ int(row[0]), row[1], int(row[2]) ])
    except:
        pass

print("Here are the problems from the file: ")

for item in problems:
    print(item)



