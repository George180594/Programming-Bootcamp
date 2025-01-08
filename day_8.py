# def greet(msg,name):
#     print(msg)
#     print('Sir')
#     print(name)
# greet('Hiii','George')
#     ################
# def life_in_weeks(year):
#     total_weeks= 90*12
#     weeks_left= total_weeks - (year*12)
#     return weeks_left
# life=life_in_weeks(30)
# print(life)
     ####################
# def greet_with(name,location):
#     print(f'Hello {name}')
#     print(f'Whats is it like in {location}')
# greet_with(name= "Jack Bauer",location='Nowhere')
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")



        
