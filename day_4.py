import random


# Gerar um número inteiro aleatório entre 1 e 10
# for numero in range(5):
#     numero_aleatorio = random.randint(1, 10)
#     print(f"Número aleatório gerado: {numero_aleatorio}")
# random_heads_or_tails= random.randint(0,1)
# if random_heads_or_tails == 0:
#     print('heads')
# else:
#     print('Tails')

# exercise 2 
names=['Jessica','Taylor','Franklin', "Jef",'Steve']
choosen= names[random.randint(0, len(names))]
print(choosen)
# or
print(random.choice(names))
print(random.choices(names)) #cria uma lista