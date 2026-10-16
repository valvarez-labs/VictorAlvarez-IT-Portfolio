# Convertir a binari, octal i hexadecimal
    binari = bin(num)
    octal = oct(num)
    hexadecimal = hex(num)
    return binari, octal, hexadecimal

# Demanar a l'usuari que introdueixi un nombre decimal
nombre_decimal = int(input("Introdueix un nombre en decimal: "))

# Convertir el nombre a binari, octal i hexadecimal
resultats = convertir_a_binari_octal_hexadecimal(nombre_decimal)
