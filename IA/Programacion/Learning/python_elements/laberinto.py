import time
import os

#Solo acepta laberintos que empiecen en 0,0  y acaben en el ultimo valor de la matriz

laberinto = [
    [' ', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', 'X', ' ']
]

laberinto[0][0] = 'u' # inicio
linea = 0
columna = 0
max_linea = len(laberinto)-1
max_columna = len(laberinto[0])-1

def printlaberinto():
    time.sleep(0.5)
    os.system("cls")
    for i in laberinto:
        print(i)

while not(linea == max_linea and columna == max_columna):
    
    if columna < max_columna and laberinto[linea][columna+1] != 'X':
        while columna < max_columna and laberinto[linea][columna+1] != 'X':
            laberinto[linea][columna] = ' '
            columna+=1
            laberinto[linea][columna] = 'u'
            printlaberinto()
    else:

        if linea < max_linea and laberinto[linea+1][columna] != 'X':
            while linea < max_linea and laberinto[linea+1][columna] != 'X':
                laberinto[linea][columna] = ' '
                linea+=1
                laberinto[linea][columna] = 'u'
                printlaberinto()
        else:

            if linea > -1 and laberinto[linea-1][columna] != 'X':
                while linea > -1 and laberinto[linea-1][columna] != 'X':
                    laberinto[linea][columna] = ' '
                    linea-=1
                    laberinto[linea][columna] = 'u'
                    printlaberinto()

            else:
                if columna > -1 and laberinto[linea][columna-1] != 'X':
                    while columna > -1 and laberinto[linea][columna-1] != 'X':
                        laberinto[linea][columna] = ' '
                        columna-=1
                        laberinto[linea][columna] = 'u'
                        printlaberinto()
                        
print("Felicidades has ganado")