"""
Excepciones comunes:
ImportError : una importación falla;
IndexError : una lista se indexa con un número fuera de rango;
NameError : se usa una variable desconocida ;
SyntaxError : el código no se puede analizar correctamente
TypeError : se llama a una función en un valor de un tipo inapropiado;
ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado
"""

def divide_elementos_lista(lista, divisor):
    #Si intento dividir por cero, enviara ese error, entonces lo cacheo y retorno la lista original
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print (e)
        return lista



lista = list(range(10))
divisor = 0

print (lista)
