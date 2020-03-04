import random 

print("Try to guess the number between 1 to 20 ... !! \n You have 5 Tries. ")

num = random.randint(1,21)
guess = 1

while True : 
    
    while guess <= 5 :
        tries = int(input("Enter your {}th Guess : ".format(guess)))
    
        if tries == num :
            print("Your have guessed right !! Number : {} on the {}th try.".format(tries,guess))
            break
        elif tries > num :
            print("The number is lower than the number you gussed.")
            guess = guess + 1
            continue
        else :
            print("The number is higher than the number you gussed.")
            guess = guess + 1
            continue
    
    
    again = input("Would you like to play again ?\n If yes press 'Y' : ").strip().lower()
    if again == "y" :
        num = random.randint(1,21)
        guess = 1
        continue
    else :
        break
