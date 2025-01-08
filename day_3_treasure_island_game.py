print('Welcome to Treasure Island.\n'
'Your mission is to find the treasure.')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

      
''')
while True:
    way_mission=input('You are at cross road. Where do you want to go? left or right \n')
    if way_mission.upper() == 'RIGHT':
        print('Sorry, but you chosse the wrong way. And now you are lost. GAME OVER')
        break
    elif way_mission.upper() == 'LEFT':
        print('Good choice, You find a river.')
        while True:
            way_mission=input('What you gonna do? swin or wait?\n')
            if way_mission.upper() == 'SWIN':
                print('You are crazy?! Swin in an unknown river. GAME OVER')
                break
            elif way_mission.upper() == 'WAIT':
                print('GOOD ISTINCT, looking around you find 2 doors, red door and blue door. ')
                while True:
                    way_mission=input('Wichi door you continue? a red or a blue?\n')
                    if way_mission.upper()== 'BLUE':
                        print('YOU WIN, CONGRATS TO YOU PLAYER')
                        break
                    elif way_mission=='RED':
                        print('NOOOOOO, why red????? You find a big monster. I really dorry for you')
                        break
                    else:
                        print('You choose something wrong. Pleasa, write again')
                        continue
            else:
                print('You choose something wrong. Pleasa, write again')
                continue
            break
    else:
        print('You choose something wrong. Pleasa, write again')
        continue
    break
print('THE END')

    


