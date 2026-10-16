# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat2_AlvarezCalvoVictor.py
# El programa realitza una funció que calcula l’àrea d’un triangle base*altura/2.

def calcular_area_triangle(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Introdueix la base: "))
altura = float(input("Introdueix l'altura: "))

area = calcular_area_triangle(base, altura)
print(f"L'àrea d'un triangle amb base {base} i altura {altura} és {area:.2f}")
