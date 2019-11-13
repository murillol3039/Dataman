def mainMenu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit Program")

    selection = int(input("Please enter a menu choice: "))
    if selection == 1:
        addition()
    elif selection == 2:
        subtraction()
    elif selection == 3:
        multiplication()
    elif selection == 4:
        division()
    elif selection == 5:
        exit
    else:
        print("Error wrong choice. Enter 1-5")
        mainMenu()

def addition():
    try:
        count = 1
        while count <= 2:
            firstNumber = int(input("Please enter a number: "))
            secondNumber = int(input("Please enter a second number: "))
            total = firstNumber + secondNumber
            correctAnswer = int(input("Please enter what you think the answer will be: "))
            print(firstNumber, " + ", secondNumber ," = ", correctAnswer)
            if correctAnswer == total:
                print("- - -- - - = - - - o")
                count = 3
            else:
                print("EEE")
                count+=1
        
        print(firstNumber, " + ", secondNumber ," = ", correctAnswer)
        print("The correct answer is", total)

    except ValueError:
        print("Error. Please enter a number")
        addition()

    option = input("Do you wish to go again? ")
    option = option.lower()

    if option == "y" or option == "yes":      
        addition()
    else:
        print("Have a great day!")


        


def subtraction():
    try:
        count = 1
        while count <= 2:
            firstNumber = int(input("Please enter a number: "))
            secondNumber = int(input("Please enter a second number: "))
            total = firstNumber - secondNumber
            correctAnswer = int(input("Please enter what you think the answer will be: "))
            print(firstNumber, " - ", secondNumber ," = ", correctAnswer)
            if correctAnswer == total:
                print("- - -- - - = - - - o")
                count = 3
            else:
                print("EEE")
                count+=1
        else:
            print(firstNumber, " - ", secondNumber ," = ", correctAnswer)
            print("The correct answer is", total)

    except ValueError:
        print("Error. Please enter a number")
        subtraction()


    option = input("Do you wish to go again? ")
    option = option.lower()

    if option == "y" or option == "yes":      
        subtraction()
    else:
        print("Have a great day!")


def multiplication():
    try:
        count = 1
        while count <= 2:
            firstNumber = int(input("Please enter a number: "))
            secondNumber = int(input("Please enter a second number: "))
            total = firstNumber * secondNumber
            correctAnswer = int(input("Please enter what you think the answer will be: "))
            print(firstNumber, " * ", secondNumber ," = ", correctAnswer)
            if correctAnswer == total:
                print("- - -- - - = - - - o")
                count = 3
            else:
                print("EEE")
                count+=1
        else:
            print(firstNumber, " * ", secondNumber ," = ", correctAnswer)
            print("The correct answer is", total)

    except ValueError:
        print("Error. Please enter a number")
        multiplication()

    option = input("Do you wish to go again? ")
    option = option.lower()

    if option == "y" or option == "yes":      
        multiplication()
    else:
        print("Have a great day!")




def division():
    try:
        count = 1
        while count <= 2:
            firstNumber = int(input("Please enter a number: "))
            secondNumber = int(input("Please enter a second number: "))
            total = firstNumber / secondNumber
            correctAnswer = int(input("Please enter what you think the answer will be: "))
            print(firstNumber, " / ", secondNumber ," = ", correctAnswer)
            if correctAnswer == total:
                print("- - -- - - = - - - o")
                count = 3
            else:
                print("EEE")
                count+=1
        else:
            print(firstNumber, " / ", secondNumber ," = ", correctAnswer)
            print("The correct answer is", total)

    except ValueError:
        print("Error. Please enter a number")
        division()

    option = input("Do you wish to go again? ")
    option = option.lower()

    if option == "y" or option == "yes":      
        division()
    else:
        print("Have a great day!")


if __name__ == "__main__":
    mainMenu()
