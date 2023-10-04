import numpy as np
import random

def Inicializar_tablero():
    tablero = np.full((10, 10), " ")
    return tablero

def Colocar_barco(tablero):
    barco1 = [(0,1), (1,1)]
    barco2 = [(1,3), (1,4), (1,5), (1,6)]
    lista_barcos = [barco1, barco2]
    for i in lista_barcos:
        for j in i:
            tablero[j]= "O"
    return tablero

def Disparar(tablero, x, y):
    if tablero[x,y] == "O":
        print("Acertaste")
        tablero[x,y] = "X"
    else:
        print("Fallaste")
        tablero[x,y] = "-"
    return tablero

def Generar_b_aleatorio(tablero):
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        orientacion = random.choice("NSEO")
        if orientacion == "N":
            limitexn = x - 4
            j = x
        elif orientacion == "S":
            limitexs = x + 4
            j = x
        elif orientacion == "E":
            limiteye = y + 4
            j = y
        elif orientacion == "O":
            limiteyo = y - 4
            j = y
        if x > 3 and orientacion == "N":
            while j > limitexn:
                if tablero[j][y] == "O":
                    break
                else: 
                    pass
                j -= 1
            if j == limitexn:
                tablero[x][y] = "O"
                tablero[x-1][y] = "O"
                tablero[x-2][y] = "O"
                tablero[x-3][y] = "O"
                break
        if x < 7 and orientacion == "S":
            while j < limitexs:
                if tablero[j][y] == "O":
                    break
                else: 
                    pass
                j += 1
            if j == limitexs:
                tablero[x][y] = "O"
                tablero[x+1][y] = "O"
                tablero[x+2][y] = "O"
                tablero[x+3][y] = "O"
                break
        if y < 7 and orientacion == "E":
            while j < limiteye:
                if tablero[j][y] == "O":
                    break
                else: 
                    pass
                j += 1
            if j == limiteye:
                tablero[x][y] = "O"
                tablero[x][y+1] = "O"
                tablero[x][y+2] = "O"
                tablero[x][y+3] = "O"
                break
        if y > 3 and orientacion == "O":
            while j > limiteyo:
                if tablero[j][y] == "O":
                    break
                else: 
                    pass
                j -= 1
            if j == limiteyo:
                tablero[x][y] = "O"
                tablero[x][y-1] = "O"
                tablero[x][y-2] = "O"
                tablero[x][y-3] = "O"
                break
        else:
            pass
    return tablero