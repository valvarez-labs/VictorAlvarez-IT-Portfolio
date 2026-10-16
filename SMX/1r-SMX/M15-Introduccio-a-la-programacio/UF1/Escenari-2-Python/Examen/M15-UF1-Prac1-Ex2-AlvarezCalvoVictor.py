# Programa fet per Victor A.C  29/01/2024
# El nombre del fitxer sera M15-UF1_Prac1_Ex2_AlvarezCalvoVictor.py
# Programa que demana a l'usuari una paraula i ha de dividir la paraula en dos per la meitat.

variable1 = str(input("Introdueix una paraula: "))
cadena1 = variable1[0:2] #Aquesta linea serveix per separar una paraula de 6 lletres
cadena2 = variable1[2:5] #Aquesta linea serveix per separar una paraula de 6 lletres
print(f"La paraula {variable1} es pot dividir en {cadena1} i {cadena2}")