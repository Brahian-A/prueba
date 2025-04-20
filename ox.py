"""Verifique si una cadena tiene la misma cantidad de
 'X y' O's. El método debe devolver un booleano y ser 
 insensible al caso. La cadena puede contener cualquier char."""

s = 'xxoo'

def xo(s):
    s = s.lower()
    x_count = s.count('x')
    o_count = s.count('o')
    return x_count == o_count
print(xo(s))

# Otra forma de hacerlo
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
print(xo(s))

# Otra forma de hacerlo
def xo(s):
    return s.lower().count('x') == s.count('o')
print(xo(s))
