def conver(currency_type, dollar_value):
    pesos = input("Cuántos "+currency_type+" tienes?: ")
    pesos = float(pesos)

    valor_dolar = dollar_value
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    dolares = str(dolares)

    print("Tienes $"+dolares+ " dolares")

menu = """
Bienvenido al conversor de monedas ❤

1 - Quetzales
2 - Pesos Argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))



if opcion == 1:
    conver("quetzales", 7.7)
elif opcion == 2:
    conver("pesos argentinos", 65)
elif opcion ==3:
    conver("pesos mexicanos", 24)
else:
    print("Ingrese una opción valida")

