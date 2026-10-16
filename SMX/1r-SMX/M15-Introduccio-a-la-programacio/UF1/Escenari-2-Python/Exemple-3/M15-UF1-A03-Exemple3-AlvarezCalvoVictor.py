# Programa fet per Victor A.C
# Data: 6/11/2023
# Nom del "script": A01_exemple3_VictorAC.py
# Descripció: Conjunt d'instruccions i elements bàsics del llenguatge Python.
# Veurem exemples de: tipus de dades, conversió entre tipus, operadors, blocs de codi i identació

print("=== EXEMPLE D'INTRUCCIONS BÀSIQUES AMB PYTHON ===")

#1-Variables ================================
print("----- VARIABLES -----")
x=8        #Crear i assignar valor a variable X de tipus INTEGER (sencer)
print("x=",x) #Mostra el valor de la varibale X
print(type(x)) #Mostra el TIPUS de la varibale X
x="Hello" #Assignar un valor diferent de TIPUS STRING (cadena de caràcteres)
print ("x=", x) #Mostra el nou valor
print (type (x)) #Mostra el nou TIPUS


#2- Tipus de dades ============================
print("\n \n----- TIPUS DE DADES -----")
#help(str) #Dona error
#help(str) #Mostra informacio de l'ajuda

cadena = "Hola Mundo" #Cadenas de cacarcteres
print("Exemple de cadena:",cadena)

help(str) #Et dona ajuda de comandes
type(cadena) #Et diu el tipus de dades <class 'str'>
entero = 23 #dona un numero sencer
type(entero) #Et diu el tipus de dades <class 'int'>
certfals = False #Valor booleano
type(certfals) #Et diu el tipus de dades que es <class 'bool'>


#3-Tipus de Booleans=======================
girar=False #Dona fals al valor
type(girar) #Et dona la classe de la variable girar
esGroc = True #Dona num zero en tots el tipos
type(esGroc) #Et dona la classe de esGroc 
x = None #Dona none al valor

#5-Conversió entre tipus==================
meutextnumeric=input("introdueix un número:") #Es per posar un numero i ho guardara a la varible 
print(meutextnumeric) #Et posara a pantalla el numero guardat
type(meutextnumeric) #Et dona la classe que es

numero=5 #Guarda el numero amb valor fix
print(numero, type(numero)) #Et posa el numero i et diu quina classe es
print(numero, type(str(numero))) #Et posa el tipus de str a la variable
int(False) #Dona 0
int(True) #Dona 1

#6-Operadors=========================
2 + 4 #Suma els dos valors que hem selecionat
2**4 #Fa una elevat del numero 2
2 - 4 #Resta els dos valors que hem selecionat
3/4 #Fa la divisio dels dos numeros selecionats
-5-4 #Fa la resta de la resta
3//4 #Divideix el numero de l'esquerra amb el de la dreta
5*4 #Multplica els numeros
3 % 4 # Divideix els numeros

5==5 #Fa igual que els dos numeros, i et dona True
4!=5 #Fa diferent que els dos numeros i dona True
98>100 #Fa major que el numero i es False
12>=39 #Fa menor que el numero i es False
6>=6 #Fa major o igual que el numero i es True
3<=8 #Fa menor o igual que el numero i es True

12>2 and 5<10 #And retorna true si las dos operacions son Trues
9!=6 or 8<=5 #Or retorna true si una de les dos opreracions es true
not True #Not retorna lo contrari que han posat


#7-Blocs de codi===============
if 5 > 10: #Fa que si la condicio anterior es compelix fagi un print)
else: #Fa que en cas contrari de la condicio fagi un print

for x in range(0, 50):
    print(x) #Això s’executa totes les vegades que dura el bucle: 50 iteracions
    print(2*x) #Això també s’executa 50 vegades
    print(x) # Imprimir últim valor de x del bucle
X = 0 # Inicialitzar la Variable comptador
while x <= 49:
    print(x) # Això s’executa totes les vegades que dura el bucle: 50 iteracions
    print(2*x) # Això també s’executa 50 vegades
x = x + 1 # Això permet que la variable sigui «comptador» d’un en un