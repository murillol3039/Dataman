import csv

with open('problems.csv', 'r') as f:

    reader = csv.reader(f)

    problems = f.readline()

    while f != "":
        try:
            problems.append(int(row[0]))
            problems.append(row[1]) 
            problems.append(int(row[2]))
        except:
            pass

    print("Here are the problems from the file: ")

    for item in problems:
        print(item)



