# Funcions

# def + nom(paràmetres)

def funcio():
    print("Hola")

funcio()

def sumar1(x,y): # Paràmetres entre () s'han d'especificar al trucar la funcio
    print(x+y)

primernombre = int(input("Primer nombre: "))
segonnombre = int(input("Segon nombre: "))

# sumar1(primernombre,segonnombre)

def sumar2(x,y):
    return x+y # return no fa res per si sol, tu trias que fer, si assignar-lo a variable, posar-ho com a text a un print, etc...

resultat = sumar2(primernombre,segonnombre)
print(sumar2(primernombre,segonnombre))