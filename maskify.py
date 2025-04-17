"""
Por lo general, cuando compra algo, se le pregunta si su número de tarjeta de crédito, número de teléfono o respuesta a su pregunta más secreta sigue siendo correcta. Sin embargo, dado que alguien podría mirar por encima del hombro,
 no desea que se muestre en su pantalla. En cambio, lo enmascaramos.
Su tarea es escribir una función Maskify,
que cambia todos menos los últimos cuatro caracteres en '#'. """

cc = "1234567890123456"

def maskify(cc):
    if len(cc) <= 4:
        return (cc)
    else:
        return '#' * (len(cc)- 4) + cc[-4:]
                                    # operador slicing [:] El índice -4 indica que Python debe empezar a contar desde el cuarto carácter desde el final de la cadena.
                                    #El índice vacío después de los dos puntos (:) significa "hasta el final de la cadena".
print(maskify(cc))

"""Los índices negativos comienzan desde el final de la cadena.
cc[-1] es el último carácter.
cc[-2] es el penúltimo carácter.
Y así sucesivamente.
Cuando usas slicing con un índice negativo, como cc[-4:], Python automáticamente 
interpreta que debe empezar desde el índice negativo especificado (-4) y continuar hasta el final."""

