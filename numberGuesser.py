import random

def main():
    
    count = 1    
    choice = int(input("Pick a number: "))
    answer = random.randint(1,10)

    while choice != answer:
        count += 1
        
        if choice < answer:
            choice = int(input("Pick a greater number: "))
        elif choice > answer:
            choice = int(input("Pick a lower number: "))

        
    if count == 1:
        print("Wow, first try. Excellent!")
    elif count > 1:
        print("You have guessed right in",count,"tries.")
      
main()
