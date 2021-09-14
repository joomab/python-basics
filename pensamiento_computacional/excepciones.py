
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e: #Cuando la excepción ocurre en ejecución y no hay ningun try except, sale en la consola este ZeroDivisionError (por lo que la podemoas agregar aquí luego de una excepcion :D)
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))