# Programa fet per Victor A.C  6/05/2024
# El nom del fitxer sera M15-UF1_Activitat7_AlvarezCalvoVictor.py
# El programa realitza dos funcions que facin la conversió entre Celsius i Fahrenheit.

def imprimir_capçalera():
    print("=" * 40)
    print("PROGRAMA QUE CONVERTEIX TEMPERATURA")
    print("{:^40}".format("Celsius (c) <==> Fahrenheit (f)"))
    print("=" * 40)

def celsius_a_fahrenheit(celsius):
    return (9.0 / 5) * celsius + 32

def fahrenheit_a_celsius(fahrenheit):
    return (5.0 / 9) * (fahrenheit - 32)

def main():
    imprimir_capçalera()
    temperatura = float(input("Introdueix la temperatura: "))
    unitat = input("Està en Celsius (c) o Fahrenheit (f)?: ")
    if unitat == 'c':
        print(f"{temperatura}º Celsius són {celsius_a_fahrenheit(temperatura):.2f}º Fahrenheit")
    elif unitat == 'f':
        print(f"{temperatura}º Fahrenheit són {fahrenheit_a_celsius(temperatura):.2f}º Celsius")
    else:
        print("Entrada no vàlida. Si us plau, introdueix 'c' per Celsius o 'f' per Fahrenheit.")

main()