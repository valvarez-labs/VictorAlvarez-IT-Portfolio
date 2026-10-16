# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat5_AlvarezCalvoVictor.py
# El programa realitza una funció per a fer l’operació a/n.

def calcular_potencia(base, exponent):
    resultat = 1
    for _ in range(exponent):
        resultat *= base
    return resultat

base = int(input("Introdueix la base: "))
exponent = int(input("Introdueix l'exponent: "))

potencia = calcular_potencia(base, exponent)
print(f"El resultat d'elevar {base} a {exponent} és {potencia}")
