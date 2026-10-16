# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat6_AlvarezCalvoVictor.py
# El programa realitza una funció que sumi els N primers nombres senars.

def sumar_nombres_senars(N):
    suma = sum(range(1, N * 2, 2))
    print("La suma dels", N, "primers nombres senars és", suma)

N = int(input("Introdueix un número: "))

sumar_nombres_senars(N)
