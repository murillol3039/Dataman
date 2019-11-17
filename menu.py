import numberGuesser as ng
import AnswerChecker as ac
import memoryBank as mb
import popQuiz as pq

def main():
    print("1) Answer checker")
    print("2) Memory bank")
    print("3) Number guesser")
    print("4) Pop Quiz")
    print("5) Exit")
    choice = int(input("Pick an option: "))

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

main()
