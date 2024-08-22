#Dice Game Involving Money
import random

rules = ("                             1. If you roll both dice and you get the same number on both dice, you |double| your profit and/or intial bet."
         "\n                             2. If you roll both dice and the sum of the dice are less than 10, you lose |50%| of your total earnings and/or intial bet. "
         "\n                             3. If you roll both dice and the sum of the dice are more than 10, you gain |0.5x| on top of your your total earnings and/or initial bet"
         )
first = (f"The rules are the following: \n{rules}")
print(first)

second= input("\nDo you agree with these rules? Please enter yes or no in order to proceed forward: ")

if second.lower() == "no":
    print("Uh oh. We hope to see you around!")
    exit()

elif second.lower() == "yes":
    var = float(input("How much money would you like to bet right now in $? "))
    if var < 15:
        print("\nYou cannot bet less than $15!")
        SystemExit
        
if var >= 15:
        inp2 = input("Would you like to roll both of your dice? Please input yes or no. ")
        if inp2.lower() == "yes":
            dice1 = [1, 2, 3, 4, 5, 6]
            dice2 = [1, 2, 3, 4, 5, 6]
            random1 = random.choice(dice1)
            random2 = random.choice(dice2)
            sum = random1 + random2
            if sum > 10:
                total = float(var * 0.5)
                end = float(total + var)
                grandtotal = round(end, 2)
                print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${grandtotal}!")
                
                rerun = input("Would you like to roll again? Please input yes or no. ")

                if rerun.lower() == "no":
                    print("See you around!")
                    exit()
                
                elif rerun.lower() == "yes":
                    range1 = int(input("How many times would you like to reroll? "))
                    for i in range(range1):
                        
                        random1 = random.choice(dice1)
                        random2 = random.choice(dice2)
                        sum = random1 + random2
                        
                        if sum > 10:
                            var = grandtotal
                            total1 = float(var * 0.5)
                            end = float(total + var)
                            grandtotal = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${grandtotal}!")
                        elif sum < 10:
                            var = grandtotal
                            end = float(var * 0.5)
                            total = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${total}...")
                        if random1 == random2:
                            var = grandtotal
                            end = float(var * 2)
                            total = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you also rolled a {random2}! Your total is now ${total}!") 
                                            
            elif sum < 10:
                end = float(var * 0.5)
                total = round(end, 2)
                print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${total}...")

                rerun2 = input("Would you like to roll again? Please input yes or no. ")

                if rerun2.lower() == "no":
                    print("See you around!")
                    SystemExit
                
                elif rerun2.lower() == "yes":
                    range1 = int(input("How many times would you like to reroll? "))
                    for i in range(range1):
                       
                        random1 = random.choice(dice1)
                        random2 = random.choice(dice2)
                        sum = random1 + random2
                    
                        if sum > 10:
                            var = total
                            total = float(var * 0.5)
                            end = float(total + var)
                            grandtotal = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${grandtotal}!")
                        elif sum < 10:
                            var = total
                            end = float(var * 0.5)
                            total = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${total}...")
                        if random1 == random2:
                            var = total
                            end = float(var * 2)
                            total = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you also rolled a {random2}! Your total is now ${total}!") 
              
            elif random1 == random2:
                end = float(var * 2)
                total = round(end, 2)
                print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you also rolled a {random2}! Your total is now ${total}!")

                rerun3 = input("Would you like to roll again? Please input yes or no. ")

                if rerun3.lower() == "no":
                    print("See you around!")
                    exit()
                
                elif rerun3.lower() == "yes":
                    range1 = int(input("How many times would you like to reroll? "))
                    for i in range(range1):
                       
                      
                        random1 = random.choice(dice1)
                        random2 = random.choice(dice2)
                        sum = random1 + random2
                        
                        if sum > 10:
                            var = total
                            total = float(var * 0.5)
                            end = float(total + var)
                            grandtotal = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${grandtotal}!")
                        elif sum < 10:
                            var = total
                            end = float(var * 0.5)
                            total = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you rolled a {random2}. Your total is now ${total}...")
                        if random1 == random2:
                            var = total
                            end = float(var * 2)
                            total = round(end, 2)
                            print(f"On the first dice, you rolled a {random1}. \nOn the second dice, you also rolled a {random2}! Your total is now ${total}!") 
             
        
        if inp2.lower() == "no":
            print("We hope to see you around! Bye-bye👋")
            exit()
if var <= 0:
    print("Sorry you have nothing left to bet! You are out of money.")

else:
    print("An error has occured. Please try again later!")
