import operator
#First define values and operations:
def basic_calculator(number):
    on_off= True
    while on_off:
    
    
        operation={
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul ,
            '/':operator.truediv ,
        }
        pick_operation=input('Pick an operation: ')
        if pick_operation not in operation:
            print('Invalid operation, please choosen again')
            continue
        # else:
        try:
            next_number=float(input("What's the next number?:  "))
        except:
            print('Please, choose a valid number')
            continue
        # if next_number is str:
        #     print('Please, choose a valid number')
        #     next_number=float(input("What's the next number?:  "))
        
        calculation= operation[pick_operation](number,next_number)
        print(calculation)
        save_number=calculation
        new_operation= input(f"Type 'y' to continue with {calculation}, or 'n' to start a new calculation, or tap anything else to finsh:\n")
        if new_operation.lower() =='y':
            number=save_number
            continue
        elif new_operation.lower()=='n':
            return (on_off==True)
        else:
            return (on_off== False)

             
on_off=True                             
while on_off:
    try:
        number=float(input("Digit a number?:  "))
    except:
        print('Please, choose a valid number')
        continue
    on_off=basic_calculator(number)
print('Thanks for playing')