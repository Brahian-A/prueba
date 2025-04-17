"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

str1 = "amor"
str2 = "roma"

def is_anagrama(str1, str2):
    # Convertimos las palabras a minúsculas
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Comprobamos si las longitudes son diferentes
    if len(str1) != len(str2):
        return False
    
    # Comprobamos si las letras son iguales
    for letra in str1:
        if str1.count(letra) != str2.count(letra):
            return False
    
    return True
print(is_anagrama(str1, str2))