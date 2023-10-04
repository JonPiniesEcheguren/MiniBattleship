import numpy as np
import random
import functions

tablero = functions.Inicializar_tablero()
print(tablero)
print("\n")

tablero = functions.Colocar_barco(tablero)
print(tablero)
print("\n")

x = int(input("Introduzca las coordenadas \"x\" e \"y\" donde disparar. Coordenada \"x\": "))
y = int(input("Coordenada \"y\": "))
functions.Disparar(tablero, x, y)
print(tablero)
print("\n")

tablero = functions.Generar_b_aleatorio(tablero)
print(tablero)
print("\n")