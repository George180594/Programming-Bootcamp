import random
import os


#Define variables
j=10
q=10
k=10


som_cards=0 
cards_begin=["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,j,j,j,j,q,q,q,q,k,k,k,k]
cards_end=cards_begin.copy
hand_pc= None

def mod_a(hand_player,sum_card): #####Title: Def to modify Ás value

    if "A" in hand_player:
        hand_player.remove('A')
        if sum_card<=10:
            hand_player.append(11)
        else:
            hand_player.append(1)
    else:
        pass
    return hand_player 

def auto_lose(sum_hand): #If player exceeds 21, automatically lose
    if sum_hand > 21:
        print(f'Your hand - {sum_hand} exceeds 21 point')
        print('Try again next time, you Lose:')
        return False
    else:
        return True
def player(cards):
    # title: Def to creat a loop to choose a random number
    game_on=True
    som_cards=0
    hand_player=[]
    while game_on:
        print()
        choice_player=input('Player, do you want a card? (y) or (n) :\n')
        os.system('cls') 
        if choice_player.lower()=="y":
            card=random.choice(cards)
            hand_player.append(card)
            hand=mod_a(hand_player,som_cards)
            cards.remove(card)
            print()
            print("Your hand:")
            for h in hand:
                print(h, end=',')
            print()
            som_cards=sum(hand)
            print(f'Total:{som_cards}')
            game_on=auto_lose(som_cards)
            continue 
        else:
            print()
            break
    print(f"Your hand is {hand_player} and your som are {som_cards}")
    return (som_cards)
def pc(cards):
    # title: Def to creat a loop to choose a random number
    som_cards=0
    hand_player=[]
    try_pc= random.randint(1,6)
    for t in range(try_pc): 
        card=random.choice(cards)
        hand_player.append(card)
        hand=mod_a(hand_player,som_cards)
        cards.remove(card)
        som_cards=sum(hand)
    if som_cards> 21:
        print('PC exceed 21, The machine lose')  
    print()  
    print(f"PC hand is {hand_player} and It som is {som_cards}")         
    return (som_cards)

total_player=player(cards_begin)

total_pc=pc(cards_begin)

def who_win(total_player,total_pc):
    if total_player>total_pc and total_player<=21:
        print("The player win")
    elif total_player<total_pc and total_pc<=21:
        print("The machine win")
    if total_player==total_pc and (total_player>21 and total_pc>21) :
        print("DRAW")
who_win(total_player,total_pc)



    