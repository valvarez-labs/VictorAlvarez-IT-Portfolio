# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat1_AlvarezCalvoVictor.py
# El programa realitzar una funció, a la que li passem com a paràmetre un nombre N 
# demanat a l'usuari  i mostri per pantalla N vegades el missatge: “Mòdul executant-se”.

def mostrar_missatge(N):
    for i in range(N):
        print("Mòdul executant-se")
        
def main():
    num_vegades = int(input("Quantes vegades l'he de repetir?: "))
    mostrar_missatge(num_vegades)  

main()