#Library's
import random

while True:
    #Entrance
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    #Variables
    difficulty= input("Choose a difficulty, Type 'easy' or 'hard': ")   
    number=random.randint(1,100) #random number to play a game
    print(number)

    #Choose a difficulty
    def level(difficulty):
        if difficulty.lower()=="easy":
            end_game=10
            print('You have 10 attempts ')
            
        elif difficulty.lower()=="hard":
            end_game=5
            print('You have 5 attempts')
        return end_game
            # if end_game==cont_life:
            #     print ("Game Over")
    end_game=level(difficulty) #Triggering function compare
    #Compare guess and number
    def compare(number,end_game):
        count_life=0
        while True:
            guess=int(input('Choose a number: '))

            if guess==number:
                print('You win')
                break
            elif guess!=number:
                
                print(f'You use {count_life+1} attempt out of {end_game}')
                if guess<number:
                    print('Too low')
                    count_life+=1
                    continue
                elif guess>number:
                    print('Too High')
                    count_life+=1
                    continue
                elif count_life==end_game:
                    print('You lose')
                    break
                
    compare(number,end_game) #Triggering function compare

    #Continue the game
    game_on=input('Do you want to play again? (y) or (no): ')  
    if game_on.lower()=='y':
        continue
    else:
        break          

            