def is_leap_year(year):
    def leap_400(year):
        leap1= None
        if year % 400 == 0:
            leap1='Leap'
        else:
            leap1='Not Leap'
        return(leap1)
    def leap_4(year):
        leap2= None
        if year % 4 == 0:
            leap2='Leap'
        else:
            leap2='Not Leap'
        return(leap2)
    def leap_100_400(year):
        leap3= None
        if year % 100 == 0:
            leap3='Not Leap'
            leap3=leap_400(year)
        
        else:
            leap3="Leap"
        return(leap3)
    if leap_4(year)==leap_100_400(year) and leap_4(year)=="Leap":
        print("It's a Leap")
        return (True)
    else:
        print("It's not a Leap year")
        return(False)


# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
is_leap_year(2400)
is_leap_year(1989)
is_leap_year(2000)
is_leap_year(2100)