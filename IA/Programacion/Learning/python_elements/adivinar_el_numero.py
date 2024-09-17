import random

playing = True
num_random = random.randint(1,100)

while (playing):
    try: 
        num = int(input("Adivine el numero del 1-100\n"))
        if (num == num_random):
            print("Has acertado")
            playing = False
        elif (num < num_random): print("El numero ha adivinar es mayor")
        else: print("Nope, intentalo de nuevo") 
    except: print("Por favor, inserte un numero")