# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat4_AlvarezCalvoVictor.py
# El programa Realitza una funció que decideixi si un nombre és parell o senar.

def determinar_parell_senar(numero):
    if numero % 2 == 0:
        print("Aquest número és parell")
    else:
        print("Aquest número és senar")

numero = int(input("Introdueix un número: "))

determinar_parell_senar(numero)

