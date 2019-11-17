import csv
def main():

    showProblems()

def showProblems():
    f = open('problems.csv', 'r')

    reader = csv.reader(f)

    problems = []

    print("Here are the problems from the file: ")

    for row in reader:
        try:
            problems.append([ int(row[0]), row[1], int(row[2]) ])
        
            for item in problems:
                print(item)
                
        except:
            pass
        


if __name__ == "__main__":
    main()




