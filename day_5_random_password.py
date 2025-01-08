# Fizzbuzz game
# for fizzbuzz in range(1,101):
    
#     if (fizzbuzz % 3 == 0) and (fizzbuzz % 5 == 0):
#         fizzbuzz='fizzbuzz'
#     elif (fizzbuzz % 5 == 0):
#         fizzbuzz='buzz'
#     elif (fizzbuzz % 3 == 0):
#         fizzbuzz='fizz'
#     print(fizzbuzz)

##### password generator  #####
import random
import string

####################################
letters_import= string.ascii_letters
l_list= []
for _ in letters_import:
    l_list+=_

numbers_import= string.digits
n_list= []
for _ in numbers_import:
    n_list+=_

symbols_import= string.punctuation
s_list= []
for _ in symbols_import:
    s_list+=_


#####################################

print('Welcome to password generator')

letters= int(input('How many letters would you like in your password?\n'))

random_letters=[]
for r in range(0,letters):
    random_letters+=random.choice(l_list)
# print(random_letters)

numbers= int(input('How many numbers would you like in your password?\n'))
random_numbers=[]
for r in range(0,numbers):
    random_numbers+=random.choice(n_list)
# print(random_numbers)


symbols= int(input('How many symbols would you like in your password?\n'))
random_symbols=[]
for r in range(0,symbols):
    random_symbols+=random.choice(s_list)
# print(random_symbols)


######password######
range_password=letters+symbols+numbers
password= random_letters+random_numbers+random_symbols
# print(password)
random.shuffle(password)
print('sua senha é:', password)
t=''
for p in password:
    t+=p
print('your string password:',t)