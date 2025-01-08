print('Welcome to the tip calculator!')
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give ?10,12, or 15? "))
people = float(input("How manu people to split the bill?"))
should_pay= (bill* (1+ tip /100))/people
print(f'Each person should pay:{should_pay:0.2f}')
