import random
from day_14_game_data import data,vs,logo

#Format the acoount data into printable format.
def format_data(account):
    """Takes the account data and returns printable format."""
    account_name= account['name']
    account_desc= account['description']
    account_country= account['country']
    return f"{account_name}, a {account_desc}, from {account_country}."

def check_answer(user_guess, a_followers,b_followers):
    """The a usar's guess and the follower count and return if they got it right"""
    if a_followers> b_followers:
        return user_guess =="a"
    else:
        return user_guess =='b'

print(logo)
score=0
game_should_continue= True
account_b= random.choice(data)

#make repeatable.
while game_should_continue:
    #Generate a random account from the game data
    #Making account at position B become the next account at position A.
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f'Compare A: {format_data(account_a)}')
    print(vs)
    print(f'Compare B: {format_data(account_b)}')

    #ask usar for a guess.
    guess= input("\nWho do you think has more followers? Type 'a', or 'b': ").lower()

    #check if usar is corret
    # Get follower count of each account
    a_follower_acount=account_a['follower_count']
    b_follower_acount=account_b['follower_count']

    is_correct= check_answer(guess,a_follower_acount,b_follower_acount)


    #give usar feedback on their guess
    if is_correct:
        score+= 1
        print(f"You are right! Current score: {score}.")

    else:
        print("Sorry,that's wrong. Final score {score}.")
        game_should_continue= False
    #Score keeping

    #Make the game repeatable.

    #making account at position B become next account at position A.
        

    


