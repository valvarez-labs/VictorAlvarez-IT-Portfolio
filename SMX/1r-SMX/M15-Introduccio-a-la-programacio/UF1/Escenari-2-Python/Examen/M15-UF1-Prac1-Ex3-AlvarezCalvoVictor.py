# Programa fet per Victor A.C  29/01/2024
# El nombre del fitxer sera M15-UF1_Prac1_Ex3_AlvarezCalvoVictor.py
# Programa que calcula el dret a la avaluacio de la UF d'un Modul.

print("PROGRAMA QUE CALCULA LA PÈRDUA DEL DRET D'AVALUACIÓ D'UNA UF ")
print("************************************************************") 
variable1 = str(input("Quina UF de quin mòdul vols saber?"))
variable2 = int(input("Quantes hores te aquesta UF?: "))
variable3 = (variable2)*0.20    #Aixó serveix per calcular el percentatge (el 0.20 equival al percenatge donat al exercici)
variable4 = int(variable3)      #Aixo serveix per pasar el numero decimal a un numero enter (s'arrodoneix al numero més a prop)
print(f"Si faltes a més de {variable4} hores de la {variable1} has perdut el dret d'avaluació") 
