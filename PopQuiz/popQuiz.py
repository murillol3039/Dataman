import csv

f = open('problems.csv', 'r')

reader = csv.reader(f)

problems = []

for row in reader:
    try:
        problems.append([ int(row[0]), row[1], int(row[2]) ])
        firstNum = problems[0]
        print(firstNum)
        for item in problems:
            print(item)
            test = int(input("Pause"))
            
    except:
        pass
    print("done")

print("Here are the problems from the file: ")





