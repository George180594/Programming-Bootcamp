import json

def time_principal():
    have_player=True
    player_dict = {}
    time_1={}
    time_2={}

    cont = 1


    while have_player:
        if cont<=10:
            valor = input(f'{cont}-Name:')
            player_dict[cont] = valor
            if cont%2==0:
                time_1[cont] = valor
            else:
                time_2[cont]= valor
            cont += 1
            with open("times.json",'w') as data_file:
                data_file.write(f"Total primeiros times:{player_dict}\n")
                data_file.write(f"time 1: {time_1}\n")
                data_file.write(f"time 2: {time_2}\n")
                
        elif cont==20:
            valor = input(f'{cont}-Name:')
            player_dict[cont] = valor
        return player_dict, time_1, time_2   

def win_lose():
    win_or_lose= input("Quem ganhou: time 1 ou 2")
    if win_lose==1:
        ...







