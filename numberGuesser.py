import random

def main():
    
    answer = random.randint(10,99)
    guessing(answer)
    
def guessing(answer):
    try:
        print(answer)
        count = 1
        choice = int(input("Pick a number between 9 and 100: "))

        if choice <= 9 or choice >= 100:
            while choice < 9 or choice > 100:
                choice = int(input("Pick a number between 9 and 100 please: "))
                     
        while choice != answer:
            count += 1
            bottomNumber = random.randint(9,answer -1)
            topNumber = random.randint(answer + 1,100)
            if choice <= 9 or choice >= 100:
                while choice <= 9 or choice >= 100:
                    choice = int(input("Pick a number between 9 and 100 please: "))

            print("The number is between ",bottomNumber," and ",topNumber,".",sep = "")           
            if choice < answer:
                choice = int(input("Pick a number: "))
            elif choice > answer:
                choice = int(input("Pick a number: "))

                
        if count == 1:
            print("Wow, first try. Excellent!")
        elif count > 1:
            print("You have guessed right in",count,"tries.")
        print("")

        option = input("Do you wish to go again? ")
        option = option.lower()

        if option == "y" or option == "yes":      
            main()
        else:
            print("Have a great day!")

    except ValueError:
        print("Error: Data must be a number.")
        guessing(answer)

if __name__ == "__main__":
    main()
