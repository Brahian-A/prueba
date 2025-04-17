
seq = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10,]

def find_it(seq):
    for num in set(seq):
        if seq.count(num) % 2 == 1:
            return num
    return None

print(find_it(seq))

"""set es un tipo de dato que representa un conjunto. 
Un conjunto es una colección desordenada de elementos únicos, 
es decir, no permite duplicados. Cuando usas for in set, estás 
iterando sobre los elementos únicos de ese conjunto."""