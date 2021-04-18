menu = """
Bienvenido al conversor de monedas ❤

1 - Quetzales
2 - Pesos Argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuántos Quetzales tienes?: ")
    pesos = float(pesos)

    valor_dolar = 7.7
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    dolares = str(dolares)

    print("Tienes $"+dolares+ " dolares")
elif opcion == 2:
    pesos = input("Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)

    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    dolares = str(dolares)

    print("Tienes $"+dolares+ " dolares")
elif opcion ==3:
    pesos = input("Cuántos pesos mexicanos tienes tienes?: ")
    pesos = float(pesos)

    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    dolares = str(dolares)

    print("Tienes $"+dolares+ " dolares")
else:
    print("Ingrese una opción valida")

