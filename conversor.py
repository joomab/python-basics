pesos = input("Cuántos Quetzales tienes?: ")
pesos = float(pesos)

valor_dolar = 7.7
dolares = pesos / valor_dolar
dolares = round(dolares, 2)

dolares = str(dolares)

print("Tienes $"+dolares+ " dolares")