#Progarma fet per Victor A.C 11/12/23
#Pasar de decimal a binari

#Printea el resultat dels numeros donats passat a hexadecimal
Num1 = input("Posa el primer numero i ho passara a hexadecimal: ")
resultatHex = hex ( int(Num1) ) 
print (resultatHex)

#Printea el resultat dels numeros donats passats a octal
Num2 = input("Posa el segon numero i ho passara a octal: ")
resultatOctal = oct ( int(Num2) )
print (resultatOctal) 

#Printea el resultat dels numeros donats passats a binari
Num3 = input("Posa el tercer numero i ho passara a binari: ")
resultatBinari = bin( int(Num3) )
print (resultatBinari) 

