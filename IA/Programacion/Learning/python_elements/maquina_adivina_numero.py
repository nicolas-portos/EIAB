import random

playing, user = True, True
min, max = 1, 100
tries = 1

while(user):
    try: 
        num_adivinar = int(input("Inserte un numero del 1-100\n"))
        user = False
    except: print("Por favor, inserte un numero")

while (playing):
    num_random = random.randint(min,max)
    print(f"has dicho {num_random}")
    if(num_random == num_adivinar):
        print(f"Felicidades, has acertado, te ha llevado {tries} intentos")
        playing = False
    elif (num_random < num_adivinar):
        min = num_random
        print(min)
    elif (num_random > num_adivinar):
        max = num_random
        print(max)
    tries+=1

# Profe
# min, max = 1, 100

# print("Contestas con las teclas '<' '>' '=' segun el numero sea menor, mayor o igual")
# while (playing):
#     num_random = int((min+max)/2)
#     user = input(f"Es {num_random} el numero ha adivinar, contesta con '<' '>' '='\n")
#     if (user == '<'):
#         max = num_random - 1
#     elif (user == '>'):
#         min = num_random + 1
#     elif (user == '='):
#         print("Muy bien, la maquina ha acertado")
#         playing = False