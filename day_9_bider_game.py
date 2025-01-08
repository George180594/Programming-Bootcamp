# import os

def find_highest_bidder(bidding_dictionary):
    winner=''
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount= bidding_dictionary[bidder]
        if bid_amount> highest_bid:
            highest_bid= bid_amount
            winner=bidder
        # or could be
        # max(bidding_dictionary, key=bidding_dictionary.get)
    print(f'The winner is {winner} with a bid of ${highest_bid} .')
continue_bidding= True
bids={}
while continue_bidding:
    name=input('Whats is your name?  ')
    price=int(input('Whats is your bid? $'))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes or no'\n ")
    if should_continue.lower()=='no':
        continue_bidding= False
        print(bids)
        find_highest_bidder(bids)
    elif should_continue.lower()=='yes':
        print("\n"*20)
        # or 
        # os.system("cls")
        



