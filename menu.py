import numberGuesser as ng
import AnswerChecker as ac
import memoryBank as mb
import popQuiz as pq

def main():
    try:
        print("1) Answer checker")
        print("2) Memory bank")
        print("3) Number guesser")
        print("4) Pop Quiz")
        print("5) Exit")
        choice = int(input("Pick an option: "))

        while choice <1 or choice >5:
            choice = int(input("Pick an option 1-5: "))
    
        if choice == 1:
              ac.mainMenu()

        elif choice == 2:
              mb.memoryBankMenu()

        elif choice == 3:
              ng.main()

        elif choice == 4:
            pq.main()

        else:
              print("exit")
              
    except ValueError:
        print("Error: Data must be a number.")
        main()
        print("")
    main()

main()
