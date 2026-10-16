# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat3_AlvarezCalvoVictor.py
# El programa realitzar una funció a la que se li passen dos sencers 
# i mostra tots els nombres compresos entre ells, ambdós inclosos. 

def mostrar_interval(inici, final):
    for i in range(inici, final + 1):
        print(i, end=" ")

inici = int(input("Dóna'm l'interval d'inici: "))
final = int(input("Dóna'm l'interval de finalització: "))

mostrar_interval(inici, final)
