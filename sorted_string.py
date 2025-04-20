"""Tome 2 strings S1 y S2, incluidas solo 
letras de A a Z. Devuelva una nueva cadena
 ordenada (ascendente alfabético), la más 
 larga posible, que contiene letras distintas, 
 cada una tomada solo una vez, proveniente de S1 o S2."""

def longest(a, b):
    a = a.lower()
    b = b.lower()
    combined = set(a + b)
    sorted_combined = ''.join(sorted(combined))
    return sorted_combined
print(longest("xyaabbbccccdefww", "xxxxyyyyabklmjopq"))

#otra forma de hacerlo 
def longest(a, b):
    return "".join(sorted(set(a.lower() + b.lower())))

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmjopq"))