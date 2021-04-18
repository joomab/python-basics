def run():
    mi_diccionario = {
        "llave1":1,
        "llave2": 2,
        "llave3": 3
    }

    print(mi_diccionario["llave1"])

    poblacion_pais = {
        "Arg": 44_938_712,
        "Bra": 210147125,
        "Col": 50372424
    }

    # print(poblacion_pais['Arg'])

    for pais in poblacion_pais.keys():
        print(pais)

    for pais in poblacion_pais.values():
        print(pais)

    for pais, poblacion in poblacion_pais.items():
        print(pais, " Pob: "+ str(poblacion))

    
    lista_diccionario = [
        {"id": 1},
        {"id": 2}
    ]

    for obj in lista_diccionario:
        print(obj["id"])

if __name__ == "__main__":
    run()