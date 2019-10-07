def main():
    print("1) Answer checker")
    print("2) Memory bank")
    print("3) Number guesser")
    print("4) Exit")
    choice = int(input("Pick an option: "))

    if choice == 1:
          answerChecker()
    elif choice == 2:
          memoryBank()
    elif choice == 3:
          numberGuesser()
    else:
          print("exit")

main()
