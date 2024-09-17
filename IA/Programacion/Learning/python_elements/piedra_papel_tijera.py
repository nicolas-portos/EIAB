import random

playing = True
jugadas = ['piedra', 'papel', 'tijera']

while (playing):
    play_user = str(input("Inserte 'piedra', 'papel' o 'tijera\n")).lower()
    
    if(play_user in jugadas): 
        play_machine = random.choice(jugadas)
        print(f"La maquina ha sacado {play_machine}")

        if(play_user == play_machine): print("Empate")
        elif((play_user == 'piedra' and play_machine == 'tijera') or
             (play_user == 'papel' and play_machine == 'piedra') or
             (play_user == 'tijera' and play_machine == 'papel')):
            print("Has ganado")
        else: print("Has perdido")

        if (input("¿Quieres seguir jugando?, No para dejar de jugar, cualquier otra letra para seguir\n").lower() == 'no'): playing = False

    else: print("Por favor, seleccione una de las 3 opciones")

    