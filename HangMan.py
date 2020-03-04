import random
aga = 1
while aga == 1 :
    game = []
    io = []
    words = {
'City' : ["Bangalore","Delhi","Chennai","Visakhapatnam","Mumbai"], 
'Sport' : ["Cricket","Football","Tennis","Basketball","Batminton"],
'Festival' : ["Diwali","Christmas","Pongal","Onam","Ramzan"]
            }
    
    a = random.randint(0,4)
    
    while True :
        choice = input("Would you like 'City' or 'Sport' or 'Festival' : ").strip().title()
        if choice == "Festival" or choice == "Sport" or choice == "City" :
            game = words[choice][a]
            print(game)
            break
        else :
            print("Enter a right choice.")
            continue
    
    for i in range(len(game)) :
        io.append("_")
    print(io)
    
    tries = 1 
    print("Total No of Tries : 6 ")
    while tries <= 6 :
        
        guess = str(input("Enter your {}th Guess : ".format(tries)).strip().upper())
        while "_" in io :
            print(6 - tries)
            for r in range(len(io)) :
            
                if game[r].upper() == guess :
                    io[r] = guess
                    tries = tries + 1
                    continue
                print(io)
        else :
            print("You Have WON !!")
    
    print("Sorry You Are Out of TRIES !!!")
    while True :
        ag = input("Would you like to Play Again ? : Y/N : ").strip().lower()
        if ag == "y":
            aga = 1
            break
        elif ag == "n" :
            aga = 0
            break
        else :
            print("Either 'Y' or 'N .'")


