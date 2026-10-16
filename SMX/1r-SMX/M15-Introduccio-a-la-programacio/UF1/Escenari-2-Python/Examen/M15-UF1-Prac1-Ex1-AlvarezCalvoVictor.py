# Programa fet per Victor A.C  29/01/2024
# El nombre del fitxer sera M15-UF1_Prac1_Ex1_AlvarezCalvoVictor.py
# Programa que demana 2 numeros i dona resultat en boolean

num1 = int(input("Introduiex un primer número: "))
num2 = int(input("Introdueix un segon número "))
print("Resultat comparacions:")

print("-------------------------------")
print(f'{num1} és igual a {num2} ?', {num1} == {num2})
print(f'{num1} és menor a {num2} ?', {num1} < {num2})
print(f'{num1} és major a {num2} ?', {num1} > {num2})
print(f'{num1} és major o igual a {num2} ?', {num1} >= {num2})
print(f'{num1} és diferents a {num2} ?', {num1} != {num2})